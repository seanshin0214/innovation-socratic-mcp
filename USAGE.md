# 사용 가이드 (Claude Desktop)

## 설치 완료 후 사용 방법

### 1. 기본 사용법

thinking-tools MCP가 설치되면 Claude가 자동으로 감지합니다.
**직접 트리거를 입력할 필요 없이** 자연스럽게 대화하세요!

```
사용자: 팀 생산성이 낮아요. 어떻게 개선할 수 있을까요?

Claude: [thinking-tools 자동 활성화]
🎯 문제 분석 완료
분류: 귀하의 문제는 '조직 개선'이 필요합니다.

📋 추천 방법론:
1. TUG-OF-WAR (Force-Field Analysis) - 장애요인 분석 (4단계)
2. SIX THINKING HATS - 다각적 관점 (6단계)
3. 5 WHYS - 근본 원인 분석 (5단계)

어떤 방법론을 사용하시겠습니까?

사용자: 3번 5 WHYS로 해주세요

Claude: [방법론: 5 WHYS - PERSPECTIVE]
질문 1/5: WHY 1: 왜 이것이 발생합니까?

사용자: 회의가 너무 많아서요

Claude: [방법론: 5 WHYS - PERSPECTIVE]
질문 2/5: WHY 2: 왜 그것이 그런 경우입니까?
...
```

### 2. 키워드로 자동 활성화

다음 키워드를 사용하면 Claude가 thinking-tools를 자동으로 활성화합니다:

- **한글**: 씽킹툴, 창의적, 혁신, 문제해결, 브레인스토밍, 전략, 아이디어
- **영어**: thinking tools, creative, innovation, brainstorming, strategy, idea
- **방법론**: SCAMPER, 5 Whys, Six Hats, TRIZ, Design Thinking 등

### 3. 사용 예시

#### 예시 1: 창의적 제품 개선
```
사용자: 기존 제품을 혁신적으로 개선하고 싶어요

Claude: [thinking-tools 활성화]
🎯 문제 분석 완료
분류: 귀하의 문제는 '제품 개선'이 필요합니다.

📋 추천 방법론:
1. SCAMPER - 7가지 혁신 기법 (7단계)
2. IDEA BOX - 조합 생성 (3단계)
3. SLICE AND DICE - 속성 분석 (3단계)

사용자: 1번으로 할게요

Claude: [방법론: SCAMPER - LINEAR]
질문 1/7: SUBSTITUTE: 무엇을 대체할 수 있습니까?
...
```

#### 예시 2: 전략적 의사결정
```
사용자: 하버드 DBA를 해야 할지 고민이에요. 씽킹툴로 분석해줘

Claude: [thinking-tools 자동 활성화]
🎯 문제 분석 완료
분류: 귀하의 문제는 '의사결정'이 필요합니다.

📋 추천 방법론:
1. SIX THINKING HATS - 다각적 관점 (6단계)
2. PMI (Plus, Minus, Interesting) - 장단점 분석 (3단계)
3. WISHFUL THINKING - 이상적 결과 (3단계)
...
```

#### 예시 3: 특정 방법론 직접 지정
```
사용자: SCAMPER 방법으로 우리 서비스를 분석해줘

Claude: [SCAMPER 방법론 직접 활성화]
🤖 방법론: SCAMPER

[방법론: SCAMPER - LINEAR]
질문 1/7: SUBSTITUTE: 무엇을 대체할 수 있습니까?
...
```

### 4. 36가지 사고 도구 카테고리

**📊 Linear (체계적 분석)**
- SCAMPER, 5 WHYS, PHOENIX, LOTUS BLOSSOM 등

**💡 Intuitive (직관적 사고)**
- BRUTETHINK, STONE SOUP, DREAMSCAPE, ANALOGIES 등

**🎭 Perspective (관점 전환)**
- SIX THINKING HATS, TRIZ, DESIGN THINKING, LATERAL THINKING 등

**👥 Feedback**
- MURDER BOARD, BRAINSTORMING

### 5. 세션 중 명령어

질문에 답변하는 중에:
- 일반 답변: 다음 질문이 자동으로 생성됩니다
- "종료" / "그만" / "done": 세션 종료 및 요약 받기

### 6. 작동 원리

1. **자동 감지**: Claude가 사용자 메시지에서 사고 도구가 필요한지 판단
2. **문제 분류**: AI가 문제 유형을 분석하고 최적의 방법론 3개 추천
3. **방법론 선택**: 사용자가 번호 선택 또는 Claude에게 추천 요청
4. **단계별 질문**: 선택된 방법론에 따라 한 번에 하나씩 질문 제공
5. **인사이트 생성**: 모든 답변 수집 후 요약 및 통찰 제공

### 7. 팁

- 자연스럽게 대화하세요 - "씽킹툴" 같은 특별한 명령어를 외울 필요 없습니다
- 문제를 구체적으로 설명할수록 더 적합한 방법론이 추천됩니다
- 답변은 상세할수록 좋습니다 - 더 깊은 통찰을 얻을 수 있습니다
- 중간에 다른 방법론으로 바꾸고 싶다면 새로운 세션을 시작하세요
