"""
압축된 방법론 템플릿
토큰 최소화를 위해 질문 템플릿만 저장
"""

# LINEAR THINKERTOYS
LINEAR_METHODS = {
    "reversal": {
        "name": "FALSE FACES (Reversal)",
        "category": "linear",
        "steps": 3,
        "best_for": "challenging_assumptions",
        "questions": [
            "귀하의 도전과제에 대한 근본적인 가정은 무엇입니까?",
            "각 가정의 정반대는 무엇입니까?",
            "각각의 반전된 가정을 어떻게 실현할 수 있습니까?"
        ]
    },
    "attribute_listing": {
        "name": "SLICE AND DICE (Attribute Listing)",
        "category": "linear",
        "steps": 3,
        "best_for": "product_improvement",
        "questions": [
            "이 도전과제의 모든 속성(특성)은 무엇입니까?",
            "각 속성을 어떻게 다르게 달성할 수 있습니까?",
            "왜 각 속성이 이런 방식이어야 합니까?"
        ]
    },
    "fractionation": {
        "name": "CHERRY SPLIT (Fractionation)",
        "category": "linear",
        "steps": 4,
        "best_for": "breaking_down_complex",
        "questions": [
            "도전과제의 핵심을 2개 단어로 표현하면 무엇입니까?",
            "각 구성요소를 어떻게 더 세분화할 수 있습니까?",
            "각 속성을 계속 나누면 어떤 요소들이 나옵니까?",
            "재조합하면 어떤 새로운 조합이 나옵니까?"
        ]
    },
    "mind_mapping": {
        "name": "THINK BUBBLES (Mind Mapping)",
        "category": "linear",
        "steps": 3,
        "best_for": "finding_connections",
        "questions": [
            "주제를 떠올리게 하는 핵심 단어는 무엇입니까?",
            "고립된 조각들 사이에 어떤 연결이 존재합니까?",
            "개념들이 자연스럽게 어떻게 군집을 이룹니까?"
        ]
    },
    "scamper": {
        "name": "SCAMPER",
        "category": "linear",
        "steps": 7,
        "best_for": "product_innovation",
        "questions": [
            "SUBSTITUTE: 무엇을 대체할 수 있습니까?",
            "COMBINE: 무엇과 결합할 수 있습니까?",
            "ADAPT: 다른 곳에서 무엇을 적용할 수 있습니까?",
            "MODIFY/MAGNIFY: 무엇을 수정하거나 확대할 수 있습니까?",
            "PUT TO OTHER USE: 다른 용도로 사용할 수 있습니까?",
            "ELIMINATE: 무엇을 제거할 수 있습니까?",
            "REVERSE/REARRANGE: 무엇을 뒤집거나 재배열할 수 있습니까?"
        ]
    },
    "force_field": {
        "name": "TUG-OF-WAR (Force-Field Analysis)",
        "category": "linear",
        "steps": 4,
        "best_for": "analyzing_forces",
        "questions": [
            "최선의 시나리오는 무엇입니까?",
            "최악의 시나리오는 무엇입니까?",
            "최선으로 이끄는 긍정적 힘은 무엇입니까?",
            "최악으로 끌어당기는 부정적 힘은 무엇입니까?"
        ]
    },
    "morphological": {
        "name": "IDEA BOX (Morphological Analysis)",
        "category": "linear",
        "steps": 3,
        "best_for": "generating_combinations",
        "questions": [
            "도전과제의 파라미터(변수)는 무엇입니까?",
            "각 파라미터의 변형은 무엇입니까?",
            "어떤 조합이 새로운 아이디어를 만듭니까?"
        ]
    },
    "fcb_grid": {
        "name": "IDEA GRID (FCB Grid)",
        "category": "linear",
        "steps": 3,
        "best_for": "market_positioning",
        "questions": [
            "High/Low involvement 중 어디에 위치합니까?",
            "Think/Feel 중 어디에 위치합니까?",
            "시장의 어떤 빈틈이 존재합니까?"
        ]
    },
    "lotus_blossom": {
        "name": "LOTUS BLOSSOM",
        "category": "linear",
        "steps": 3,
        "best_for": "expanding_ideas",
        "questions": [
            "중심 주제를 둘러싼 8가지 테마는 무엇입니까?",
            "각 테마가 어떻게 더 확장됩니까?",
            "전체 연꽃에서 어떤 패턴이 나타납니까?"
        ]
    },
    "phoenix": {
        "name": "PHOENIX Checklist",
        "category": "linear",
        "steps": 7,
        "best_for": "comprehensive_analysis",
        "questions": [
            "WHY: 왜 이 문제를 해결해야 합니까?",
            "WHAT: 미지의 것은 무엇입니까?",
            "WHAT: 어떤 정보를 가지고 있습니까?",
            "WHAT: 이것이 문제가 아닌 것은 무엇입니까?",
            "WHERE: 문제의 경계는 어디입니까?",
            "HOW: 부분들을 어떻게 분리할 수 있습니까?",
            "WHAT: 변경할 수 없는 상수는 무엇입니까?"
        ]
    },
    "keyword_categorization": {
        "name": "THE GREAT TRANSPACIFIC AIRLINE",
        "category": "linear",
        "steps": 4,
        "best_for": "business_strategy",
        "questions": [
            "우리 사업은 무엇입니까?",
            "우리 사업은 무엇이어야 합니까?",
            "각 변수를 정의하는 키워드는 무엇입니까?",
            "어떤 새로운 조합이 나타납니까?"
        ]
    },
    "future_scenarios": {
        "name": "FUTURE FRUIT",
        "category": "linear",
        "steps": 3,
        "best_for": "future_planning",
        "questions": [
            "어떤 트렌드가 나타나고 있습니까?",
            "가능한 3가지 미래 시나리오는 무엇입니까?",
            "각각을 어떻게 활용할 수 있습니까?"
        ]
    }
}

# INTUITIVE THINKERTOYS
INTUITIVE_METHODS = {
    "relaxation": {
        "name": "CHILLING OUT (Relaxation)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "clearing_mind",
        "questions": [
            "조용한 환경에 있습니까?",
            "마음을 비웠습니까?",
            "침묵 속에서 무엇이 떠오릅니까?"
        ]
    },
    "intuition": {
        "name": "BLUE ROSES (Intuition)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "developing_intuition",
        "questions": [
            "분석 전 직관적 느낌은 무엇입니까?",
            "어떻게 직관적 추측을 연습할 수 있습니까?",
            "직관이 이성과 어떻게 결합됩니까?"
        ]
    },
    "incubation": {
        "name": "THE THREE B'S (Bus, Bed, Bath)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "subconscious_processing",
        "questions": [
            "중요한 정보를 수집했습니까?",
            "뇌에 해결책을 찾으라고 지시했습니까?",
            "인큐베이션 중 어떤 통찰이 나타납니까?"
        ]
    },
    "random_stimulation": {
        "name": "BRUTETHINK (Random Stimulation)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "breaking_patterns",
        "questions": [
            "완전히 무작위 단어는 무엇입니까?",
            "이 단어에서 어떤 연상이 나옵니까?",
            "도전과제와 어떻게 강제로 연결할 수 있습니까?"
        ]
    },
    "hall_of_fame": {
        "name": "HALL OF FAME (Forced Connection)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "wisdom_from_greats",
        "questions": [
            "개인적 영웅은 누구입니까?",
            "그들의 명언은 무엇입니까?",
            "도전과제와 어떻게 관련됩니까?"
        ]
    },
    "circle_opportunity": {
        "name": "CIRCLE OF OPPORTUNITY",
        "category": "intuitive",
        "steps": 3,
        "best_for": "attribute_connection",
        "questions": [
            "도전과제의 12가지 속성은 무엇입니까?",
            "주사위가 선택한 2가지 속성은 무엇입니까?",
            "둘 사이에 어떤 연결이 나타납니까?"
        ]
    },
    "ideatoons": {
        "name": "IDEATOONS (Pattern Language)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "visual_thinking",
        "questions": [
            "각 속성을 나타내는 심볼은 무엇입니까?",
            "심볼을 어떻게 무작위로 그룹화할 수 있습니까?",
            "심볼 패턴에서 어떤 아이디어가 나옵니까?"
        ]
    },
    "talk_stranger": {
        "name": "CLEVER TREVOR (Talk to a Stranger)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "outside_perspective",
        "questions": [
            "귀하의 분야 밖에 있는 사람은 누구입니까?",
            "그들은 어떤 독특한 관점을 제공합니까?",
            "경청을 통해 무엇을 배웠습니까?"
        ]
    },
    "analogies": {
        "name": "RATTLESNAKES AND ROSES (Analogies)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "finding_analogies",
        "questions": [
            "도전과제와 평행한 분야는 무엇입니까?",
            "그 분야에서 관련된 이미지는 무엇입니까?",
            "어떤 유사성과 연결이 존재합니까?"
        ]
    },
    "fantasy_questions": {
        "name": "STONE SOUP (Fantasy Questions)",
        "category": "intuitive",
        "steps": 5,
        "best_for": "imaginative_thinking",
        "questions": [
            "만약 중력이 없다면?",
            "만약 고객이 마음을 읽을 수 있다면?",
            "만약 시간이 거꾸로 간다면?",
            "만약 돈이 무제한이라면?",
            "만약 물리 법칙이 다르다면?"
        ]
    },
    "paradox": {
        "name": "TRUE AND FALSE (Paradox)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "opposite_thinking",
        "questions": [
            "문제의 반대는 무엇입니까?",
            "둘이 어떻게 동시에 존재할 수 있습니까?",
            "이 역설에서 어떤 통찰이 나옵니까?"
        ]
    },
    "dreamscape": {
        "name": "DREAMSCAPE (Dreams)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "dream_insights",
        "questions": [
            "잠들기 전 어떤 질문을 할 것입니까?",
            "꿈에 어떤 이미지가 나타났습니까?",
            "꿈의 상징에서 어떤 연상이 나옵니까?"
        ]
    },
    "da_vinci": {
        "name": "DA VINCI'S TECHNIQUE (Drawing)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "visual_expression",
        "questions": [
            "직관이 제공하는 이미지는 무엇입니까?",
            "자유롭게 그릴 때 무엇이 나타납니까?",
            "그림을 보면 어떤 단어가 떠오릅니까?"
        ]
    },
    "dali": {
        "name": "DALI'S TECHNIQUE (Hypnogogic Imagery)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "surrealistic_imagery",
        "questions": [
            "잠들기 직전에 무엇이 나타납니까?",
            "어떤 초현실적 이미지가 나타납니까?",
            "도전과제와의 연상적 연결은 무엇입니까?"
        ]
    },
    "not_kansas": {
        "name": "NOT KANSAS (Guided Imagery)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "guided_journey",
        "questions": [
            "상상력이 어디로 데려갑니까?",
            "여정에서 어떤 메시지가 나타납니까?",
            "어떤 특성과 단서가 나타납니까?"
        ]
    },
    "shadow": {
        "name": "THE SHADOW (Psychosynthesis)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "inner_wisdom",
        "questions": [
            "영적 멘토는 누구입니까?",
            "그들은 어떤 조언을 제공합니까?",
            "대화에서 어떤 지혜가 나타납니까?"
        ]
    },
    "hieroglyphics": {
        "name": "BOOK OF THE DEAD (Hieroglyphics)",
        "category": "intuitive",
        "steps": 3,
        "best_for": "symbolic_interpretation",
        "questions": [
            "각 심볼이 당신에게 의미하는 것은 무엇입니까?",
            "상형문자가 도전과제와 어떻게 관련됩니까?",
            "어떤 예상치 못한 해석이 나타납니까?"
        ]
    }
}

# PERSPECTIVE METHODS
PERSPECTIVE_METHODS = {
    "six_hats": {
        "name": "SIX THINKING HATS",
        "category": "perspective",
        "steps": 6,
        "best_for": "multi_perspective",
        "questions": [
            "⚪ WHITE HAT: 사실과 데이터는 무엇입니까?",
            "🔴 RED HAT: 감정과 직관은 무엇을 말합니까?",
            "⚫ BLACK HAT: 위험과 단점은 무엇입니까?",
            "🟡 YELLOW HAT: 이점과 기회는 무엇입니까?",
            "🟢 GREEN HAT: 창의적 대안은 무엇입니까?",
            "🔵 BLUE HAT: 프로세스와 다음 단계는 무엇입니까?"
        ]
    },
    "five_whys": {
        "name": "5 WHYS",
        "category": "perspective",
        "steps": 5,
        "best_for": "root_cause",
        "questions": [
            "WHY 1: 왜 이것이 발생합니까?",
            "WHY 2: 왜 그것이 그런 경우입니까?",
            "WHY 3: 왜 그것이 발생합니까?",
            "WHY 4: 왜 그것이 근본적인 이유입니까?",
            "WHY 5: 근본 원인은 무엇입니까?"
        ]
    },
    "triz": {
        "name": "TRIZ (40 Inventive Principles)",
        "category": "perspective",
        "steps": 5,
        "best_for": "technical_innovation",
        "questions": [
            "SEGMENTATION: 문제를 분할할 수 있습니까?",
            "ASYMMETRY: 비대칭으로 만들 수 있습니까?",
            "PRELIMINARY ACTION: 사전 조치를 취할 수 있습니까?",
            "UNIVERSALITY: 보편적으로 만들 수 있습니까?",
            "INVERSION: 반대로 할 수 있습니까?"
        ]
    },
    "design_thinking": {
        "name": "DESIGN THINKING",
        "category": "perspective",
        "steps": 5,
        "best_for": "user_centered",
        "questions": [
            "EMPATHIZE: 사용자가 진정으로 필요한 것은 무엇입니까?",
            "DEFINE: 핵심 문제는 무엇입니까?",
            "IDEATE: 가능한 모든 솔루션은 무엇입니까?",
            "PROTOTYPE: 빠르게 테스트할 수 있는 것은 무엇입니까?",
            "TEST: 어떤 피드백을 받았습니까?"
        ]
    },
    "lateral_thinking": {
        "name": "LATERAL THINKING",
        "category": "perspective",
        "steps": 3,
        "best_for": "breaking_patterns",
        "questions": [
            "어떤 가정에 도전할 수 있습니까?",
            "무작위 입력으로 무엇을 촉발할 수 있습니까?",
            "어떤 도발을 사용할 수 있습니까?"
        ]
    }
}

# FEEDBACK METHODS
FEEDBACK_METHODS = {
    "murder_board": {
        "name": "MURDER BOARD (Feedback)",
        "category": "feedback",
        "steps": 4,
        "best_for": "honest_feedback",
        "questions": [
            "누가 정직한 피드백을 줄 수 있습니까?",
            "아이디어의 강점은 무엇입니까?",
            "치명적 결함은 무엇입니까?",
            "어떻게 개선할 수 있습니까?"
        ]
    },
    "brainstorming": {
        "name": "BRAINSTORMING RULES",
        "category": "group",
        "steps": 4,
        "best_for": "group_ideation",
        "questions": [
            "양을 추구하고 있습니까?",
            "판단을 유보하고 있습니까?",
            "'예, 그리고...'를 말하고 있습니까?",
            "'하지만', '안돼', '못해'를 피하고 있습니까?"
        ]
    }
}

# STRATEGIC METHODS (Decision-Making & Business Strategy)
STRATEGIC_METHODS = {
    "decision_tree": {
        "name": "DECISION TREE",
        "category": "strategic",
        "steps": 5,
        "best_for": "complex_decisions",
        "questions": [
            "결정해야 할 핵심 질문은 무엇입니까?",
            "가능한 선택지(옵션)는 무엇입니까? (최소 2개 이상)",
            "각 선택지의 예상 결과는 무엇입니까?",
            "각 결과의 확률과 가치는 어떻습니까? (예: 성공확률 70%, 가치 높음)",
            "최적의 선택은 무엇이며 그 이유는 무엇입니까?"
        ]
    },
    "swot": {
        "name": "SWOT ANALYSIS",
        "category": "strategic",
        "steps": 5,
        "best_for": "strategic_planning",
        "questions": [
            "STRENGTHS: 우리의 강점은 무엇입니까? (내부 역량)",
            "WEAKNESSES: 우리의 약점은 무엇입니까? (내부 한계)",
            "OPPORTUNITIES: 외부 기회는 무엇입니까? (시장, 트렌드)",
            "THREATS: 외부 위협은 무엇입니까? (경쟁, 규제)",
            "전략: SO(강점-기회), ST(강점-위협), WO(약점-기회), WT(약점-위협) 전략은?"
        ]
    },
    "cost_benefit": {
        "name": "COST-BENEFIT ANALYSIS",
        "category": "strategic",
        "steps": 4,
        "best_for": "investment_decisions",
        "questions": [
            "고려 중인 결정/투자는 무엇입니까?",
            "예상되는 모든 비용은 무엇입니까? (직접비용, 기회비용, 시간, 위험)",
            "예상되는 모든 이익은 무엇입니까? (단기, 중기, 장기 가치)",
            "비용 대비 이익이 정당화됩니까? 최종 결정은?"
        ]
    },
    "bcg_matrix": {
        "name": "BCG MATRIX (Growth-Share)",
        "category": "strategic",
        "steps": 4,
        "best_for": "portfolio_analysis",
        "questions": [
            "분석할 제품/사업부는 무엇입니까?",
            "각각의 시장 성장률은 어떻습니까? (높음/낮음)",
            "각각의 상대적 시장 점유율은? (높음/낮음)",
            "분류 결과와 전략은? (Star-투자확대 / Cash Cow-수확 / Question Mark-선택적투자 / Dog-철수검토)"
        ]
    },
    "porter_five_forces": {
        "name": "PORTER'S FIVE FORCES",
        "category": "strategic",
        "steps": 6,
        "best_for": "industry_analysis",
        "questions": [
            "분석할 산업/시장은 무엇입니까?",
            "기존 경쟁자 간 경쟁 강도는? (많음/적음, 차별화 정도)",
            "신규 진입자의 위협은? (진입장벽 높음/낮음)",
            "대체재의 위협은? (대체 가능성 높음/낮음)",
            "공급자의 교섭력은? (높음/낮음, 전환비용)",
            "구매자의 교섭력은? (높음/낮음, 가격민감도)"
        ]
    },
    "decision_matrix": {
        "name": "DECISION MATRIX (Weighted Scoring)",
        "category": "strategic",
        "steps": 4,
        "best_for": "multi_criteria_decision",
        "questions": [
            "평가할 옵션들은 무엇입니까?",
            "중요한 평가 기준은 무엇입니까? (예: 비용, 시간, 효과, 위험)",
            "각 기준의 중요도는 몇 점입니까? (1-10점)",
            "각 옵션을 각 기준으로 평가하면? (점수 x 가중치 = 총점)"
        ]
    },
    "pros_cons_fixes": {
        "name": "PROS-CONS-FIXES",
        "category": "strategic",
        "steps": 3,
        "best_for": "option_evaluation",
        "questions": [
            "PROS: 이 선택의 장점/강점은 무엇입니까?",
            "CONS: 이 선택의 단점/위험은 무엇입니까?",
            "FIXES: 단점을 완화/해결할 방법은 무엇입니까?"
        ]
    },
    "pestel": {
        "name": "PESTEL ANALYSIS",
        "category": "strategic",
        "steps": 6,
        "best_for": "macro_environment",
        "questions": [
            "POLITICAL: 정치적 요인은? (정부정책, 규제, 정치안정성)",
            "ECONOMIC: 경제적 요인은? (경기, 환율, 인플레이션)",
            "SOCIAL: 사회문화적 요인은? (인구통계, 라이프스타일, 가치관)",
            "TECHNOLOGICAL: 기술적 요인은? (기술혁신, 자동화, R&D)",
            "ENVIRONMENTAL: 환경적 요인은? (지속가능성, 기후변화)",
            "LEGAL: 법적 요인은? (노동법, 안전규제, 지적재산권)"
        ]
    },
    "ansoff_matrix": {
        "name": "ANSOFF MATRIX (Growth Strategy)",
        "category": "strategic",
        "steps": 5,
        "best_for": "growth_strategy",
        "questions": [
            "현재 제품/서비스와 시장은 무엇입니까?",
            "MARKET PENETRATION: 기존 시장에서 점유율 확대 방법은?",
            "MARKET DEVELOPMENT: 새로운 시장/고객층 진출 방법은?",
            "PRODUCT DEVELOPMENT: 기존 고객 대상 신제품 개발 방법은?",
            "DIVERSIFICATION: 새로운 시장에 새로운 제품 진출 방법은? (위험도 가장 높음)"
        ]
    },
    "blue_ocean": {
        "name": "BLUE OCEAN STRATEGY",
        "category": "strategic",
        "steps": 4,
        "best_for": "market_creation",
        "questions": [
            "ELIMINATE: 업계 표준 중 제거할 요소는 무엇입니까?",
            "REDUCE: 업계 표준보다 대폭 줄일 요소는 무엇입니까?",
            "RAISE: 업계 표준보다 대폭 높일 요소는 무엇입니까?",
            "CREATE: 업계에 없는 새로 만들 요소는 무엇입니까?"
        ]
    },
    "okr": {
        "name": "OKR (Objectives & Key Results)",
        "category": "strategic",
        "steps": 3,
        "best_for": "goal_setting",
        "questions": [
            "OBJECTIVE: 달성하고자 하는 명확하고 도전적인 목표는 무엇입니까?",
            "KEY RESULTS: 목표 달성을 측정할 핵심 결과는 무엇입니까? (3-5개, 정량적)",
            "INITIATIVES: 핵심 결과를 달성하기 위한 구체적 실행방안은 무엇입니까?"
        ]
    },
    "value_chain": {
        "name": "VALUE CHAIN ANALYSIS",
        "category": "strategic",
        "steps": 5,
        "best_for": "competitive_advantage",
        "questions": [
            "주요 활동(Primary)은 무엇입니까? (생산, 마케팅, 판매, 물류, 서비스)",
            "지원 활동(Support)은 무엇입니까? (인사, 기술개발, 조달, 인프라)",
            "각 활동에서 창출되는 가치는 무엇입니까?",
            "비용 대비 가치가 높은 활동은 무엇입니까? (경쟁우위 원천)",
            "개선이 필요한 활동은 무엇입니까?"
        ]
    },
    "fishbone": {
        "name": "FISHBONE DIAGRAM (Ishikawa)",
        "category": "strategic",
        "steps": 6,
        "best_for": "causal_analysis",
        "questions": [
            "분석할 문제/결과는 무엇입니까?",
            "MAN (사람): 사람 요인은 무엇입니까? (역량, 교육, 동기)",
            "METHOD (방법): 프로세스/절차 요인은?",
            "MACHINE (기계): 기술/장비 요인은?",
            "MATERIAL (재료): 자원/투입 요인은?",
            "근본 원인은 무엇이며 해결방안은?"
        ]
    },
    "systems_thinking": {
        "name": "SYSTEMS THINKING (Causal Loop)",
        "category": "strategic",
        "steps": 5,
        "best_for": "systemic_understanding",
        "questions": [
            "시스템의 핵심 요소들은 무엇입니까?",
            "요소 간 인과관계는 무엇입니까? (A가 증가하면 B는?)",
            "강화 루프(Reinforcing Loop)는 무엇입니까? (선순환/악순환)",
            "균형 루프(Balancing Loop)는 무엇입니까? (안정화 메커니즘)",
            "레버리지 포인트(개입점)는 어디입니까?"
        ]
    },
    "second_order_thinking": {
        "name": "SECOND-ORDER THINKING",
        "category": "strategic",
        "steps": 4,
        "best_for": "long_term_consequences",
        "questions": [
            "직접적(1차) 결과는 무엇입니까?",
            "그다음(2차) 결과는 무엇입니까?",
            "장기적(3차 이상) 파급효과는 무엇입니까?",
            "의도하지 않은 결과는 무엇입니까?"
        ]
    },
    "scenario_planning": {
        "name": "SCENARIO PLANNING",
        "category": "strategic",
        "steps": 5,
        "best_for": "future_uncertainty",
        "questions": [
            "핵심 불확실성은 무엇입니까? (2가지 주요 변수)",
            "BEST CASE: 최선의 시나리오는 무엇입니까?",
            "WORST CASE: 최악의 시나리오는 무엇입니까?",
            "MOST LIKELY: 가장 가능성 높은 시나리오는?",
            "각 시나리오에 대한 대응전략은?"
        ]
    },
    "pre_mortem": {
        "name": "PRE-MORTEM (Prospective Hindsight)",
        "category": "strategic",
        "steps": 4,
        "best_for": "risk_prevention",
        "questions": [
            "1년 후, 이 프로젝트가 완전히 실패했다고 가정합니다. 무엇이 잘못되었습니까?",
            "실패의 징후는 무엇이었습니까?",
            "어떤 가정이 틀렸습니까?",
            "미리 예방할 수 있는 방법은?"
        ]
    },
    "mental_models": {
        "name": "MENTAL MODELS CHECK",
        "category": "strategic",
        "steps": 5,
        "best_for": "cognitive_biases",
        "questions": [
            "어떤 가정/믿음에 기반하고 있습니까?",
            "확증편향: 반대 증거를 충분히 고려했습니까?",
            "매몰비용: 과거 투자가 판단을 왜곡하고 있습니까?",
            "가용성 편향: 최근 경험에 과도하게 의존하고 있습니까?",
            "객관적으로 다시 평가하면 결론이 바뀝니까?"
        ]
    },
    "inversion": {
        "name": "INVERSION (Backwards Thinking)",
        "category": "strategic",
        "steps": 3,
        "best_for": "avoiding_failure",
        "questions": [
            "성공하려면 무엇을 해야 합니까?",
            "실패하려면 무엇을 해야 합니까? (반대로 생각)",
            "실패 방법을 피하면 성공 가능성이 높아집니까?"
        ]
    },
    "regret_minimization": {
        "name": "REGRET MINIMIZATION (Jeff Bezos)",
        "category": "strategic",
        "steps": 3,
        "best_for": "life_decisions",
        "questions": [
            "80세가 되었을 때, 이 결정을 후회할 가능성이 높습니까?",
            "시도하지 않은 것을 후회할까요, 시도한 것을 후회할까요?",
            "장기적 관점에서 어떤 선택이 후회를 최소화합니까?"
        ]
    },
    "opportunity_cost": {
        "name": "OPPORTUNITY COST ANALYSIS",
        "category": "strategic",
        "steps": 4,
        "best_for": "resource_allocation",
        "questions": [
            "이 선택에 투입할 자원(시간, 돈, 에너지)은 무엇입니까?",
            "같은 자원으로 할 수 있는 다른 선택지는 무엇입니까?",
            "포기하는 것의 가치는 얼마입니까?",
            "기회비용을 고려해도 이 선택이 최선입니까?"
        ]
    },
    "eisenhower_matrix": {
        "name": "EISENHOWER MATRIX (Urgent-Important)",
        "category": "strategic",
        "steps": 4,
        "best_for": "prioritization",
        "questions": [
            "긴급하고 중요한 일은? (즉시 실행)",
            "중요하지만 긴급하지 않은 일은? (계획 수립)",
            "긴급하지만 중요하지 않은 일은? (위임)",
            "긴급하지도 중요하지도 않은 일은? (제거)"
        ]
    }
}

# 모든 방법론 통합
ALL_METHODS = {
    **LINEAR_METHODS,
    **INTUITIVE_METHODS,
    **PERSPECTIVE_METHODS,
    **FEEDBACK_METHODS,
    **STRATEGIC_METHODS
}

# 방법론 카테고리 매핑
CATEGORY_MAP = {
    "analytical": ["five_whys", "phoenix", "force_field", "fishbone", "systems_thinking"],
    "creative": ["scamper", "random_stimulation", "analogies", "blue_ocean"],
    "strategic": [
        "decision_tree", "swot", "cost_benefit", "bcg_matrix",
        "porter_five_forces", "scenario_planning", "pre_mortem",
        "mental_models", "second_order_thinking", "okr"
    ],
    "technical": ["triz", "morphological", "attribute_listing", "value_chain"],
    "product": ["scamper", "fcb_grid", "morphological", "value_chain"],
    "organizational": ["force_field", "six_hats", "murder_board", "okr", "eisenhower_matrix"],
    "personal": [
        "intuition", "incubation", "dreamscape",
        "regret_minimization", "opportunity_cost", "mental_models"
    ]
}
