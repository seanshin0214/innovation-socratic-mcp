"""
RAG (Retrieval-Augmented Generation) Integration
사용자 업로드 문서 분석 및 질문 생성
"""

from typing import List, Dict, Any, Optional
from pathlib import Path


class RAGEngine:
    """
    RAG 엔진 (간단한 버전)
    실제 구현에서는 벡터 DB (Chroma, Pinecone 등) 사용 권장
    """

    def __init__(self):
        self.documents: Dict[str, str] = {}  # {doc_id: content}
        self.indexed = False

    def add_document(
        self,
        doc_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        문서 추가

        Args:
            doc_id: 문서 ID
            content: 문서 내용
            metadata: 메타데이터 (선택사항)

        Returns:
            성공 여부
        """
        try:
            self.documents[doc_id] = content
            self.indexed = False  # 재색인 필요
            return True
        except Exception as e:
            print(f"문서 추가 실패: {e}")
            return False

    def load_pdf(self, pdf_path: str) -> bool:
        """
        PDF 파일 로드

        실제 구현에서는 PyPDF2, pdfplumber 등 사용
        여기서는 placeholder
        """
        # TODO: PDF 파싱 구현
        # from PyPDF2 import PdfReader
        # reader = PdfReader(pdf_path)
        # content = ""
        # for page in reader.pages:
        #     content += page.extract_text()

        doc_id = Path(pdf_path).stem
        # self.add_document(doc_id, content)

        return True

    def query_relevant_chunks(
        self,
        query: str,
        top_k: int = 3
    ) -> List[Dict[str, Any]]:
        """
        쿼리와 관련된 문서 청크 검색

        Args:
            query: 검색 쿼리
            top_k: 상위 K개 결과

        Returns:
            관련 청크 리스트
        """
        # 간단한 키워드 매칭 (실제로는 벡터 유사도 검색)
        results = []

        query_lower = query.lower()

        for doc_id, content in self.documents.items():
            # 청크로 분할 (문단 단위)
            chunks = content.split('\n\n')

            for i, chunk in enumerate(chunks):
                if not chunk.strip():
                    continue

                # 간단한 점수 계산 (키워드 매칭)
                score = sum(1 for word in query_lower.split() if word in chunk.lower())

                if score > 0:
                    results.append({
                        "doc_id": doc_id,
                        "chunk_id": i,
                        "content": chunk,
                        "score": score
                    })

        # 점수 순 정렬
        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:top_k]

    def generate_context_questions(
        self,
        method_id: str,
        document_chunks: List[Dict[str, Any]]
    ) -> List[str]:
        """
        문서 컨텍스트 기반 맞춤 질문 생성

        Args:
            method_id: 방법론 ID
            document_chunks: 관련 문서 청크

        Returns:
            맞춤 질문 리스트
        """
        # 문서 내용 요약
        context_summary = " ".join([
            chunk["content"][:100] for chunk in document_chunks
        ])

        # 방법론별 맞춤 질문 생성
        # 실제로는 LLM을 사용하여 생성
        # 여기서는 간단한 템플릿 사용

        questions = []

        if method_id == "scamper":
            questions.append(f"문서에서 언급된 요소 중 무엇을 대체할 수 있습니까?")
            questions.append(f"문서의 개념들을 어떻게 결합할 수 있습니까?")

        elif method_id == "five_whys":
            questions.append(f"문서에서 식별된 문제는 왜 발생합니까?")

        elif method_id == "six_hats":
            questions.append(f"문서의 사실적 데이터는 무엇입니까? (White Hat)")

        # 기본 질문
        questions.append(f"문서의 핵심 개념을 {method_id} 방법론으로 어떻게 분석할 수 있습니까?")

        return questions

    def analyze_document_with_method(
        self,
        doc_id: str,
        method_id: str,
        problem_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        문서를 특정 방법론으로 분석

        Args:
            doc_id: 문서 ID
            method_id: 방법론 ID
            problem_context: 문제 컨텍스트

        Returns:
            분석 결과
        """
        if doc_id not in self.documents:
            return {"error": f"문서를 찾을 수 없습니다: {doc_id}"}

        # 관련 청크 검색
        query = problem_context if problem_context else method_id
        chunks = self.query_relevant_chunks(query, top_k=5)

        # 맞춤 질문 생성
        questions = self.generate_context_questions(method_id, chunks)

        return {
            "doc_id": doc_id,
            "method": method_id,
            "relevant_chunks": len(chunks),
            "custom_questions": questions,
            "chunks_preview": [
                {"content": c["content"][:200] + "...", "score": c["score"]}
                for c in chunks[:3]
            ]
        }

    def clear_documents(self):
        """모든 문서 삭제"""
        self.documents.clear()
        self.indexed = False


# 싱글톤 인스턴스
rag_engine = RAGEngine()
