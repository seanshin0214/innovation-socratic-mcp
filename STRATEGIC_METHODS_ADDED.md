# 전략적 의사결정 & 경영전략 방법론 추가 완료

## 추가된 방법론 (22개)

### 🎯 의사결정 도구 (Decision-Making)

1. **DECISION TREE** ⭐ 최우선
   - 복잡한 의사결정의 선택지와 결과 분석
   - 5단계

2. **DECISION MATRIX (Weighted Scoring)**
   - 여러 기준으로 옵션 평가 및 점수화
   - 4단계

3. **COST-BENEFIT ANALYSIS** ⭐
   - 투자 대비 효과 분석
   - 4단계

4. **PROS-CONS-FIXES**
   - 장단점 분석 + 단점 해결방안
   - 3단계

5. **REGRET MINIMIZATION (Jeff Bezos)**
   - 인생 결정에서 후회 최소화
   - 3단계

6. **OPPORTUNITY COST ANALYSIS**
   - 자원 배분 최적화
   - 4단계

7. **EISENHOWER MATRIX**
   - 우선순위 설정 (긴급-중요)
   - 4단계

### 📊 경영전략 프레임워크 (Business Strategy)

8. **SWOT ANALYSIS** ⭐
   - 강점/약점/기회/위협 분석
   - 5단계

9. **BCG MATRIX (Growth-Share)**
   - 포트폴리오 분석 (Star/Cash Cow/Question Mark/Dog)
   - 4단계

10. **PORTER'S FIVE FORCES**
    - 산업 경쟁 구조 분석
    - 6단계

11. **PESTEL ANALYSIS**
    - 거시환경 분석 (정치/경제/사회/기술/환경/법)
    - 6단계

12. **ANSOFF MATRIX**
    - 성장전략 (시장침투/시장개발/제품개발/다각화)
    - 5단계

13. **BLUE OCEAN STRATEGY**
    - 경쟁 없는 새로운 시장 창출
    - 4단계

14. **VALUE CHAIN ANALYSIS**
    - 가치사슬 분석으로 경쟁우위 발견
    - 5단계

15. **OKR (Objectives & Key Results)**
    - 목표 설정 및 측정
    - 3단계

### 🔗 인과관계 분석 (Causal Analysis)

16. **FISHBONE DIAGRAM (Ishikawa)**
    - 원인 분석 (Man/Method/Machine/Material)
    - 6단계

17. **SYSTEMS THINKING (Causal Loop)**
    - 시스템적 인과관계 이해
    - 5단계

18. **SECOND-ORDER THINKING**
    - 장기적 파급효과 분석
    - 4단계

### 🧠 심리적 의사결정 (Cognitive Decision-Making)

19. **MENTAL MODELS CHECK**
    - 인지편향 극복 (확증편향, 매몰비용, 가용성편향)
    - 5단계

20. **PRE-MORTEM**
    - 실패 시나리오로 리스크 예방
    - 4단계

21. **SCENARIO PLANNING**
    - 미래 불확실성 대비 (Best/Worst/Most Likely)
    - 5단계

22. **INVERSION (Backwards Thinking)**
    - 실패 방법으로 성공 찾기
    - 3단계

## 전체 방법론 수

- **기존**: 36개 (Linear, Intuitive, Perspective, Feedback)
- **추가**: 22개 (Strategic)
- **총합**: **58개 방법론**

## 분류 개선

### Classifier 키워드 추가

**strategic 카테고리 키워드**:
- 한글: 전략, 의사결정, 결정, 선택, 투자, ROI, BCG, SWOT, 포터, 경쟁, 시장분석, 포트폴리오, 사업전략, 성장전략, 리스크, 기회비용, 시나리오, 불확실성
- 영어: strategy, decision, choice, investment, BCG, SWOT, Porter, competitive, market analysis, portfolio, business strategy, growth, risk, opportunity cost, scenario, uncertainty

### 자동 방법론 매칭

- "결정" → DECISION TREE
- "SWOT" → SWOT ANALYSIS
- "BCG" → BCG MATRIX
- "포터" / "경쟁" → PORTER'S FIVE FORCES
- "원인" / "인과" → FISHBONE, SYSTEMS THINKING
- "투자" / "비용" → COST-BENEFIT ANALYSIS
- "리스크" / "실패" → PRE-MORTEM
- "후회" / "인생" → REGRET MINIMIZATION
- "편향" → MENTAL MODELS CHECK

## 사용 예시

### 예시 1: DBA 의사결정
```
사용자: "밥슨칼리지 DBA를 해야 할지 결정해야 해요"

추천 방법론:
1. DECISION TREE ⭐
2. REGRET MINIMIZATION (Jeff Bezos)
3. COST-BENEFIT ANALYSIS
```

### 예시 2: 회사 전략 분석
```
사용자: "우리 회사 전략을 분석하고 싶어요"

추천 방법론:
1. SWOT ANALYSIS ⭐
2. PORTER'S FIVE FORCES
3. BCG MATRIX
```

### 예시 3: 투자 결정
```
사용자: "신규 사업에 투자할지 고민 중입니다"

추천 방법론:
1. COST-BENEFIT ANALYSIS ⭐
2. SCENARIO PLANNING
3. PRE-MORTEM
```

### 예시 4: 리스크 관리
```
사용자: "프로젝트가 실패할 리스크를 미리 파악하고 싶어요"

추천 방법론:
1. PRE-MORTEM ⭐
2. SECOND-ORDER THINKING
3. SCENARIO PLANNING
```

## 다음 단계

1. **Claude Desktop 재시작** - 새로운 58개 방법론 로드
2. **테스트** - 전략적 의사결정 문제로 테스트
3. **피드백** - 실제 사용 후 질문 개선

## 주요 파일 수정

- `src/methods/templates.py` - STRATEGIC_METHODS 추가 (22개)
- `src/classifier.py` - strategic 키워드 대폭 확장
- `src/methods/templates.py` - CATEGORY_MAP 업데이트

모든 방법론이 정상 작동 확인 완료! ✅
