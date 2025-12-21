---
id: kpi-metrics
title: KPI & Metrics (핵심성과지표)
category: strategy_planning
category_kr: 전략/계획
difficulty: intermediate
time_required: 1-2시간
group_size: 2-10명

related_methods:
  - 41-OKR
  - 16-Critical-Success-Factors
  - 19-Balanced-Scorecard

complementary_methods:
  - 10-Impact-Effort-Matrix
  - 67-Decision-Matrix

keywords:
  - 지표
  - 측정
  - 성과
  - 대시보드
  - 모니터링

use_cases:
  - 성과 측정
  - 의사결정
  - 개선 추적
  - 보고

origin: 경영학, 품질관리
---
# KPI & Metrics (핵심성과지표)

## 개요
KPI(Key Performance Indicators)는 조직의 핵심 목표 달성 여부를 측정하는 정량적 지표입니다. "측정할 수 없으면 관리할 수 없다"는 피터 드러커의 철학을 기반으로 합니다.

## KPI vs Metrics

```
모든 KPI는 Metric이지만, 모든 Metric이 KPI는 아니다

Metrics (지표)
├── Vanity Metrics (허영 지표) - 보기 좋지만 의미 없음
├── Operational Metrics (운영 지표) - 일상 운영 추적
└── KPI (핵심성과지표) - 핵심 목표와 직결
```

## 좋은 KPI의 특성 (SMART)

- **S**pecific: 구체적
- **M**easurable: 측정 가능
- **A**chievable: 달성 가능
- **R**elevant: 관련성 있음
- **T**ime-bound: 시간 제한

## 영역별 핵심 KPI

### 재무 (Finance)

| KPI | 설명 | 공식 |
|-----|------|------|
| Revenue | 매출 | 총 판매액 |
| Gross Margin | 매출총이익률 | (매출-원가)/매출 × 100 |
| Net Profit Margin | 순이익률 | 순이익/매출 × 100 |
| EBITDA | 영업이익 | 영업이익 + 감가상각 |
| Cash Flow | 현금흐름 | 유입-유출 |

### 마케팅 (Marketing)

| KPI | 설명 | 공식 |
|-----|------|------|
| CAC | 고객획득비용 | 마케팅비용/신규고객수 |
| ROAS | 광고수익률 | 광고매출/광고비용 × 100 |
| CTR | 클릭률 | 클릭수/노출수 × 100 |
| CPM | 1000회 노출 비용 | (광고비/노출수) × 1000 |
| Brand Awareness | 브랜드 인지도 | 설문조사 |

### 고객 (Customer)

| KPI | 설명 | 공식 |
|-----|------|------|
| NPS | 순추천지수 | 추천자% - 비추천자% |
| CSAT | 고객만족도 | 만족고객/전체 × 100 |
| CES | 고객노력지수 | 평균 노력 점수 |
| Churn Rate | 이탈률 | 이탈고객/전체 × 100 |
| LTV | 고객생애가치 | 평균거래액 × 거래빈도 × 고객수명 |

### 제품/서비스 (Product)

| KPI | 설명 | 공식 |
|-----|------|------|
| DAU/MAU | 일/월 활성 사용자 | 활성 사용자 수 |
| Retention Rate | 리텐션 | 유지고객/시작고객 × 100 |
| Activation Rate | 활성화율 | 활성화유저/가입자 × 100 |
| Feature Adoption | 기능 채택률 | 기능사용자/전체 × 100 |
| Time to Value | 가치 도달 시간 | 첫 가치 경험까지 시간 |

### 운영 (Operations)

| KPI | 설명 | 공식 |
|-----|------|------|
| Uptime | 가동률 | 정상시간/전체시간 × 100 |
| Response Time | 응답 시간 | 평균 응답 시간 |
| Error Rate | 오류율 | 오류수/전체요청 × 100 |
| Throughput | 처리량 | 시간당 처리 건수 |
| MTTR | 평균복구시간 | 총복구시간/장애건수 |

### 인사 (HR)

| KPI | 설명 | 공식 |
|-----|------|------|
| Turnover Rate | 이직률 | 퇴사자/평균인원 × 100 |
| eNPS | 직원추천지수 | 추천자% - 비추천자% |
| Time to Hire | 채용 소요시간 | 평균 채용일수 |
| Training Hours | 교육시간 | 인당 평균 교육시간 |
| Engagement Score | 몰입도 | 설문조사 점수 |

## SaaS 핵심 지표

### Pirate Metrics (AARRR)
```
A - Acquisition (획득): 사용자가 어떻게 오는가?
A - Activation (활성화): 첫 경험이 좋은가?
R - Retention (유지): 다시 오는가?
R - Revenue (수익): 돈을 지불하는가?
R - Referral (추천): 다른 사람에게 추천하는가?
```

### SaaS 고유 지표

| KPI | 설명 | 건강 기준 |
|-----|------|----------|
| MRR | 월간반복매출 | 월 5-10% 성장 |
| ARR | 연간반복매출 | MRR × 12 |
| Churn Rate | 이탈률 | < 5% 월간 |
| Net Revenue Retention | 순매출유지율 | > 100% |
| LTV/CAC | 고객가치/획득비용 | > 3:1 |
| Payback Period | 회수기간 | < 12개월 |

## KPI 설계 프로세스

### 1단계: 전략 연결
```
비전/미션
    ↓
전략 목표
    ↓
핵심 성공 요인 (CSF)
    ↓
KPI 도출
```

### 2단계: KPI 정의서 작성

```markdown
## KPI 정의서 템플릿

**KPI 명칭**: 월간 활성 사용자 (MAU)
**정의**: 최근 30일 내 1회 이상 로그인한 순 사용자 수
**측정 공식**: COUNT(DISTINCT user_id WHERE last_login >= 30일전)
**데이터 소스**: 사용자 활동 로그 DB
**측정 주기**: 주간
**목표**: 100,000명
**담당자**: 그로스팀
**관련 OKR**: 고객 참여도 향상
```

### 3단계: 대시보드 구성
- 실시간 모니터링
- 트렌드 시각화
- 알림 설정
- 드릴다운 기능

## 대시보드 설계 원칙

### 계층 구조
```
Level 1: 경영진 대시보드 (5-7개 핵심 KPI)
Level 2: 팀 대시보드 (10-15개 운영 지표)
Level 3: 개인 대시보드 (상세 메트릭)
```

### 시각화 선택
| 목적 | 차트 유형 |
|------|----------|
| 트렌드 | 라인 차트 |
| 비교 | 바 차트 |
| 비율 | 파이/도넛 차트 |
| 분포 | 히스토그램 |
| 관계 | 산점도 |
| 현재 상태 | 게이지/숫자 |

## 흔한 실수

### Vanity Metrics 집착
- ❌ 총 가입자 수 (비활성 포함)
- ✅ 월간 활성 사용자 (MAU)

### 너무 많은 KPI
- ❌ 50개 KPI 모니터링
- ✅ 5-7개 핵심 KPI 집중

### 지표 조작 가능성
- ❌ "클릭 수" 만 측정 → 클릭 유도 남발
- ✅ "의미 있는 행동" 까지 추적

### 후행 지표만 측정
- ❌ 매출만 보고 (이미 늦음)
- ✅ 리드, 전환율 등 선행 지표 포함

## 분석 프레임워크

### Cohort Analysis (코호트 분석)
- 같은 특성의 그룹별 행동 비교
- 예: 1월 가입자 vs 2월 가입자 리텐션

### Funnel Analysis (퍼널 분석)
```
방문 (100%)
    ↓
가입 (30%)
    ↓
활성화 (15%)
    ↓
구독 (5%)
    ↓
추천 (1%)
```

### Segmentation (세그먼트 분석)
- 사용자 그룹별 지표 비교
- 예: 국가별, 디바이스별, 요금제별

## 도구

### BI 도구
- Tableau
- Power BI
- Looker
- Metabase

### 제품 분석
- Amplitude
- Mixpanel
- Google Analytics 4

### 대시보드
- Geckoboard
- Klipfolio
- Databox
