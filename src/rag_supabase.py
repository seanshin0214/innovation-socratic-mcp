"""
RAG Engine with Supabase Backend
Supabase + pgvector 기반 원격 벡터 검색

로컬 ChromaDB 대신 Supabase를 사용하여:
- 모든 사용자가 동일한 지식 베이스 접근
- 지식 업데이트 시 실시간 반영
- 하이브리드 검색 (벡터 + 메타데이터)

환경변수:
    SUPABASE_URL: Supabase 프로젝트 URL
    SUPABASE_KEY: Supabase anon/service key
    OPENAI_API_KEY: OpenAI API key (임베딩용)

SUPABASE_URL이 없으면 자동으로 로컬 ChromaDB로 fallback
"""

import os
import sys
from typing import List, Dict, Any, Optional
from pathlib import Path

# Supabase 의존성 확인
try:
    from supabase import create_client, Client
    from openai import OpenAI
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False


class SupabaseRAGEngine:
    """Supabase 기반 RAG 엔진"""

    def __init__(
        self,
        supabase_url: Optional[str] = None,
        supabase_key: Optional[str] = None,
        openai_key: Optional[str] = None,
        lazy_init: bool = True
    ):
        self.supabase_url = supabase_url or os.environ.get('SUPABASE_URL')
        self.supabase_key = supabase_key or os.environ.get('SUPABASE_KEY')
        self.openai_key = openai_key or os.environ.get('OPENAI_API_KEY')

        self.supabase: Optional[Client] = None
        self.openai: Optional[OpenAI] = None
        self._initialized = False
        self.indexed = True  # Supabase는 이미 인덱싱됨

        # 필요한 키가 있으면 사용 가능
        self.available = bool(
            SUPABASE_AVAILABLE and
            self.supabase_url and
            self.supabase_key and
            self.openai_key
        )

        if not lazy_init and self.available:
            self._initialize()

    def _initialize(self):
        """클라이언트 초기화"""
        if self._initialized:
            return

        try:
            self.supabase = create_client(self.supabase_url, self.supabase_key)
            self.openai = OpenAI(api_key=self.openai_key)
            self._initialized = True
            print("Supabase RAG Engine initialized", file=sys.stderr)
        except Exception as e:
            print(f"Supabase init error: {e}", file=sys.stderr)
            self.available = False

    def _ensure_initialized(self):
        """Lazy initialization"""
        if not self._initialized and self.available:
            self._initialize()

    def _generate_embedding(self, text: str) -> List[float]:
        """텍스트 임베딩 생성"""
        response = self.openai.embeddings.create(
            model="text-embedding-3-small",
            input=text[:8000]
        )
        return response.data[0].embedding

    def search(
        self,
        query: str,
        n_results: int = 5,
        category: Optional[str] = None,
        difficulty: Optional[str] = None,
        threshold: float = 0.5
    ) -> List[Dict[str, Any]]:
        """
        하이브리드 시맨틱 검색

        Args:
            query: 검색 쿼리
            n_results: 결과 수
            category: 카테고리 필터
            difficulty: 난이도 필터
            threshold: 유사도 임계값

        Returns:
            검색 결과 리스트
        """
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return []

        try:
            # 쿼리 임베딩 생성
            query_embedding = self._generate_embedding(query)

            # RPC 호출 (search_thinking_tools 함수)
            result = self.supabase.rpc(
                'search_thinking_tools',
                {
                    'query_embedding': query_embedding,
                    'match_threshold': threshold,
                    'match_count': n_results,
                    'filter_category': category,
                    'filter_difficulty': difficulty
                }
            ).execute()

            # 결과 포맷팅
            formatted = []
            for row in result.data:
                formatted.append({
                    'id': row['id'],
                    'title': row['title'],
                    'category': row['category'],
                    'difficulty': row.get('difficulty', ''),
                    'relevance_score': round(row.get('similarity', 0), 3),
                    'related_methods': row.get('related_methods', []),
                    'complementary_methods': row.get('complementary_methods', [])
                })

            return formatted

        except Exception as e:
            print(f"Supabase search error: {e}", file=sys.stderr)
            return []

    def get_related(self, tool_id: str) -> List[Dict[str, Any]]:
        """관련 도구 조회"""
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return []

        try:
            result = self.supabase.rpc(
                'get_related_tools',
                {'tool_id': tool_id}
            ).execute()

            return result.data

        except Exception as e:
            print(f"Get related error: {e}", file=sys.stderr)
            return []

    def get_tool_content(self, tool_id: str) -> Optional[Dict[str, Any]]:
        """도구 상세 내용 조회"""
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return None

        try:
            result = self.supabase.table('thinking_tools').select(
                'id, title, category, difficulty, content, '
                'keywords, use_cases, related_methods, complementary_methods'
            ).eq('id', tool_id).single().execute()

            return result.data

        except Exception as e:
            print(f"Get tool error: {e}", file=sys.stderr)
            return None

    def search_by_use_case(self, use_case: str) -> List[Dict[str, Any]]:
        """Use case 기반 검색"""
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return []

        try:
            result = self.supabase.rpc(
                'search_by_use_case',
                {'use_case': use_case}
            ).execute()

            return result.data

        except Exception as e:
            print(f"Use case search error: {e}", file=sys.stderr)
            return []

    def get_by_category(self, category: str) -> List[Dict[str, Any]]:
        """카테고리별 도구 조회"""
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return []

        try:
            result = self.supabase.table('thinking_tools').select(
                'id, title, difficulty, time_required'
            ).eq('category', category).order('title').execute()

            return result.data

        except Exception as e:
            print(f"Category search error: {e}", file=sys.stderr)
            return []

    def get_categories(self) -> List[Dict[str, Any]]:
        """모든 카테고리 조회"""
        self._ensure_initialized()

        if not self.available or not self.supabase:
            return []

        try:
            result = self.supabase.table('categories').select('*').execute()
            return result.data
        except:
            return []

    def get_stats(self) -> Dict[str, Any]:
        """통계 정보"""
        self._ensure_initialized()

        stats = {
            'backend': 'supabase',
            'available': self.available,
            'initialized': self._initialized
        }

        if self.available and self.supabase:
            try:
                result = self.supabase.table('thinking_tools').select(
                    'id', count='exact'
                ).execute()
                stats['docs'] = result.count
            except:
                pass

        return stats

    # 하위 호환 메서드 (로컬 RAG 인터페이스 유지)
    def index_knowledge(self, force: bool = False) -> Dict[str, Any]:
        """Supabase는 서버에서 인덱싱됨 - no-op"""
        return {
            'success': True,
            'message': 'Supabase backend - indexing managed server-side',
            'indexed': True
        }

    def query_relevant_chunks(self, query: str, top_k: int = 3):
        """search 메서드 래퍼"""
        return self.search(query, n_results=top_k)


class HybridRAGEngine:
    """
    하이브리드 RAG 엔진
    - Supabase 사용 가능하면 원격 검색
    - 아니면 로컬 ChromaDB 사용
    """

    def __init__(self, knowledge_path: Optional[str] = None, lazy_init: bool = True):
        self.supabase_engine = SupabaseRAGEngine(lazy_init=lazy_init)
        self._local_engine = None
        self.knowledge_path = knowledge_path
        self.lazy_init = lazy_init

    @property
    def _use_supabase(self) -> bool:
        """Supabase 사용 가능 여부"""
        return self.supabase_engine.available

    @property
    def local_engine(self):
        """
        로컬 ChromaDB 엔진 (lazy load)
        NOTE: 사용자가 별도로 설정할 필요 없음 - 자동으로 rag.py를 찾아서 임포트
        """
        if self._local_engine is None:
            # [자동] 모듈 또는 패키지 실행 방식에 따라 적절한 import 사용
            try:
                from .rag import RAGEngine
            except ImportError:
                from rag import RAGEngine
            self._local_engine = RAGEngine(
                knowledge_path=self.knowledge_path,
                lazy_init=self.lazy_init
            )
        return self._local_engine

    def search(self, query: str, n_results: int = 5, **kwargs) -> List[Dict[str, Any]]:
        """검색 - Supabase 우선, fallback to local"""
        if self._use_supabase:
            results = self.supabase_engine.search(query, n_results, **kwargs)
            if results:
                return results

        # Fallback to local
        return self.local_engine.search(query, n_results)

    def get_related(self, tool_id: str) -> List[Dict[str, Any]]:
        """관련 도구 - Supabase only"""
        if self._use_supabase:
            return self.supabase_engine.get_related(tool_id)
        return []

    def get_tool_content(self, tool_id: str) -> Optional[Dict[str, Any]]:
        """도구 내용 - Supabase only"""
        if self._use_supabase:
            return self.supabase_engine.get_tool_content(tool_id)
        return None

    def index_knowledge(self, force: bool = False) -> Dict[str, Any]:
        """인덱싱"""
        if self._use_supabase:
            return self.supabase_engine.index_knowledge(force)
        return self.local_engine.index_knowledge(force)

    def get_stats(self) -> Dict[str, Any]:
        """통계"""
        if self._use_supabase:
            stats = self.supabase_engine.get_stats()
            stats['fallback'] = 'chromadb'
            return stats
        return self.local_engine.get_stats()

    # 하위 호환
    def query_relevant_chunks(self, query: str, top_k: int = 3):
        return self.search(query, n_results=top_k)


# 글로벌 인스턴스 (HybridRAGEngine 사용)
rag_engine = HybridRAGEngine(lazy_init=True)


if __name__ == "__main__":
    print("Socratic RAG Engine (Supabase + ChromaDB Hybrid)")
    print(f"Stats: {rag_engine.get_stats()}")

    # 테스트 검색
    for q in ["목표 설정", "아이디어 발상", "근본 원인 분석"]:
        results = rag_engine.search(q, n_results=3)
        print(f"\n'{q}':")
        for r in results:
            print(f"  - {r['title']} ({r.get('relevance_score', 0):.2f})")
