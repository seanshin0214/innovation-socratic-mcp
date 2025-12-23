# Thinking Tools Relationship Map

## 메타데이터 구조

각 파일은 YAML frontmatter에 다음 필드를 포함합니다:

```yaml
---
id: unique-identifier
title: Tool Name (한글명)
category: category_id
category_kr: 카테고리 한글명
difficulty: beginner/intermediate/advanced/expert
time_required: 소요시간
group_size: 적정 인원

related_methods:       # 직접 관련된 도구
  - 파일명

complementary_methods: # 보완적으로 함께 사용하면 좋은 도구
  - 파일명

keywords:              # 검색 키워드
  - 키워드

use_cases:             # 사용 사례
  - 사례

origin: 개발자/출처
---
```

## 카테고리 분류 (12개)

| ID | 한글명 | 도구 수 | 대표 도구 |
|----|--------|---------|-----------|
| question_inquiry | 질문/탐구 | 7 | Question Storming |
| creative_divergent | 창의적 발산 | 11 | Brainstorming |
| analysis_convergent | 분석/수렴 | 8 | SWOT Analysis |
| strategy_planning | 전략/계획 | 8 | Business Model Canvas |
| problem_solving | 문제해결 | 6 | Six Thinking Hats |
| innovation_design | 혁신/디자인 | 6 | Design Thinking |
| visualization | 시각화 | 5 | Mind Mapping |
| decision_making | 의사결정 | 3 | Decision Matrix |
| intuitive_creative | 직관적 사고 | 8 | Dreamscape |
| group_collaboration | 그룹/협업 | 3 | World Cafe |
| structured_thinking | 구조화 사고 | 6 | MECE |
| root_cause | 근본원인 분석 | 3 | Fishbone Diagram |

## 도구 클러스터 (10개)

### 1. 질문 기반 탐구
- **Core**: Question Storming
- **Members**: Kipling Method, Socratic Questioning, Phoenix Checklist, Starbursting

### 2. 창의적 역발상
- **Core**: Reverse Brainstorming
- **Members**: Worst Possible Idea, False Faces, Reframing

### 3. 브레인스토밍 계열
- **Core**: Brainstorming
- **Members**: SCAMPER, Brainwriting 635, Idea Box, Forced Connections

### 4. 비즈니스 캔버스
- **Core**: Business Model Canvas
- **Members**: Value Proposition Canvas, Lean Canvas, Jobs-to-be-Done

### 5. 근본원인 분석
- **Core**: Fishbone Diagram
- **Members**: Five Whys, Theory of Constraints, Causal Loop Diagrams

### 6. 전략 분석
- **Core**: SWOT Analysis
- **Members**: PESTLE, Stakeholder Mapping, Force Field Analysis

### 7. 성과 관리
- **Core**: OKR
- **Members**: KPI Metrics, Critical Success Factors, Balanced Scorecard

### 8. 시각화 도구
- **Core**: Mind Mapping
- **Members**: Concept Map, Lotus Blossom, Think Bubbles, Affinity Diagram

### 9. 직관적 창의
- **Core**: Dreamscape
- **Members**: Da Vinci Technique, Dali Technique, Three Bs, Chilling Out

### 10. 의사결정
- **Core**: Decision Matrix
- **Members**: Impact-Effort Matrix, PMI Analysis, Tug of War

## 추천 워크플로우

### 문제해결 워크플로우
```
Question Storming → Fishbone Diagram → Five Whys → Brainstorming → Decision Matrix
     (탐구)           (원인분석)        (근본원인)    (해결책)        (선택)
```

### 혁신 워크플로우
```
Design Thinking → JTBD → SCAMPER → Value Proposition → Pre-Mortem
    (공감)       (니즈)   (발상)      (가치설계)        (검증)
```

### 전략 수립 워크플로우
```
PESTLE → SWOT → Scenario Planning → Business Model Canvas → OKR
(외부)   (분석)    (미래시나리오)        (비즈니스모델)      (목표)
```

## 난이도별 분류

### Beginner (26개)
Quick Win - 15-30분 내 실행 가능, 사전 지식 불필요

### Intermediate (34개)
표준 도구 - 1-2시간, 기본 이해 필요

### Advanced (10개)
심화 도구 - 2시간 이상, 전문 지식 권장

### Expert (1개)
TRIZ - 전문 교육 필요

## 사용 방법

### 벡터 검색 시
1. `keywords` 필드로 의미 검색
2. `use_cases` 필드로 상황 매칭
3. `category` 필드로 유형 필터링

### 관련 도구 탐색 시
1. `related_methods`로 직접 관련 도구 확인
2. `complementary_methods`로 보완 도구 확인
3. `_index.json`의 `clusters`로 도구군 확인

### 워크플로우 구성 시
1. `_index.json`의 `workflows` 참조
2. `use_case_index`로 목적별 도구 선택
3. 난이도 고려하여 조합

