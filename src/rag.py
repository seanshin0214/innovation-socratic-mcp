"""
RAG (Retrieval-Augmented Generation) Integration
ChromaDB 기반 벡터 검색으로 사고 방법론 추천

NOTE: Lazy initialization is used to prevent slow server startup.
ChromaDB and SentenceTransformer models are loaded only when first needed.
"""

import os
import sys
import yaml
from typing import List, Dict, Any, Optional
from pathlib import Path

try:
    import chromadb
    from chromadb.utils import embedding_functions
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False


class RAGEngine:
    def __init__(self, knowledge_path: Optional[str] = None, lazy_init: bool = True):
        self.knowledge_path = knowledge_path or self._find_knowledge_path()
        self.collection = None
        self.client = None
        self.embedding_fn = None
        self.indexed = False
        self.documents: Dict[str, str] = {}
        self._initialized = False

        # Only initialize immediately if not lazy (for CLI usage)
        if not lazy_init and CHROMADB_AVAILABLE:
            self._initialize_chromadb()
            self._initialized = True

    def _ensure_initialized(self):
        """Lazy initialization - only initialize ChromaDB when first needed"""
        if not self._initialized and CHROMADB_AVAILABLE:
            print("Initializing ChromaDB (lazy)...", file=sys.stderr)
            self._initialize_chromadb()
            self._initialized = True

    def _find_knowledge_path(self) -> str:
        current_dir = Path(__file__).parent.parent
        knowledge_dir = current_dir / "knowledge"
        if knowledge_dir.exists():
            return str(knowledge_dir)
        env_path = os.environ.get("INNOVATION_SOCRATIC_KNOWLEDGE_PATH")
        if env_path and Path(env_path).exists():
            return env_path
        return str(knowledge_dir)

    def _initialize_chromadb(self):
        try:
            persist_dir = Path(self.knowledge_path).parent / ".chromadb"
            persist_dir.mkdir(exist_ok=True)
            self.client = chromadb.PersistentClient(path=str(persist_dir))
            self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="paraphrase-multilingual-MiniLM-L12-v2"
            )
            self.collection = self.client.get_or_create_collection(
                name="socratic_methods",
                embedding_function=self.embedding_fn
            )
            if self.collection.count() > 0:
                self.indexed = True
        except Exception as e:
            print(f"ChromaDB error: {e}", file=sys.stderr)
            self.collection = None

    def _parse_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        content = file_path.read_text(encoding='utf-8')
        metadata = {}
        body = content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1]) or {}
                except:
                    pass
                body = parts[2].strip()
        return {
            "id": metadata.get("id", file_path.stem),
            "file": file_path.name,
            "title": metadata.get("title", file_path.stem),
            "aliases": metadata.get("aliases", []),
            "category": metadata.get("category", "general"),
            "use_cases": metadata.get("use_cases", []),
            "keywords": metadata.get("keywords", []),
            "body": body
        }

    def _create_searchable_text(self, doc: Dict[str, Any]) -> str:
        parts = [doc["title"], " ".join(doc.get("aliases", [])),
                 " ".join(doc.get("keywords", [])), " ".join(doc.get("use_cases", [])),
                 doc.get("body", "")[:2000]]
        return " ".join(filter(None, parts))

    def index_knowledge(self, force: bool = False) -> Dict[str, Any]:
        self._ensure_initialized()

        if not CHROMADB_AVAILABLE or not self.collection:
            return {"success": False, "error": "ChromaDB not available"}

        if force and self.collection.count() > 0:
            ids = self.collection.get()["ids"]
            if ids:
                self.collection.delete(ids=ids)

        knowledge_path = Path(self.knowledge_path)
        md_files = [f for f in sorted(knowledge_path.glob("*.md"))
                    if not f.name.startswith("_") and f.name != "README.md"]

        indexed = 0
        for f in md_files:
            try:
                doc = self._parse_markdown_file(f)
                self.collection.add(
                    ids=[doc["id"]], documents=[self._create_searchable_text(doc)],
                    metadatas=[{"file": doc["file"], "title": doc["title"],
                               "category": doc["category"],
                               "use_cases": ", ".join(doc.get("use_cases", []))}]
                )
                indexed += 1
            except Exception as e:
                print(f"Index error {f.name}: {e}", file=sys.stderr)

        self.indexed = True
        return {"success": True, "indexed": indexed, "total": len(md_files)}

    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        self._ensure_initialized()

        if not CHROMADB_AVAILABLE or not self.collection:
            return self._fallback_search(query, n_results)

        if not self.indexed:
            self.index_knowledge()

        try:
            results = self.collection.query(query_texts=[query], n_results=n_results)
            formatted = []
            if results["ids"] and results["ids"][0]:
                for i, id in enumerate(results["ids"][0]):
                    meta = results["metadatas"][0][i] if results["metadatas"] else {}
                    dist = results["distances"][0][i] if results.get("distances") else 0
                    formatted.append({
                        "id": id, "title": meta.get("title", id),
                        "file": meta.get("file", ""), "category": meta.get("category", ""),
                        "relevance_score": round(1 - dist, 3),
                        "use_cases": meta.get("use_cases", "")
                    })
            return formatted
        except Exception as e:
            return self._fallback_search(query, n_results)

    def _fallback_search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        knowledge_path = Path(self.knowledge_path)
        if not knowledge_path.exists():
            return []
        query_words = set(query.lower().split())
        results = []
        for f in knowledge_path.glob("*.md"):
            if f.name.startswith("_") or f.name == "README.md":
                continue
            try:
                doc = self._parse_markdown_file(f)
                text = self._create_searchable_text(doc).lower()
                score = sum(1 for w in query_words if w in text)
                if score > 0:
                    results.append({"id": doc["id"], "title": doc["title"],
                                   "relevance_score": score / len(query_words)})
            except:
                continue
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return results[:n_results]

    def get_stats(self) -> Dict[str, Any]:
        self._ensure_initialized()
        stats = {"chromadb": CHROMADB_AVAILABLE, "indexed": self.indexed}
        if self.collection:
            stats["docs"] = self.collection.count()
        return stats

    # 하위 호환
    def add_document(self, doc_id: str, content: str, metadata=None) -> bool:
        self.documents[doc_id] = content
        return True

    def query_relevant_chunks(self, query: str, top_k: int = 3):
        return self.search(query, n_results=top_k)

    def generate_context_questions(self, method_id: str, chunks) -> List[str]:
        return [f"'{method_id}' 방법론으로 분석하세요"]

    def clear_documents(self):
        self.documents.clear()


# Global instance with lazy initialization (default for MCP server)
rag_engine = RAGEngine(lazy_init=True)

if __name__ == "__main__":
    import sys
    print("Socratic RAG Engine (ChromaDB)")
    print(f"Stats: {rag_engine.get_stats()}")
    if "--index" in sys.argv:
        print(rag_engine.index_knowledge(force="--force" in sys.argv))
    for q in ["목표 설정", "아이디어 발상"]:
        print(f"\n'{q}':", [r["title"] for r in rag_engine.search(q, 3)])
