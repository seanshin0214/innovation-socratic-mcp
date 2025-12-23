# Socratic Thinking MCP - Knowledge Base

**74개 사고도구(Thinking Tools) RAG 지식 베이스**

Last Updated: 2024-12-22

---

## 개요

이 폴더는 RAG(Retrieval-Augmented Generation) 시스템을 위한 74개의 사고도구 지식 파일을 포함합니다.
모든 파일에 YAML frontmatter 메타데이터가 적용되어 있으며, 파일 간 관계 정보를 통해 연관된 도구를 함께 검색할 수 있습니다.

---

## 메타데이터 구조

각 파일은 다음 YAML frontmatter를 포함합니다:

```yaml
---
id: unique-identifier
title: 도구명 (한글명)
category: category_id
category_kr: 카테고리 한글
difficulty: beginner/intermediate/advanced/expert
time_required: 소요시간
group_size: 적정 인원

related_methods:       # 직접 관련 도구 (함께 불러오기)
  - 04-Socratic-Questioning

complementary_methods: # 보완 도구
  - 49-Six-Thinking-Hats

keywords:              # 벡터 검색용 키워드
use_cases:             # 사용 사례
origin: 개발자/출처
---
```

---

## 12개 카테고리

| 카테고리 | 한글명 | 도구 수 | 대표 도구 |
|----------|--------|---------|-----------|
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

---

## 10개 도구 클러스터

| 클러스터 | Core 도구 | 관련 도구 |
|----------|-----------|-----------|
| 질문 기반 탐구 | Question Storming | Kipling, Socratic, Phoenix, Starbursting |
| 창의적 역발상 | Reverse Brainstorming | Worst Idea, False Faces, Reframing |
| 브레인스토밍 계열 | Brainstorming | SCAMPER, Brainwriting, Idea Box, Forced Connections |
| 비즈니스 캔버스 | BMC | VPC, Lean Canvas, JTBD |
| 근본원인 분석 | Fishbone | Five Whys, TOC, Causal Loop |
| 전략 분석 | SWOT | PESTLE, Stakeholder Mapping, Force Field |
| 성과 관리 | OKR | KPI, CSF, Balanced Scorecard |
| 시각화 도구 | Mind Map | Concept Map, Lotus Blossom, Think Bubbles |
| 직관적 창의 | Dreamscape | Da Vinci, Dali, Three Bs |
| 의사결정 | Decision Matrix | Impact-Effort, PMI, Tug of War |

---

## 추천 워크플로우

### 문제해결
```
Question Storming -> Fishbone -> Five Whys -> Brainstorming -> Decision Matrix
```

### 혁신
```
Design Thinking -> JTBD -> SCAMPER -> Value Proposition -> Pre-Mortem
```

### 전략 수립
```
PESTLE -> SWOT -> Scenario Planning -> BMC -> OKR
```

---

## 인덱스 파일

| 파일 | 용도 |
|------|------|
| _index.json | 카테고리, 클러스터, 워크플로우 JSON 인덱스 |
| _RELATIONSHIP_MAP.md | 관계 구조 상세 문서 |
| _metadata_generator.py | 메타데이터 자동 생성 스크립트 |

---

## 난이도별 분류

- **Beginner** (26개): 15-30분, 사전지식 불필요
- **Intermediate** (34개): 1-2시간, 기본 이해 필요
- **Advanced** (10개): 2시간+, 전문 지식 권장
- **Expert** (1개): TRIZ - 전문 교육 필요

---

## 파일 목록 (74개)

### 01-20
01-Question-Storming, 02-Kipling-Method, 03-Appreciative-Inquiry, 04-Socratic-Questioning, 05-Jobs-To-Be-Done, 06-Liberating-Structures-1-2-4-All, 07-Assumption-Testing, 08-Thought-Experiments, 09-Cynefin-Framework, 10-Impact-Effort-Matrix, 11-Business-Model-Canvas, 12-Value-Proposition-Canvas, 13-Lean-Canvas, 14-Theory-of-Constraints-TOC, 15-Causal-Loop-Diagrams, 16-Critical-Success-Factors, 17-Stakeholder-Mapping, 18-Worst-Possible-Idea, 19-Balanced-Scorecard, 20-TRIZ-Contradiction-Matrix

### 21-40
21-False-Faces-Reversal, 22-Slice-and-Dice, 23-Cherry-Split, 24-Think-Bubbles, 25-SCAMPER, 26-Tug-of-War, 27-Idea-Box, 28-Lotus-Blossom, 29-Phoenix-Checklist, 30-BruteThink, 31-Chilling-Out, 32-Blue-Roses, 33-Three-Bs, 34-Rattlesnakes-and-Roses, 35-Stone-Soup, 36-Dreamscape, 37-Da-Vinci-Technique, 38-Dali-Technique, 39-Not-Kansas, 40-Murder-Board

### 41-60
41-OKR, 42-Agile-Framework, 43-KPI-Metrics, 44-Design-Thinking, 45-Jobs-to-be-Done, 46-Value-Proposition-Canvas, 47-Lean-Canvas, 48-Pre-Mortem, 49-Six-Thinking-Hats, 50-Fishbone-Diagram, 51-Five-Whys, 52-SWOT-Analysis, 53-Force-Field-Analysis, 54-Mind-Mapping, 55-PMI-Analysis, 56-Reverse-Brainstorming, 57-Starbursting, 58-Brainwriting-635, 59-Affinity-Diagram, 60-Morphological-Analysis

### 61-74
61-Synectics, 62-PESTLE-Analysis, 63-World-Cafe, 64-Thinking-Tools-Guide, 65-Multi-Perspective-Questioning, 66-Questions-Tools-Integration-Guide, 67-Decision-Matrix, 68-Forced-Connections, 69-MECE, 70-Scenario-Planning, 71-Reframing, 72-Concept-Map, 73-Brainstorming, 74-Fishbone-Diagram

---

## RAG 활용

### 벡터 검색
- keywords 필드로 의미 검색
- use_cases 필드로 상황 매칭

### 관계 기반 검색
- related_methods로 관련 도구 함께 불러오기
- complementary_methods로 보완 도구 추천
- _index.json의 clusters로 도구군 검색

### Use Case 기반 검색
- problem_definition: 문제 정의 도구
- root_cause_analysis: 근본원인 분석 도구
- idea_generation: 아이디어 생성 도구
- strategic_planning: 전략 수립 도구
- decision_making: 의사결정 도구
- team_collaboration: 팀 협업 도구
- innovation: 혁신 도구
- risk_assessment: 리스크 평가 도구
- goal_setting: 목표 설정 도구
