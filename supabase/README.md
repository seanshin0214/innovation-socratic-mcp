# Supabase Integration Guide

**Socratic Thinking MCP - Supabase + pgvector 백엔드**

Supabase를 사용하면 사용자들이 로컬 파일 없이도 74개 사고도구 지식에 접근할 수 있습니다.

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                      User's Claude Code                      │
│                              ↓                               │
│                   Socratic Thinking MCP                      │
│                              ↓                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │              HybridRAGEngine                            │ │
│  │   ┌──────────────────┬──────────────────────────┐      │ │
│  │   │  Supabase 가능?  │     Yes → SupabaseRAG    │      │ │
│  │   │                  │     No  → ChromaDB       │      │ │
│  │   └──────────────────┴──────────────────────────┘      │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ↓
              ┌───────────────────────────────┐
              │      Supabase (PostgreSQL)     │
              │  ┌─────────────────────────┐  │
              │  │      thinking_tools     │  │
              │  │   - 74 documents        │  │
              │  │   - vector embeddings   │  │
              │  │   - metadata (JSON)     │  │
              │  └─────────────────────────┘  │
              │  ┌─────────────────────────┐  │
              │  │   pgvector extension    │  │
              │  │   - IVFFlat index       │  │
              │  │   - cosine similarity   │  │
              │  └─────────────────────────┘  │
              └───────────────────────────────┘
```

---

## 1. Supabase 프로젝트 설정

### 1.1 프로젝트 생성
1. [Supabase](https://supabase.com)에서 새 프로젝트 생성
2. Region: Seoul (ap-northeast-2) 권장
3. 프로젝트 URL과 API 키 저장

### 1.2 pgvector 활성화
Supabase Dashboard → SQL Editor에서:
```sql
create extension if not exists vector;
```

### 1.3 스키마 실행
```sql
-- supabase/schema.sql 파일 전체 실행
```

또는 터미널에서:
```bash
# Supabase CLI 사용
supabase db push --db-url postgresql://postgres:[password]@[host]:5432/postgres < supabase/schema.sql
```

---

## 2. 지식 업로드

### 2.1 환경변수 설정
```bash
# .env 파일 또는 직접 설정
export SUPABASE_URL="https://xxxxx.supabase.co"
export SUPABASE_KEY="eyJhbGci..."  # service_role 키 (업로드용)
export OPENAI_API_KEY="sk-..."
```

### 2.2 업로드 실행
```bash
# 모든 파일 업로드
python supabase/upload_knowledge.py

# 특정 파일만 업로드
python supabase/upload_knowledge.py --file 01-Question-Storming.md

# 테스트 (실제 업로드 안함)
python supabase/upload_knowledge.py --dry-run
```

### 2.3 업로드 확인
Supabase Dashboard → Table Editor → thinking_tools에서 확인

---

## 3. 사용자 설정 (Claude Desktop)

### 3.1 Supabase 연결 설정

`claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "innovation-socratic": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "C:\\Users\\YourName\\Documents\\innovation-socratic-mcp",
      "env": {
        "PYTHONPATH": "C:\\Users\\YourName\\Documents\\innovation-socratic-mcp",
        "SUPABASE_URL": "https://xxxxx.supabase.co",
        "SUPABASE_KEY": "eyJhbGci...",
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

**참고**: 사용자는 `anon` 키를 사용 (읽기 전용)

### 3.2 로컬 모드 (Supabase 없이)

환경변수를 설정하지 않으면 자동으로 로컬 ChromaDB 사용:
```json
{
  "mcpServers": {
    "innovation-socratic": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "C:\\Users\\YourName\\Documents\\innovation-socratic-mcp"
    }
  }
}
```

---

## 4. API 함수

### 4.1 search_thinking_tools
하이브리드 시맨틱 검색

```sql
select * from search_thinking_tools(
    query_embedding := '[0.1, 0.2, ...]'::vector,
    match_threshold := 0.7,
    match_count := 5,
    filter_category := 'creative_divergent',
    filter_difficulty := null
);
```

### 4.2 get_related_tools
관련 도구 조회

```sql
select * from get_related_tools('question-storming');
```

### 4.3 search_by_use_case
Use case 기반 검색

```sql
select * from search_by_use_case('root_cause_analysis');
```

---

## 5. 보안 설정

### 5.1 Row Level Security (RLS)
```sql
-- 읽기 전용 정책 (anon 키용)
alter table thinking_tools enable row level security;

create policy "Public read access"
on thinking_tools for select
to anon
using (true);
```

### 5.2 키 권한
| 키 | 용도 | 권한 |
|---|---|---|
| `anon` | 사용자용 | 읽기만 |
| `service_role` | 관리자용 | 읽기/쓰기 |

---

## 6. 비용 예측

### Supabase (Free Tier)
- 500MB 데이터베이스 ✓
- 2GB 대역폭/월 ✓
- 74개 문서 (약 5MB) → 충분

### OpenAI Embeddings
- text-embedding-3-small: $0.02/1M tokens
- 업로드: 74개 × 2000 tokens ≈ $0.003
- 검색: 쿼리당 약 100 tokens ≈ $0.000002

**예상 월 비용**: ~$1 미만 (일반 사용량)

---

## 7. 문제 해결

### Supabase 연결 실패
```
Supabase init error: ...
```
→ URL과 키 확인, 네트워크 연결 확인

### 임베딩 생성 실패
```
OpenAI API error: ...
```
→ OpenAI API 키 확인, 잔액 확인

### 검색 결과 없음
→ `match_threshold` 값 낮추기 (0.7 → 0.5)

---

## 8. 파일 구조

```
supabase/
├── README.md           # 이 문서
├── schema.sql          # 테이블 & 함수 정의
├── upload_knowledge.py # 지식 업로드 스크립트
└── search_client.py    # Python 검색 클라이언트

src/
├── rag.py              # 로컬 ChromaDB RAG
└── rag_supabase.py     # Supabase + Hybrid RAG
```

---

## 9. 지식 업데이트

새 도구 추가 또는 수정 시:
```bash
# 1. knowledge/ 폴더에 마크다운 추가/수정
# 2. 메타데이터 생성
python knowledge/_metadata_generator.py

# 3. Supabase에 업로드
python supabase/upload_knowledge.py --file 새파일.md
```

---

**문의**: [Issues](https://github.com/seanshin0214/innovation-socratic-mcp/issues)
