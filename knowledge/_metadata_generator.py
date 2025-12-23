"""
Thinking Tools Metadata Generator
지식 파일에 YAML frontmatter 메타데이터 자동 추가
"""

import os
import re
from pathlib import Path

# 카테고리 정의
CATEGORIES = {
    "question_inquiry": "질문/탐구",
    "creative_divergent": "창의적 발산",
    "analysis_convergent": "분석/수렴",
    "strategy_planning": "전략/계획",
    "problem_solving": "문제해결",
    "innovation_design": "혁신/디자인",
    "visualization": "시각화",
    "decision_making": "의사결정",
    "intuitive_creative": "직관적 사고",
    "group_collaboration": "그룹/협업",
    "structured_thinking": "구조화 사고",
    "root_cause": "근본원인 분석"
}

# 파일별 메타데이터 정의
METADATA = {
    "01-Question-Storming": {
        "id": "question-storming",
        "title": "Question Storming (질문 폭풍)",
        "category": "question_inquiry",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "4-8명",
        "related": ["04-Socratic-Questioning", "57-Starbursting", "73-Brainstorming", "02-Kipling-Method"],
        "complementary": ["49-Six-Thinking-Hats", "71-Reframing"],
        "keywords": ["질문", "발산", "탐색", "문제정의", "브레인스토밍"],
        "use_cases": ["문제 정의", "탐색 단계", "혁신 워크샵", "전략 수립"],
        "origin": "Hal Gregersen, MIT"
    },
    "02-Kipling-Method": {
        "id": "kipling-method",
        "title": "Kipling Method (5W1H)",
        "category": "question_inquiry",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-10명",
        "related": ["01-Question-Storming", "04-Socratic-Questioning", "57-Starbursting"],
        "complementary": ["51-Five-Whys", "74-Fishbone-Diagram"],
        "keywords": ["5W1H", "Who", "What", "When", "Where", "Why", "How"],
        "use_cases": ["문제 분석", "요구사항 정의", "기사 작성", "조사"],
        "origin": "Rudyard Kipling"
    },
    "03-Appreciative-Inquiry": {
        "id": "appreciative-inquiry",
        "title": "Appreciative Inquiry (긍정 탐구)",
        "category": "question_inquiry",
        "difficulty": "intermediate",
        "time_required": "2-4시간",
        "group_size": "5-30명",
        "related": ["04-Socratic-Questioning", "35-Stone-Soup", "71-Reframing"],
        "complementary": ["44-Design-Thinking", "63-World-Cafe"],
        "keywords": ["긍정", "강점", "4D", "Discovery", "Dream", "Design", "Destiny"],
        "use_cases": ["조직 개발", "팀 빌딩", "변화 관리", "비전 수립"],
        "origin": "David Cooperrider"
    },
    "04-Socratic-Questioning": {
        "id": "socratic-questioning",
        "title": "Socratic Questioning (소크라테스식 질문)",
        "category": "question_inquiry",
        "difficulty": "advanced",
        "time_required": "30-60분",
        "group_size": "2-6명",
        "related": ["01-Question-Storming", "51-Five-Whys", "02-Kipling-Method"],
        "complementary": ["07-Assumption-Testing", "71-Reframing"],
        "keywords": ["비판적 사고", "논리", "가정 검증", "깊은 질문"],
        "use_cases": ["비판적 분석", "교육", "코칭", "논증 검토"],
        "origin": "Socrates"
    },
    "05-Jobs-To-Be-Done": {
        "id": "jobs-to-be-done",
        "title": "Jobs-To-Be-Done (JTBD)",
        "category": "innovation_design",
        "difficulty": "intermediate",
        "time_required": "1-3시간",
        "group_size": "3-8명",
        "related": ["44-Design-Thinking", "12-Value-Proposition-Canvas", "11-Business-Model-Canvas"],
        "complementary": ["17-Stakeholder-Mapping", "52-SWOT-Analysis"],
        "keywords": ["고객", "니즈", "Job", "Outcome", "혁신"],
        "use_cases": ["제품 개발", "시장 분석", "고객 이해", "혁신 전략"],
        "origin": "Clayton Christensen"
    },
    "06-Liberating-Structures-1-2-4-All": {
        "id": "liberating-structures",
        "title": "Liberating Structures 1-2-4-All",
        "category": "group_collaboration",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "4-100명",
        "related": ["63-World-Cafe", "58-Brainwriting-635", "73-Brainstorming"],
        "complementary": ["59-Affinity-Diagram", "49-Six-Thinking-Hats"],
        "keywords": ["참여", "구조화 토론", "민주적", "포용"],
        "use_cases": ["대규모 회의", "팀 참여", "아이디어 수렴", "합의 도출"],
        "origin": "Keith McCandless, Henri Lipmanowicz"
    },
    "07-Assumption-Testing": {
        "id": "assumption-testing",
        "title": "Assumption Testing (가정 검증)",
        "category": "problem_solving",
        "difficulty": "intermediate",
        "time_required": "30-90분",
        "group_size": "2-8명",
        "related": ["04-Socratic-Questioning", "48-Pre-Mortem", "40-Murder-Board"],
        "complementary": ["51-Five-Whys", "52-SWOT-Analysis"],
        "keywords": ["가정", "검증", "리스크", "비판적 사고"],
        "use_cases": ["프로젝트 계획", "신사업", "투자 결정", "전략 검토"],
        "origin": "Lean Startup, Scientific Method"
    },
    "08-Thought-Experiments": {
        "id": "thought-experiments",
        "title": "Thought Experiments (사고 실험)",
        "category": "intuitive_creative",
        "difficulty": "advanced",
        "time_required": "30-60분",
        "group_size": "1-6명",
        "related": ["71-Reframing", "35-Stone-Soup", "36-Dreamscape"],
        "complementary": ["70-Scenario-Planning", "49-Six-Thinking-Hats"],
        "keywords": ["상상", "가설", "what-if", "철학적"],
        "use_cases": ["이론 검토", "윤리적 판단", "혁신", "복잡한 문제"],
        "origin": "Albert Einstein, Philosophy"
    },
    "09-Cynefin-Framework": {
        "id": "cynefin-framework",
        "title": "Cynefin Framework (키네빈)",
        "category": "problem_solving",
        "difficulty": "advanced",
        "time_required": "30-60분",
        "group_size": "3-10명",
        "related": ["14-Theory-of-Constraints-TOC", "15-Causal-Loop-Diagrams", "70-Scenario-Planning"],
        "complementary": ["52-SWOT-Analysis", "67-Decision-Matrix"],
        "keywords": ["복잡성", "의사결정", "Simple", "Complicated", "Complex", "Chaotic"],
        "use_cases": ["문제 유형 진단", "전략 선택", "조직 관리", "위기 대응"],
        "origin": "Dave Snowden"
    },
    "10-Impact-Effort-Matrix": {
        "id": "impact-effort-matrix",
        "title": "Impact-Effort Matrix (영향-노력 매트릭스)",
        "category": "decision_making",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-10명",
        "related": ["67-Decision-Matrix", "55-PMI-Analysis", "16-Critical-Success-Factors"],
        "complementary": ["41-OKR", "43-KPI-Metrics"],
        "keywords": ["우선순위", "Quick Win", "효율성", "자원배분"],
        "use_cases": ["우선순위 결정", "프로젝트 선정", "자원 배분", "개선 활동"],
        "origin": "Eisenhower Matrix 변형"
    },
    "11-Business-Model-Canvas": {
        "id": "business-model-canvas",
        "title": "Business Model Canvas (비즈니스 모델 캔버스)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "1-3시간",
        "group_size": "3-8명",
        "related": ["12-Value-Proposition-Canvas", "13-Lean-Canvas", "05-Jobs-To-Be-Done"],
        "complementary": ["52-SWOT-Analysis", "62-PESTLE-Analysis"],
        "keywords": ["비즈니스모델", "가치제안", "고객세그먼트", "수익모델"],
        "use_cases": ["신사업 기획", "스타트업", "비즈니스 분석", "혁신"],
        "origin": "Alexander Osterwalder"
    },
    "12-Value-Proposition-Canvas": {
        "id": "value-proposition-canvas",
        "title": "Value Proposition Canvas (가치제안 캔버스)",
        "category": "innovation_design",
        "difficulty": "intermediate",
        "time_required": "1-2시간",
        "group_size": "2-6명",
        "related": ["11-Business-Model-Canvas", "05-Jobs-To-Be-Done", "44-Design-Thinking"],
        "complementary": ["17-Stakeholder-Mapping", "52-SWOT-Analysis"],
        "keywords": ["가치제안", "고객", "Pain", "Gain", "Product-Market Fit"],
        "use_cases": ["제품 설계", "마케팅", "고객 이해", "차별화"],
        "origin": "Alexander Osterwalder"
    },
    "13-Lean-Canvas": {
        "id": "lean-canvas",
        "title": "Lean Canvas (린 캔버스)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-5명",
        "related": ["11-Business-Model-Canvas", "12-Value-Proposition-Canvas", "42-Agile-Framework"],
        "complementary": ["07-Assumption-Testing", "48-Pre-Mortem"],
        "keywords": ["린스타트업", "MVP", "Problem-Solution Fit", "스타트업"],
        "use_cases": ["스타트업", "신제품", "린 방법론", "빠른 검증"],
        "origin": "Ash Maurya"
    },
    "14-Theory-of-Constraints-TOC": {
        "id": "theory-of-constraints",
        "title": "Theory of Constraints (제약이론)",
        "category": "problem_solving",
        "difficulty": "advanced",
        "time_required": "1-4시간",
        "group_size": "3-10명",
        "related": ["15-Causal-Loop-Diagrams", "74-Fishbone-Diagram", "51-Five-Whys"],
        "complementary": ["09-Cynefin-Framework", "53-Force-Field-Analysis"],
        "keywords": ["병목", "제약", "5단계", "지속적 개선"],
        "use_cases": ["공정 개선", "생산성", "프로젝트 관리", "조직 최적화"],
        "origin": "Eliyahu Goldratt"
    },
    "15-Causal-Loop-Diagrams": {
        "id": "causal-loop-diagrams",
        "title": "Causal Loop Diagrams (인과 루프 다이어그램)",
        "category": "visualization",
        "difficulty": "advanced",
        "time_required": "1-2시간",
        "group_size": "2-8명",
        "related": ["14-Theory-of-Constraints-TOC", "72-Concept-Map", "74-Fishbone-Diagram"],
        "complementary": ["09-Cynefin-Framework", "70-Scenario-Planning"],
        "keywords": ["시스템사고", "피드백 루프", "강화루프", "균형루프"],
        "use_cases": ["시스템 분석", "복잡한 문제", "정책 설계", "조직 동학"],
        "origin": "Jay Forrester, Peter Senge"
    },
    "16-Critical-Success-Factors": {
        "id": "critical-success-factors",
        "title": "Critical Success Factors (핵심 성공 요인)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "1-2시간",
        "group_size": "3-10명",
        "related": ["41-OKR", "43-KPI-Metrics", "19-Balanced-Scorecard"],
        "complementary": ["52-SWOT-Analysis", "10-Impact-Effort-Matrix"],
        "keywords": ["성공요인", "전략", "KPI", "목표"],
        "use_cases": ["전략 수립", "성과 관리", "프로젝트 계획", "경영 분석"],
        "origin": "D. Ronald Daniel, John Rockart"
    },
    "17-Stakeholder-Mapping": {
        "id": "stakeholder-mapping",
        "title": "Stakeholder Mapping (이해관계자 맵핑)",
        "category": "analysis_convergent",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "2-8명",
        "related": ["52-SWOT-Analysis", "53-Force-Field-Analysis", "62-PESTLE-Analysis"],
        "complementary": ["05-Jobs-To-Be-Done", "44-Design-Thinking"],
        "keywords": ["이해관계자", "Power-Interest", "영향력", "커뮤니케이션"],
        "use_cases": ["프로젝트 관리", "변화 관리", "정치적 분석", "협상"],
        "origin": "R. Edward Freeman"
    },
    "18-Worst-Possible-Idea": {
        "id": "worst-possible-idea",
        "title": "Worst Possible Idea (최악의 아이디어)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "3-12명",
        "related": ["56-Reverse-Brainstorming", "73-Brainstorming", "21-False-Faces-Reversal"],
        "complementary": ["25-SCAMPER", "68-Forced-Connections"],
        "keywords": ["역발상", "창의성", "두려움 제거", "자유로운 발상"],
        "use_cases": ["창의성 촉진", "팀 워밍업", "고착 탈피", "아이스브레이킹"],
        "origin": "IDEO Design Thinking"
    },
    "19-Balanced-Scorecard": {
        "id": "balanced-scorecard",
        "title": "Balanced Scorecard (균형성과표)",
        "category": "strategy_planning",
        "difficulty": "advanced",
        "time_required": "2-4시간",
        "group_size": "5-15명",
        "related": ["41-OKR", "43-KPI-Metrics", "16-Critical-Success-Factors"],
        "complementary": ["52-SWOT-Analysis", "11-Business-Model-Canvas"],
        "keywords": ["재무", "고객", "내부프로세스", "학습성장", "전략맵"],
        "use_cases": ["전략 실행", "성과 관리", "조직 균형", "KPI 설계"],
        "origin": "Robert Kaplan, David Norton"
    },
    "20-TRIZ-Contradiction-Matrix": {
        "id": "triz",
        "title": "TRIZ (창의적 문제해결 이론)",
        "category": "problem_solving",
        "difficulty": "expert",
        "time_required": "1-4시간",
        "group_size": "1-6명",
        "related": ["25-SCAMPER", "60-Morphological-Analysis", "68-Forced-Connections"],
        "complementary": ["61-Synectics", "71-Reframing"],
        "keywords": ["모순", "40원리", "발명", "혁신", "특허"],
        "use_cases": ["기술 혁신", "제품 개발", "모순 해결", "발명"],
        "origin": "Genrich Altshuller"
    },
    "21-False-Faces-Reversal": {
        "id": "false-faces-reversal",
        "title": "False Faces / Reversal (역발상)",
        "category": "creative_divergent",
        "difficulty": "intermediate",
        "time_required": "20-40분",
        "group_size": "1-10명",
        "related": ["56-Reverse-Brainstorming", "18-Worst-Possible-Idea", "25-SCAMPER"],
        "complementary": ["71-Reframing", "49-Six-Thinking-Hats"],
        "keywords": ["역발상", "반전", "가정 뒤집기", "새로운 관점"],
        "use_cases": ["고착 탈피", "혁신", "문제 재정의", "창의적 해결"],
        "origin": "Creative Problem Solving"
    },
    "22-Slice-and-Dice": {
        "id": "slice-and-dice",
        "title": "Slice and Dice (분해 분석)",
        "category": "structured_thinking",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-6명",
        "related": ["69-MECE", "23-Cherry-Split", "74-Fishbone-Diagram"],
        "complementary": ["59-Affinity-Diagram", "54-Mind-Mapping"],
        "keywords": ["분해", "분류", "MECE", "구조화"],
        "use_cases": ["데이터 분석", "문제 분해", "시장 세분화", "구조화"],
        "origin": "McKinsey 컨설팅"
    },
    "23-Cherry-Split": {
        "id": "cherry-split",
        "title": "Cherry Split (체리 분할)",
        "category": "structured_thinking",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-8명",
        "related": ["22-Slice-and-Dice", "69-MECE", "59-Affinity-Diagram"],
        "complementary": ["54-Mind-Mapping", "72-Concept-Map"],
        "keywords": ["분류", "그룹핑", "우선순위", "선별"],
        "use_cases": ["아이디어 분류", "우선순위 결정", "정보 정리", "선택"],
        "origin": "창의적 문제해결"
    },
    "24-Think-Bubbles": {
        "id": "think-bubbles",
        "title": "Think Bubbles (생각 거품)",
        "category": "visualization",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-8명",
        "related": ["54-Mind-Mapping", "72-Concept-Map", "28-Lotus-Blossom"],
        "complementary": ["73-Brainstorming", "59-Affinity-Diagram"],
        "keywords": ["마인드맵", "시각화", "연상", "아이디어"],
        "use_cases": ["아이디어 발산", "노트 정리", "브레인스토밍", "학습"],
        "origin": "Tony Buzan 영향"
    },
    "25-SCAMPER": {
        "id": "scamper",
        "title": "SCAMPER (스캠퍼)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "20-45분",
        "group_size": "1-10명",
        "related": ["20-TRIZ-Contradiction-Matrix", "68-Forced-Connections", "73-Brainstorming"],
        "complementary": ["18-Worst-Possible-Idea", "60-Morphological-Analysis"],
        "keywords": ["대체", "결합", "적용", "수정", "다른용도", "제거", "역전"],
        "use_cases": ["제품 개선", "아이디어 발상", "혁신", "창의성 훈련"],
        "origin": "Bob Eberle (Alex Osborn 기반)"
    },
    "26-Tug-of-War": {
        "id": "tug-of-war",
        "title": "Tug of War (줄다리기)",
        "category": "analysis_convergent",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "2-10명",
        "related": ["53-Force-Field-Analysis", "55-PMI-Analysis", "52-SWOT-Analysis"],
        "complementary": ["67-Decision-Matrix", "49-Six-Thinking-Hats"],
        "keywords": ["찬반", "힘의균형", "장단점", "갈등"],
        "use_cases": ["의사결정", "토론", "이해관계 분석", "협상"],
        "origin": "창의적 문제해결"
    },
    "27-Idea-Box": {
        "id": "idea-box",
        "title": "Idea Box (아이디어 박스)",
        "category": "creative_divergent",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-8명",
        "related": ["60-Morphological-Analysis", "25-SCAMPER", "28-Lotus-Blossom"],
        "complementary": ["68-Forced-Connections", "73-Brainstorming"],
        "keywords": ["조합", "매트릭스", "체계적 발상", "변수"],
        "use_cases": ["제품 개발", "조합 탐색", "옵션 생성", "창의적 해결"],
        "origin": "Fritz Zwicky 영향"
    },
    "28-Lotus-Blossom": {
        "id": "lotus-blossom",
        "title": "Lotus Blossom (연꽃 기법)",
        "category": "visualization",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-8명",
        "related": ["54-Mind-Mapping", "24-Think-Bubbles", "27-Idea-Box"],
        "complementary": ["73-Brainstorming", "72-Concept-Map"],
        "keywords": ["확장", "8방향", "구조화", "심층 탐색"],
        "use_cases": ["아이디어 확장", "주제 탐구", "계획 수립", "문제 분해"],
        "origin": "Yasuo Matsumura (일본)"
    },
    "29-Phoenix-Checklist": {
        "id": "phoenix-checklist",
        "title": "Phoenix Checklist (피닉스 체크리스트)",
        "category": "question_inquiry",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-6명",
        "related": ["02-Kipling-Method", "01-Question-Storming", "04-Socratic-Questioning"],
        "complementary": ["07-Assumption-Testing", "48-Pre-Mortem"],
        "keywords": ["CIA", "체크리스트", "종합질문", "문제정의"],
        "use_cases": ["문제 분석", "정보 수집", "조사", "계획 검토"],
        "origin": "CIA (미국 중앙정보국)"
    },
    "30-BruteThink": {
        "id": "brutethink",
        "title": "BruteThink (무차별 사고)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "20-40분",
        "group_size": "1-10명",
        "related": ["68-Forced-Connections", "25-SCAMPER", "61-Synectics"],
        "complementary": ["73-Brainstorming", "71-Reframing"],
        "keywords": ["무작위", "연결", "자극", "강제연상"],
        "use_cases": ["창의적 돌파", "고착 탈피", "새로운 관점", "아이디어 생성"],
        "origin": "Edward de Bono"
    },
    "31-Chilling-Out": {
        "id": "chilling-out",
        "title": "Chilling Out (휴식과 성찰)",
        "category": "intuitive_creative",
        "difficulty": "beginner",
        "time_required": "5-30분",
        "group_size": "1명",
        "related": ["33-Three-Bs", "36-Dreamscape", "37-Da-Vinci-Technique"],
        "complementary": ["08-Thought-Experiments", "71-Reframing"],
        "keywords": ["휴식", "이완", "무의식", "창의성"],
        "use_cases": ["창의적 막힘", "스트레스 해소", "통찰", "재충전"],
        "origin": "창의성 연구"
    },
    "32-Blue-Roses": {
        "id": "blue-roses",
        "title": "Blue Roses (파란 장미)",
        "category": "intuitive_creative",
        "difficulty": "intermediate",
        "time_required": "20-40분",
        "group_size": "1-6명",
        "related": ["35-Stone-Soup", "36-Dreamscape", "68-Forced-Connections"],
        "complementary": ["71-Reframing", "08-Thought-Experiments"],
        "keywords": ["불가능", "상상", "제약 제거", "이상적"],
        "use_cases": ["혁신", "비전 수립", "제약 탈피", "창의적 도전"],
        "origin": "창의적 사고 기법"
    },
    "33-Three-Bs": {
        "id": "three-bs",
        "title": "Three B's (세 가지 B)",
        "category": "intuitive_creative",
        "difficulty": "beginner",
        "time_required": "유동적",
        "group_size": "1명",
        "related": ["31-Chilling-Out", "36-Dreamscape", "37-Da-Vinci-Technique"],
        "complementary": ["08-Thought-Experiments", "71-Reframing"],
        "keywords": ["Bed", "Bath", "Bus", "무의식", "통찰"],
        "use_cases": ["창의적 휴식", "문제 잠재화", "통찰 대기", "이완"],
        "origin": "창의성 연구 (역사적 관찰)"
    },
    "34-Rattlesnakes-and-Roses": {
        "id": "rattlesnakes-and-roses",
        "title": "Rattlesnakes and Roses (뱀과 장미)",
        "category": "analysis_convergent",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "2-10명",
        "related": ["55-PMI-Analysis", "26-Tug-of-War", "52-SWOT-Analysis"],
        "complementary": ["53-Force-Field-Analysis", "67-Decision-Matrix"],
        "keywords": ["위험", "기회", "긍정", "부정", "균형"],
        "use_cases": ["리스크 분석", "기회 발견", "균형 잡힌 평가", "의사결정"],
        "origin": "창의적 문제해결"
    },
    "35-Stone-Soup": {
        "id": "stone-soup",
        "title": "Stone Soup (돌 수프)",
        "category": "intuitive_creative",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "3-10명",
        "related": ["32-Blue-Roses", "36-Dreamscape", "03-Appreciative-Inquiry"],
        "complementary": ["71-Reframing", "70-Scenario-Planning"],
        "keywords": ["이상적", "환상", "비전", "협력"],
        "use_cases": ["비전 수립", "팀 빌딩", "창의적 돌파", "영감"],
        "origin": "민담 기반 창의 기법"
    },
    "36-Dreamscape": {
        "id": "dreamscape",
        "title": "Dreamscape (꿈 풍경)",
        "category": "intuitive_creative",
        "difficulty": "intermediate",
        "time_required": "20-40분",
        "group_size": "1-6명",
        "related": ["38-Dali-Technique", "37-Da-Vinci-Technique", "35-Stone-Soup"],
        "complementary": ["08-Thought-Experiments", "71-Reframing"],
        "keywords": ["꿈", "상상", "무의식", "시각화"],
        "use_cases": ["창의적 영감", "비전 탐색", "무의식 활용", "예술적 발상"],
        "origin": "초현실주의 영향"
    },
    "37-Da-Vinci-Technique": {
        "id": "da-vinci-technique",
        "title": "Da Vinci Technique (다빈치 기법)",
        "category": "intuitive_creative",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "1-4명",
        "related": ["38-Dali-Technique", "36-Dreamscape", "54-Mind-Mapping"],
        "complementary": ["08-Thought-Experiments", "72-Concept-Map"],
        "keywords": ["시각화", "스케치", "다학제", "관찰"],
        "use_cases": ["시각적 사고", "문제 탐구", "창의적 연결", "발명"],
        "origin": "Leonardo da Vinci"
    },
    "38-Dali-Technique": {
        "id": "dali-technique",
        "title": "Dali Technique (달리 기법)",
        "category": "intuitive_creative",
        "difficulty": "advanced",
        "time_required": "20-40분",
        "group_size": "1명",
        "related": ["36-Dreamscape", "37-Da-Vinci-Technique", "33-Three-Bs"],
        "complementary": ["31-Chilling-Out", "68-Forced-Connections"],
        "keywords": ["수면", "최면", "무의식", "초현실"],
        "use_cases": ["창의적 영감", "무의식 활용", "예술", "돌파구"],
        "origin": "Salvador Dali"
    },
    "39-Not-Kansas": {
        "id": "not-kansas",
        "title": "Not Kansas (캔자스가 아냐)",
        "category": "creative_divergent",
        "difficulty": "intermediate",
        "time_required": "20-40분",
        "group_size": "2-10명",
        "related": ["71-Reframing", "68-Forced-Connections", "61-Synectics"],
        "complementary": ["08-Thought-Experiments", "70-Scenario-Planning"],
        "keywords": ["맥락전환", "다른세계", "은유", "새로운관점"],
        "use_cases": ["관점 전환", "창의적 해결", "고착 탈피", "혁신"],
        "origin": "오즈의 마법사 (은유)"
    },
    "40-Murder-Board": {
        "id": "murder-board",
        "title": "Murder Board (머더 보드)",
        "category": "analysis_convergent",
        "difficulty": "advanced",
        "time_required": "1-2시간",
        "group_size": "5-12명",
        "related": ["48-Pre-Mortem", "07-Assumption-Testing", "29-Phoenix-Checklist"],
        "complementary": ["49-Six-Thinking-Hats", "52-SWOT-Analysis"],
        "keywords": ["비판", "검증", "약점발견", "스트레스테스트"],
        "use_cases": ["제안서 검토", "전략 검증", "투자 심사", "프레젠테이션 준비"],
        "origin": "미국 군대, NASA"
    },
    "41-OKR": {
        "id": "okr",
        "title": "OKR (목표와 핵심결과)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "1-3시간",
        "group_size": "1-50명",
        "related": ["43-KPI-Metrics", "16-Critical-Success-Factors", "19-Balanced-Scorecard"],
        "complementary": ["42-Agile-Framework", "10-Impact-Effort-Matrix"],
        "keywords": ["목표", "핵심결과", "정렬", "투명성", "구글"],
        "use_cases": ["목표 설정", "성과 관리", "조직 정렬", "분기 계획"],
        "origin": "Andy Grove (Intel), John Doerr"
    },
    "42-Agile-Framework": {
        "id": "agile-framework",
        "title": "Agile Framework (애자일)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "지속적",
        "group_size": "5-9명 (스크럼팀)",
        "related": ["13-Lean-Canvas", "41-OKR", "44-Design-Thinking"],
        "complementary": ["48-Pre-Mortem", "63-World-Cafe"],
        "keywords": ["스크럼", "칸반", "스프린트", "반복", "적응"],
        "use_cases": ["소프트웨어 개발", "프로젝트 관리", "제품 개발", "팀 운영"],
        "origin": "Agile Manifesto (2001)"
    },
    "43-KPI-Metrics": {
        "id": "kpi-metrics",
        "title": "KPI & Metrics (핵심성과지표)",
        "category": "strategy_planning",
        "difficulty": "intermediate",
        "time_required": "1-2시간",
        "group_size": "2-10명",
        "related": ["41-OKR", "16-Critical-Success-Factors", "19-Balanced-Scorecard"],
        "complementary": ["10-Impact-Effort-Matrix", "67-Decision-Matrix"],
        "keywords": ["지표", "측정", "성과", "대시보드", "모니터링"],
        "use_cases": ["성과 측정", "의사결정", "개선 추적", "보고"],
        "origin": "경영학, 품질관리"
    },
    "44-Design-Thinking": {
        "id": "design-thinking",
        "title": "Design Thinking (디자인 씽킹)",
        "category": "innovation_design",
        "difficulty": "intermediate",
        "time_required": "1-5일",
        "group_size": "4-8명",
        "related": ["05-Jobs-To-Be-Done", "12-Value-Proposition-Canvas", "03-Appreciative-Inquiry"],
        "complementary": ["73-Brainstorming", "25-SCAMPER"],
        "keywords": ["공감", "정의", "아이디에이션", "프로토타입", "테스트", "IDEO"],
        "use_cases": ["제품 개발", "서비스 디자인", "혁신", "고객 경험"],
        "origin": "Stanford d.school, IDEO"
    },
    "48-Pre-Mortem": {
        "id": "pre-mortem",
        "title": "Pre-Mortem (사전 부검)",
        "category": "analysis_convergent",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "4-12명",
        "related": ["07-Assumption-Testing", "40-Murder-Board", "70-Scenario-Planning"],
        "complementary": ["52-SWOT-Analysis", "53-Force-Field-Analysis"],
        "keywords": ["리스크", "실패예측", "예방", "시나리오"],
        "use_cases": ["프로젝트 계획", "리스크 관리", "의사결정", "팀 정렬"],
        "origin": "Gary Klein"
    },
    "49-Six-Thinking-Hats": {
        "id": "six-thinking-hats",
        "title": "Six Thinking Hats (여섯 색깔 모자)",
        "category": "problem_solving",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "2-12명",
        "related": ["01-Question-Storming", "55-PMI-Analysis", "65-Multi-Perspective-Questioning"],
        "complementary": ["73-Brainstorming", "67-Decision-Matrix"],
        "keywords": ["병렬사고", "관점", "흰색", "빨강", "검정", "노랑", "초록", "파랑"],
        "use_cases": ["회의 진행", "의사결정", "문제해결", "팀 토론"],
        "origin": "Edward de Bono"
    },
    "50-Fishbone-Diagram": {
        "id": "fishbone-diagram-50",
        "title": "Fishbone Diagram (특성요인도)",
        "category": "root_cause",
        "difficulty": "beginner",
        "time_required": "30-60분",
        "group_size": "3-8명",
        "related": ["51-Five-Whys", "74-Fishbone-Diagram", "14-Theory-of-Constraints-TOC"],
        "complementary": ["15-Causal-Loop-Diagrams", "52-SWOT-Analysis"],
        "keywords": ["원인분석", "6M", "이시카와", "품질"],
        "use_cases": ["품질 문제", "근본원인", "공정개선", "문제해결"],
        "origin": "Kaoru Ishikawa"
    },
    "51-Five-Whys": {
        "id": "five-whys",
        "title": "Five Whys (5 Whys)",
        "category": "root_cause",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "2-6명",
        "related": ["74-Fishbone-Diagram", "04-Socratic-Questioning", "14-Theory-of-Constraints-TOC"],
        "complementary": ["50-Fishbone-Diagram", "52-SWOT-Analysis"],
        "keywords": ["왜", "근본원인", "Toyota", "린"],
        "use_cases": ["근본원인 분석", "품질 문제", "프로세스 개선", "문제해결"],
        "origin": "Sakichi Toyoda (Toyota)"
    },
    "52-SWOT-Analysis": {
        "id": "swot-analysis",
        "title": "SWOT Analysis (SWOT 분석)",
        "category": "analysis_convergent",
        "difficulty": "beginner",
        "time_required": "30-60분",
        "group_size": "2-10명",
        "related": ["62-PESTLE-Analysis", "53-Force-Field-Analysis", "17-Stakeholder-Mapping"],
        "complementary": ["11-Business-Model-Canvas", "70-Scenario-Planning"],
        "keywords": ["강점", "약점", "기회", "위협", "전략"],
        "use_cases": ["전략 수립", "경쟁 분석", "자기 평가", "의사결정"],
        "origin": "Albert Humphrey (Stanford)"
    },
    "53-Force-Field-Analysis": {
        "id": "force-field-analysis",
        "title": "Force Field Analysis (힘의 장 분석)",
        "category": "analysis_convergent",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "3-10명",
        "related": ["52-SWOT-Analysis", "26-Tug-of-War", "48-Pre-Mortem"],
        "complementary": ["17-Stakeholder-Mapping", "67-Decision-Matrix"],
        "keywords": ["추진력", "저항력", "변화관리", "균형"],
        "use_cases": ["변화 관리", "의사결정", "저항 분석", "계획 수립"],
        "origin": "Kurt Lewin"
    },
    "54-Mind-Mapping": {
        "id": "mind-mapping",
        "title": "Mind Mapping (마인드맵)",
        "category": "visualization",
        "difficulty": "beginner",
        "time_required": "15-60분",
        "group_size": "1-6명",
        "related": ["72-Concept-Map", "24-Think-Bubbles", "28-Lotus-Blossom"],
        "complementary": ["73-Brainstorming", "59-Affinity-Diagram"],
        "keywords": ["시각화", "방사형", "연상", "아이디어"],
        "use_cases": ["아이디어 정리", "노트 정리", "계획", "학습"],
        "origin": "Tony Buzan"
    },
    "55-PMI-Analysis": {
        "id": "pmi-analysis",
        "title": "PMI Analysis (Plus-Minus-Interesting)",
        "category": "decision_making",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-10명",
        "related": ["52-SWOT-Analysis", "26-Tug-of-War", "34-Rattlesnakes-and-Roses"],
        "complementary": ["67-Decision-Matrix", "49-Six-Thinking-Hats"],
        "keywords": ["장점", "단점", "흥미로운점", "평가"],
        "use_cases": ["아이디어 평가", "의사결정", "빠른 분석", "토론"],
        "origin": "Edward de Bono"
    },
    "56-Reverse-Brainstorming": {
        "id": "reverse-brainstorming",
        "title": "Reverse Brainstorming (역 브레인스토밍)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "20-40분",
        "group_size": "3-12명",
        "related": ["18-Worst-Possible-Idea", "21-False-Faces-Reversal", "73-Brainstorming"],
        "complementary": ["25-SCAMPER", "71-Reframing"],
        "keywords": ["역발상", "문제악화", "반전", "창의성"],
        "use_cases": ["창의적 해결", "문제 재정의", "숨겨진 원인", "혁신"],
        "origin": "창의적 문제해결"
    },
    "57-Starbursting": {
        "id": "starbursting",
        "title": "Starbursting (별폭발)",
        "category": "question_inquiry",
        "difficulty": "beginner",
        "time_required": "20-40분",
        "group_size": "2-10명",
        "related": ["02-Kipling-Method", "01-Question-Storming", "73-Brainstorming"],
        "complementary": ["04-Socratic-Questioning", "29-Phoenix-Checklist"],
        "keywords": ["5W1H", "질문", "탐색", "아이디어검증"],
        "use_cases": ["아이디어 검증", "계획 검토", "질문 생성", "요구사항"],
        "origin": "브레인스토밍 변형"
    },
    "58-Brainwriting-635": {
        "id": "brainwriting-635",
        "title": "Brainwriting 6-3-5",
        "category": "group_collaboration",
        "difficulty": "beginner",
        "time_required": "30-45분",
        "group_size": "6명",
        "related": ["73-Brainstorming", "06-Liberating-Structures-1-2-4-All", "59-Affinity-Diagram"],
        "complementary": ["25-SCAMPER", "49-Six-Thinking-Hats"],
        "keywords": ["침묵", "글쓰기", "구조화", "108아이디어"],
        "use_cases": ["아이디어 발산", "내향적 참여", "평등한 참여", "팀 창의성"],
        "origin": "Bernd Rohrbach (1969)"
    },
    "59-Affinity-Diagram": {
        "id": "affinity-diagram",
        "title": "Affinity Diagram (친화도)",
        "category": "structured_thinking",
        "difficulty": "beginner",
        "time_required": "30-60분",
        "group_size": "3-10명",
        "related": ["69-MECE", "22-Slice-and-Dice", "54-Mind-Mapping"],
        "complementary": ["73-Brainstorming", "72-Concept-Map"],
        "keywords": ["그룹핑", "패턴", "분류", "KJ법"],
        "use_cases": ["아이디어 정리", "데이터 분류", "패턴 발견", "합의 도출"],
        "origin": "Jiro Kawakita (KJ법)"
    },
    "60-Morphological-Analysis": {
        "id": "morphological-analysis",
        "title": "Morphological Analysis (형태학적 분석)",
        "category": "creative_divergent",
        "difficulty": "advanced",
        "time_required": "1-3시간",
        "group_size": "2-8명",
        "related": ["27-Idea-Box", "20-TRIZ-Contradiction-Matrix", "25-SCAMPER"],
        "complementary": ["68-Forced-Connections", "67-Decision-Matrix"],
        "keywords": ["조합", "매트릭스", "변수", "체계적"],
        "use_cases": ["제품 개발", "시나리오 생성", "조합 탐색", "혁신"],
        "origin": "Fritz Zwicky"
    },
    "61-Synectics": {
        "id": "synectics",
        "title": "Synectics (시네틱스)",
        "category": "creative_divergent",
        "difficulty": "advanced",
        "time_required": "1-2시간",
        "group_size": "5-10명",
        "related": ["68-Forced-Connections", "30-BruteThink", "39-Not-Kansas"],
        "complementary": ["20-TRIZ-Contradiction-Matrix", "71-Reframing"],
        "keywords": ["유추", "은유", "낯설게하기", "친숙하게하기"],
        "use_cases": ["혁신", "문제해결", "창의적 돌파", "팀 창의성"],
        "origin": "William Gordon"
    },
    "62-PESTLE-Analysis": {
        "id": "pestle-analysis",
        "title": "PESTLE Analysis (거시환경 분석)",
        "category": "analysis_convergent",
        "difficulty": "intermediate",
        "time_required": "1-2시간",
        "group_size": "2-10명",
        "related": ["52-SWOT-Analysis", "17-Stakeholder-Mapping", "70-Scenario-Planning"],
        "complementary": ["11-Business-Model-Canvas", "09-Cynefin-Framework"],
        "keywords": ["정치", "경제", "사회", "기술", "법률", "환경"],
        "use_cases": ["전략 분석", "시장 진입", "리스크 분석", "환경 스캐닝"],
        "origin": "Francis Aguilar (PEST)"
    },
    "63-World-Cafe": {
        "id": "world-cafe",
        "title": "World Cafe (월드카페)",
        "category": "group_collaboration",
        "difficulty": "intermediate",
        "time_required": "1-3시간",
        "group_size": "12-100명+",
        "related": ["06-Liberating-Structures-1-2-4-All", "03-Appreciative-Inquiry", "73-Brainstorming"],
        "complementary": ["59-Affinity-Diagram", "49-Six-Thinking-Hats"],
        "keywords": ["대화", "카페", "집단지성", "순환"],
        "use_cases": ["대규모 토론", "지식 공유", "합의 도출", "커뮤니티"],
        "origin": "Juanita Brown, David Isaacs"
    },
    "64-Thinking-Tools-Guide": {
        "id": "thinking-tools-guide",
        "title": "Thinking Tools Guide (사고도구 가이드)",
        "category": "structured_thinking",
        "difficulty": "beginner",
        "time_required": "참조용",
        "group_size": "해당없음",
        "related": ["66-Questions-Tools-Integration-Guide", "all"],
        "complementary": ["all"],
        "keywords": ["가이드", "선택", "도구선택", "방법론"],
        "use_cases": ["도구 선택", "학습", "퍼실리테이션", "참조"],
        "origin": "통합 가이드"
    },
    "65-Multi-Perspective-Questioning": {
        "id": "multi-perspective-questioning",
        "title": "Multi-Perspective Questioning (다중관점 질문)",
        "category": "question_inquiry",
        "difficulty": "intermediate",
        "time_required": "30-60분",
        "group_size": "2-10명",
        "related": ["49-Six-Thinking-Hats", "01-Question-Storming", "71-Reframing"],
        "complementary": ["04-Socratic-Questioning", "17-Stakeholder-Mapping"],
        "keywords": ["관점", "다양성", "PERSPECTIVE", "Six Hats"],
        "use_cases": ["문제 분석", "이해관계자 이해", "편향 제거", "종합적 분석"],
        "origin": "통합 방법론"
    },
    "66-Questions-Tools-Integration-Guide": {
        "id": "questions-tools-integration",
        "title": "Questions-Tools Integration Guide",
        "category": "structured_thinking",
        "difficulty": "intermediate",
        "time_required": "참조용",
        "group_size": "해당없음",
        "related": ["64-Thinking-Tools-Guide", "01-Question-Storming", "all"],
        "complementary": ["all"],
        "keywords": ["통합", "질문", "도구연결", "워크플로우"],
        "use_cases": ["도구 조합", "워크샵 설계", "프로세스 설계", "학습"],
        "origin": "통합 가이드"
    },
    "67-Decision-Matrix": {
        "id": "decision-matrix",
        "title": "Decision Matrix (의사결정 매트릭스)",
        "category": "decision_making",
        "difficulty": "intermediate",
        "time_required": "20-45분",
        "group_size": "1-8명",
        "related": ["10-Impact-Effort-Matrix", "55-PMI-Analysis", "69-MECE"],
        "complementary": ["52-SWOT-Analysis", "49-Six-Thinking-Hats"],
        "keywords": ["가중치", "평가", "점수", "비교", "선택"],
        "use_cases": ["대안 선택", "우선순위", "객관적 평가", "팀 의사결정"],
        "origin": "의사결정 과학"
    },
    "68-Forced-Connections": {
        "id": "forced-connections",
        "title": "Forced Connections (강제 연결법)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "15-30분",
        "group_size": "1-10명",
        "related": ["30-BruteThink", "25-SCAMPER", "61-Synectics"],
        "complementary": ["73-Brainstorming", "71-Reframing"],
        "keywords": ["무작위", "연결", "자극", "측면사고"],
        "use_cases": ["창의적 막힘", "새로운 아이디어", "고착 탈피", "혁신"],
        "origin": "Edward de Bono"
    },
    "69-MECE": {
        "id": "mece",
        "title": "MECE (상호배타적 전체포괄적)",
        "category": "structured_thinking",
        "difficulty": "intermediate",
        "time_required": "15-30분",
        "group_size": "1-5명",
        "related": ["22-Slice-and-Dice", "59-Affinity-Diagram", "74-Fishbone-Diagram"],
        "complementary": ["67-Decision-Matrix", "52-SWOT-Analysis"],
        "keywords": ["구조화", "분류", "McKinsey", "로직트리"],
        "use_cases": ["문제 분해", "전략 분석", "프레젠테이션", "데이터 분류"],
        "origin": "McKinsey & Company"
    },
    "70-Scenario-Planning": {
        "id": "scenario-planning",
        "title": "Scenario Planning (시나리오 플래닝)",
        "category": "strategy_planning",
        "difficulty": "advanced",
        "time_required": "2-8시간",
        "group_size": "5-15명",
        "related": ["48-Pre-Mortem", "62-PESTLE-Analysis", "09-Cynefin-Framework"],
        "complementary": ["52-SWOT-Analysis", "08-Thought-Experiments"],
        "keywords": ["미래", "불확실성", "시나리오", "전략적유연성"],
        "use_cases": ["장기 전략", "불확실성 대응", "투자 결정", "정책 수립"],
        "origin": "Royal Dutch Shell"
    },
    "71-Reframing": {
        "id": "reframing",
        "title": "Reframing (리프레이밍)",
        "category": "problem_solving",
        "difficulty": "intermediate",
        "time_required": "15-45분",
        "group_size": "1-8명",
        "related": ["21-False-Faces-Reversal", "39-Not-Kansas", "04-Socratic-Questioning"],
        "complementary": ["49-Six-Thinking-Hats", "68-Forced-Connections"],
        "keywords": ["관점전환", "재정의", "프레임", "인지"],
        "use_cases": ["문제 재정의", "갈등 해소", "창의적 돌파", "코칭"],
        "origin": "인지치료, NLP"
    },
    "72-Concept-Map": {
        "id": "concept-map",
        "title": "Concept Map (개념도)",
        "category": "visualization",
        "difficulty": "beginner",
        "time_required": "20-60분",
        "group_size": "1-6명",
        "related": ["54-Mind-Mapping", "15-Causal-Loop-Diagrams", "28-Lotus-Blossom"],
        "complementary": ["59-Affinity-Diagram", "73-Brainstorming"],
        "keywords": ["개념", "관계", "시각화", "명제"],
        "use_cases": ["지식 구조화", "학습", "복잡한 관계", "공유"],
        "origin": "Joseph Novak"
    },
    "73-Brainstorming": {
        "id": "brainstorming",
        "title": "Brainstorming (브레인스토밍)",
        "category": "creative_divergent",
        "difficulty": "beginner",
        "time_required": "15-45분",
        "group_size": "4-12명",
        "related": ["58-Brainwriting-635", "25-SCAMPER", "18-Worst-Possible-Idea"],
        "complementary": ["59-Affinity-Diagram", "67-Decision-Matrix"],
        "keywords": ["아이디어", "발산", "비판금지", "양"],
        "use_cases": ["아이디어 생성", "문제해결", "팀 창의성", "워크샵"],
        "origin": "Alex Osborn"
    },
    "74-Fishbone-Diagram": {
        "id": "fishbone-diagram",
        "title": "Fishbone Diagram (특성요인도)",
        "category": "root_cause",
        "difficulty": "beginner",
        "time_required": "30-60분",
        "group_size": "3-8명",
        "related": ["51-Five-Whys", "50-Fishbone-Diagram", "69-MECE"],
        "complementary": ["14-Theory-of-Constraints-TOC", "52-SWOT-Analysis"],
        "keywords": ["원인분석", "6M", "이시카와", "품질"],
        "use_cases": ["근본원인", "품질 문제", "공정개선", "팀 분석"],
        "origin": "Kaoru Ishikawa"
    }
}

# 중복 파일 처리 (45, 46, 47은 상위 버전과 연결)
METADATA["45-Jobs-to-be-Done"] = METADATA["05-Jobs-To-Be-Done"].copy()
METADATA["45-Jobs-to-be-Done"]["id"] = "jobs-to-be-done-detailed"
METADATA["46-Value-Proposition-Canvas"] = METADATA["12-Value-Proposition-Canvas"].copy()
METADATA["46-Value-Proposition-Canvas"]["id"] = "value-proposition-canvas-detailed"
METADATA["47-Lean-Canvas"] = METADATA["13-Lean-Canvas"].copy()
METADATA["47-Lean-Canvas"]["id"] = "lean-canvas-detailed"

def generate_frontmatter(file_key):
    """YAML frontmatter 생성"""
    if file_key not in METADATA:
        return None

    m = METADATA[file_key]
    cat_kr = CATEGORIES.get(m["category"], m["category"])

    lines = [
        "---",
        f"id: {m['id']}",
        f"title: {m['title']}",
        f"category: {m['category']}",
        f"category_kr: {cat_kr}",
        f"difficulty: {m['difficulty']}",
        f"time_required: {m['time_required']}",
        f"group_size: {m['group_size']}",
        "",
        "related_methods:"
    ]

    for rel in m.get("related", []):
        lines.append(f"  - {rel}")

    lines.append("")
    lines.append("complementary_methods:")
    for comp in m.get("complementary", []):
        lines.append(f"  - {comp}")

    lines.append("")
    lines.append("keywords:")
    for kw in m.get("keywords", []):
        lines.append(f"  - {kw}")

    lines.append("")
    lines.append("use_cases:")
    for uc in m.get("use_cases", []):
        lines.append(f"  - {uc}")

    if m.get("origin"):
        lines.append("")
        lines.append(f"origin: {m['origin']}")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)

def process_file(filepath):
    """파일에 frontmatter 추가"""
    filename = os.path.basename(filepath)
    file_key = filename.replace(".md", "")

    if file_key not in METADATA:
        print(f"SKIP: {filename} - no metadata defined")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 이미 frontmatter가 있으면 제거
    if content.startswith("---"):
        # 두 번째 ---를 찾아서 그 이후부터 사용
        second_dash = content.find("---", 3)
        if second_dash != -1:
            content = content[second_dash + 3:].lstrip()

    frontmatter = generate_frontmatter(file_key)
    if not frontmatter:
        return False

    new_content = frontmatter + content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"UPDATED: {filename}")
    return True

def main():
    """메인 실행"""
    knowledge_dir = Path(__file__).parent

    processed = 0
    skipped = 0

    for md_file in sorted(knowledge_dir.glob("[0-9]*.md")):
        if process_file(md_file):
            processed += 1
        else:
            skipped += 1

    print(f"\n완료: {processed}개 처리, {skipped}개 스킵")

if __name__ == "__main__":
    main()
