# 📦 Knowledge Setup Guide

## Option 1: Claude Desktop (Local) - 추천

Claude Desktop은 **로컬 knowledge 폴더 + ChromaDB**를 사용합니다. 외부 서비스 불필요!

### 설치 방법

```bash
git clone https://github.com/seanshin0214/innovation-socratic-mcp.git
cd innovation-socratic-mcp
pip install -r requirements.txt
```

### claude_desktop_config.json 설정

```json
{
  "mcpServers": {
    "innovation-socratic": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "C:\Users\YourName\Documents\innovation-socratic-mcp",
      "env": {
        "PYTHONPATH": "C:\Users\YourName\Documents\innovation-socratic-mcp"
      }
    }
  }
}
```

**특징:**
- ✅ 지식 파일이 `knowledge/` 폴더에 포함됨
- ✅ ChromaDB 벡터 DB가 로컬에서 자동 생성
- ✅ Supabase 불필요
- ✅ 인터넷 연결 없이 사용 가능

---

## Option 2: ChatGPT GPT (Supabase) - 24시간 접근

GPT Actions를 사용하려면 **원격 지식 베이스**가 필요합니다.

### 설정 방법

1. **Supabase 프로젝트 생성**: [supabase.com](https://supabase.com)
2. **스키마 실행**: `supabase/schema.sql`
3. **지식 업로드**: `supabase/upload_knowledge.py`
4. **GPT Action 설정**: Supabase Edge Function URL 사용

### 환경변수 설정

```bash
export SUPABASE_URL="https://your-project.supabase.co"
export SUPABASE_KEY="your-service-role-key"
export OPENAI_API_KEY="sk-..."
python supabase/upload_knowledge.py
```

자세한 설정은 `supabase/README.md` 참고.

**특징:**
- ✅ 24시간 접근 가능
- ✅ 컴퓨터 꺼도 작동
- ⚠️ Supabase + OpenAI API 키 필요
- ⚠️ 월 비용 ~$0-27 (사용량에 따라)

---

## Option 3: ChatGPT GPT (ngrok) - 대안

로컬에서 ngrok으로 실행하는 방법:

```bash
# 1. 로컬 서버 실행
python run_server.py

# 2. ngrok으로 노출
ngrok http 8000

# 3. GPT Action에 ngrok URL 사용
```

**특징:**
- ⚠️ 컴퓨터가 켜져 있어야 함
- ⚠️ ngrok 무료 버전은 URL 변경됨
- ✅ Supabase 비용 없음

---

## 비교표

| 플랫폼 | 지식 저장 | 벡터 DB | 비용 | 24시간 |
|--------|----------|---------|------|--------|
| **Claude Desktop** | 로컬 `knowledge/` | ChromaDB | 무료 | ❌ |
| **GPT (Supabase)** | Supabase | pgvector | $0-27/월 | ✅ |
| **GPT (ngrok)** | 로컬 | ChromaDB | 무료 | ❌ |

---

## 자신만의 지식 추가하기

`knowledge/` 폴더에 마크다운 파일 추가:

```markdown
---
id: my-custom-method
title: My Custom Method (나만의 방법)
category: strategy_planning
difficulty: intermediate
---

## 개요
...

## 질문 순서
1. 첫 번째 질문?
2. 두 번째 질문?
...
```

자세한 형식은 `knowledge/_지식-추가-방법.md` 참고.
