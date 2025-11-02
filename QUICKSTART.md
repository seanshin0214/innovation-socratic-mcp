# 🚀 빠른 시작 가이드

## 설치 및 실행

```bash
# 1. 디렉토리 이동
cd thinking-tools-mcp

# 2. 테스트 실행
python test_mcp.py

# 3. 대화형 데모
python test_mcp.py interactive

# 4. 모든 방법론 확인
python test_mcp.py all
```

## 사용 예시

### 예시 1: 팀 생산성 문제

```
사용자: "팀 생산성이 낮아요 /think"

MCP:
🎯 문제 분석 완료
분류: 귀하의 문제는 '조직 개선'이 필요합니다.

📋 추천 방법론:
1. TUG-OF-WAR (Force-Field Analysis) - 장애요인 분석 (4단계)
2. SIX THINKING HATS - 다각적 관점 (6단계)
3. 5 WHYS - 근본 원인 분석 (5단계)

방법 선택: /1, /2, /3 또는 /auto

사용자: "/3"

MCP:
[방법론: 5 WHYS - PERSPECTIVE]
질문 1/5: WHY 1: 왜 이것이 발생합니까?

사용자: "회의가 너무 많아서요"

MCP:
[방법론: 5 WHYS - PERSPECTIVE]
질문 2/5: WHY 2: 왜 그것이 그런 경우입니까?

사용자: "결정을 내리지 못해서요"

MCP:
[방법론: 5 WHYS - PERSPECTIVE]
질문 3/5: WHY 3: 왜 그것이 발생합니까?

사용자: "의사결정 권한이 불명확해서요"

MCP:
[방법론: 5 WHYS - PERSPECTIVE]
질문 4/5: WHY 4: 왜 그것이 근본적인 이유입니까?

사용자: "역할과 책임이 정의되지 않아서요"

MCP:
[방법론: 5 WHYS - PERSPECTIVE]
질문 5/5: WHY 5: 근본 원인은 무엇입니까?

✅ 마지막 질문입니다.

사용자: "조직 재구조화 이후 업데이트하지 않았어요"

MCP:
✅ 세션 완료

📌 문제: 팀 생산성이 낮아요
🔧 사용 방법: 5 WHYS
📊 답변: 5/5

💡 인사이트:
근본 원인: 조직 재구조화 이후 업데이트하지 않았어요

다음 단계:
- 다른 방법론 시도: /method:scamper
- 새 문제 분석: /think [문제]
- 종료: /done
```

### 예시 2: 제품 혁신

```
사용자: "기존 제품을 개선하고 싶어요 /think"

MCP:
🎯 문제 분석 완료
분류: 귀하의 문제는 '제품 개선'이 필요합니다.

📋 추천 방법론:
1. SCAMPER - 7가지 혁신 기법 (7단계)
2. IDEA BOX (Morphological Analysis) - 조합 생성 (3단계)
3. SLICE AND DICE (Attribute Listing) - 속성 분석 (3단계)

방법 선택: /1, /2, /3 또는 /auto

사용자: "/auto"

MCP:
🤖 AI 추천: SCAMPER

[방법론: SCAMPER - LINEAR]
질문 1/7: SUBSTITUTE: 무엇을 대체할 수 있습니까?

사용자: "플라스틱 재질을 친환경 소재로 대체"

MCP:
[방법론: SCAMPER - LINEAR]
질문 2/7: COMBINE: 무엇과 결합할 수 있습니까?

사용자: "스마트폰 앱과 연동 기능 추가"

...
```

### 예시 3: 창의적 브레인스토밍

```
사용자: "완전히 새로운 아이디어가 필요해요 /think"

MCP:
🎯 문제 분석 완료
분류: 귀하의 문제는 '창의적 사고'가 필요합니다.

📋 추천 방법론:
1. BRUTETHINK (Random Stimulation) - 랜덤 자극 (3단계)
2. STONE SOUP (Fantasy Questions) - 상상 질문 (5단계)
3. ANALOGIES - 유추 사고 (3단계)

방법 선택: /1, /2, /3 또는 /auto

사용자: "/2"

MCP:
[방법론: STONE SOUP (Fantasy Questions) - INTUITIVE]
질문 1/5: 만약 중력이 없다면?

사용자: "제품이 공중에 떠다니면 어떤 새로운 용도가 있을까요..."

MCP:
[방법론: STONE SOUP (Fantasy Questions) - INTUITIVE]
질문 2/5: 만약 고객이 마음을 읽을 수 있다면?

...
```

## 명령어 치트시트

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `/think [문제]` | 문제 분석 시작 | `/think 매출이 떨어져요` |
| `/innovate [문제]` | 혁신 도구 시작 | `/innovate 신제품 아이디어` |
| `/1`, `/2`, `/3` | 방법론 선택 | `/1` |
| `/auto` | AI 자동 선택 | `/auto` |
| `/method:NAME` | 특정 방법론 | `/method:scamper` |
| `/done` | 세션 종료 | `/done` |
| `/help` | 도움말 | `/help` |

## 방법론 카테고리

### 📊 Linear (체계적 분석)
- **SCAMPER**: 제품 혁신 7단계
- **5 WHYS**: 근본 원인 분석
- **PHOENIX**: 포괄적 질문 체크리스트
- **LOTUS BLOSSOM**: 아이디어 확장

### 💡 Intuitive (직관적 사고)
- **BRUTETHINK**: 랜덤 단어 자극
- **STONE SOUP**: 상상 질문
- **DREAMSCAPE**: 꿈 분석
- **ANALOGIES**: 유추 사고

### 🎭 Perspective (관점 전환)
- **SIX THINKING HATS**: 6가지 관점
- **TRIZ**: 발명적 문제 해결
- **DESIGN THINKING**: 사용자 중심
- **LATERAL THINKING**: 측면 사고

### 👥 Feedback
- **MURDER BOARD**: 정직한 피드백
- **BRAINSTORMING**: 그룹 아이디어

## 트러블슈팅

### 문제: 잠수함 모드에서 벗어나지 않음
**해결**: `/think [문제]` 또는 `/innovate [문제]`로 활성화

### 문제: 방법론을 모르겠음
**해결**: `/auto`로 AI에게 자동 선택 맡기기

### 문제: 세션 중단하고 싶음
**해결**: `/done`으로 언제든지 종료 가능

## 프로그래매틱 사용

```python
from src.classifier import classifier
from src.question_engine import engine
from src.session import session_manager

# 1. 문제 분류
result = classifier.classify("팀 생산성이 낮음")

# 2. 세션 시작
session = session_manager.create_session(
    user_id="user123",
    problem="팀 생산성이 낮음",
    category=result["category"],
    method_id="five_whys",
    method_name="5 WHYS",
    total_steps=5
)

# 3. 질문 생성
question = engine.generate_question("five_whys", 0)
print(question["question"])

# 4. 답변 추가
session_manager.add_answer("회의가 많아서")

# 5. 다음 질문
next_question = engine.generate_question("five_whys", 1)
```

## 다음 단계

1. **PDF 업로드**: RAG 기능으로 문서 기반 분석
2. **커스텀 방법론**: 자신만의 질문 템플릿 추가
3. **팀 협업**: 세션 공유 및 협업 기능

---

**Happy Thinking! 🧠✨**
