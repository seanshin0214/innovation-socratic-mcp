"""
Socratic Thinking MCP - Supabase Search Client
하이브리드 검색 (벡터 + 메타데이터) 클라이언트

사용법:
    from supabase.search_client import SocraticSearchClient

    client = SocraticSearchClient()

    # 시맨틱 검색
    results = client.search("문제의 근본 원인을 찾는 방법")

    # 카테고리 필터 검색
    results = client.search("브레인스토밍", category="creative_divergent")

    # 관련 도구 조회
    related = client.get_related("question-storming")

    # Use case 기반 검색
    tools = client.search_by_use_case("root_cause_analysis")
"""

import os
from typing import Optional
from dataclasses import dataclass

try:
    from supabase import create_client, Client
    from openai import OpenAI
except ImportError as e:
    raise ImportError(f"Missing dependency: {e}. Install with: pip install supabase openai")


@dataclass
class SearchResult:
    """검색 결과 데이터 클래스"""
    id: str
    title: str
    category: str
    difficulty: str
    content: str
    similarity: float
    related_methods: list
    complementary_methods: list


@dataclass
class RelatedTool:
    """관련 도구 데이터 클래스"""
    id: str
    title: str
    category: str
    relation_type: str  # 'related' or 'complementary'


class SocraticSearchClient:
    """Socratic Thinking 지식 베이스 검색 클라이언트"""

    def __init__(
        self,
        supabase_url: Optional[str] = None,
        supabase_key: Optional[str] = None,
        openai_key: Optional[str] = None
    ):
        """
        클라이언트 초기화

        Args:
            supabase_url: Supabase 프로젝트 URL (기본: 환경변수)
            supabase_key: Supabase API 키 (기본: 환경변수)
            openai_key: OpenAI API 키 (기본: 환경변수)
        """
        self.supabase_url = supabase_url or os.environ.get('SUPABASE_URL')
        self.supabase_key = supabase_key or os.environ.get('SUPABASE_KEY')
        self.openai_key = openai_key or os.environ.get('OPENAI_API_KEY')

        if not all([self.supabase_url, self.supabase_key, self.openai_key]):
            raise ValueError(
                "Missing credentials. Set SUPABASE_URL, SUPABASE_KEY, OPENAI_API_KEY "
                "environment variables or pass them to constructor."
            )

        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)
        self.openai = OpenAI(api_key=self.openai_key)

    def _generate_embedding(self, text: str) -> list[float]:
        """텍스트 임베딩 생성"""
        response = self.openai.embeddings.create(
            model="text-embedding-3-small",
            input=text[:8000]  # 토큰 제한
        )
        return response.data[0].embedding

    def search(
        self,
        query: str,
        category: Optional[str] = None,
        difficulty: Optional[str] = None,
        threshold: float = 0.7,
        limit: int = 5,
        include_related: bool = True
    ) -> list[SearchResult]:
        """
        하이브리드 시맨틱 검색

        Args:
            query: 검색 쿼리
            category: 카테고리 필터 (예: 'creative_divergent')
            difficulty: 난이도 필터 (예: 'beginner')
            threshold: 유사도 임계값 (0-1)
            limit: 최대 결과 수
            include_related: 관련 도구 포함 여부

        Returns:
            검색 결과 리스트
        """
        # 쿼리 임베딩 생성
        query_embedding = self._generate_embedding(query)

        # RPC 호출 (search_thinking_tools 함수)
        result = self.supabase.rpc(
            'search_thinking_tools',
            {
                'query_embedding': query_embedding,
                'match_threshold': threshold,
                'match_count': limit,
                'filter_category': category,
                'filter_difficulty': difficulty
            }
        ).execute()

        results = []
        for row in result.data:
            results.append(SearchResult(
                id=row['id'],
                title=row['title'],
                category=row['category'],
                difficulty=row['difficulty'],
                content=row['content'],
                similarity=row['similarity'],
                related_methods=row.get('related_methods', []),
                complementary_methods=row.get('complementary_methods', [])
            ))

        return results

    def search_by_keyword(
        self,
        keyword: str,
        limit: int = 10
    ) -> list[dict]:
        """
        키워드 기반 검색

        Args:
            keyword: 검색할 키워드
            limit: 최대 결과 수

        Returns:
            매칭된 도구 리스트
        """
        result = self.supabase.table('thinking_tools').select(
            'id, title, category, difficulty'
        ).contains('keywords', [keyword]).limit(limit).execute()

        return result.data

    def search_by_use_case(self, use_case: str) -> list[dict]:
        """
        Use case 기반 검색

        Args:
            use_case: 사용 사례 (예: 'problem_definition', 'idea_generation')

        Returns:
            매칭된 도구 리스트
        """
        result = self.supabase.rpc(
            'search_by_use_case',
            {'use_case': use_case}
        ).execute()

        return result.data

    def get_related(self, tool_id: str) -> list[RelatedTool]:
        """
        관련 도구 조회

        Args:
            tool_id: 도구 ID

        Returns:
            관련 도구 리스트
        """
        result = self.supabase.rpc(
            'get_related_tools',
            {'tool_id': tool_id}
        ).execute()

        return [
            RelatedTool(
                id=row['id'],
                title=row['title'],
                category=row['category'],
                relation_type=row['relation_type']
            )
            for row in result.data
        ]

    def get_tool(self, tool_id: str) -> Optional[dict]:
        """
        특정 도구 상세 조회

        Args:
            tool_id: 도구 ID

        Returns:
            도구 상세 정보
        """
        result = self.supabase.table('thinking_tools').select(
            '*'
        ).eq('id', tool_id).single().execute()

        return result.data

    def get_by_category(self, category: str) -> list[dict]:
        """
        카테고리별 도구 조회

        Args:
            category: 카테고리 ID

        Returns:
            해당 카테고리의 도구 리스트
        """
        result = self.supabase.table('thinking_tools').select(
            'id, title, difficulty, time_required'
        ).eq('category', category).order('title').execute()

        return result.data

    def get_categories(self) -> list[dict]:
        """모든 카테고리 조회"""
        result = self.supabase.table('categories').select('*').execute()
        return result.data

    def get_clusters(self) -> list[dict]:
        """모든 클러스터 조회"""
        result = self.supabase.table('clusters').select('*').execute()
        return result.data

    def get_workflows(self) -> list[dict]:
        """모든 워크플로우 조회"""
        result = self.supabase.table('workflows').select('*').execute()
        return result.data


# CLI 테스트용
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python search_client.py <query>")
        print("Example: python search_client.py '문제의 근본 원인 분석'")
        sys.exit(1)

    query = " ".join(sys.argv[1:])

    try:
        client = SocraticSearchClient()
        results = client.search(query, limit=3)

        print(f"\n검색 결과: '{query}'\n")
        print("=" * 60)

        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result.title}")
            print(f"   카테고리: {result.category}")
            print(f"   난이도: {result.difficulty}")
            print(f"   유사도: {result.similarity:.2%}")
            print(f"   관련 도구: {', '.join(result.related_methods[:3])}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
