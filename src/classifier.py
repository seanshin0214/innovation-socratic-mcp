"""
Problem Classifier
문제 유형 분석 및 방법론 추천 (AI 또는 규칙 기반)
"""

from typing import List, Dict, Any
from .methods.templates import ALL_METHODS, CATEGORY_MAP


class ProblemClassifier:
    """문제 분류 및 방법론 추천"""

    # 키워드 기반 분류 규칙
    KEYWORD_RULES = {
        "analytical": [
            "왜", "이유", "원인", "분석", "why", "cause", "reason",
            "근본", "root", "문제", "problem", "인과관계", "causal"
        ],
        "creative": [
            "창의적", "혁신", "새로운", "아이디어", "creative", "innovative",
            "idea", "brainstorm", "상상", "imagine"
        ],
        "strategic": [
            "전략", "미래", "계획", "목표", "strategy", "future", "plan",
            "비전", "vision", "장기", "long-term", "의사결정", "결정",
            "선택", "decision", "choice", "투자", "investment", "ROI",
            "BCG", "SWOT", "포터", "Porter", "경쟁", "competitive",
            "시장분석", "market analysis", "포트폴리오", "portfolio",
            "사업전략", "business strategy", "성장전략", "growth",
            "인수합병", "M&A", "리스크", "risk", "기회비용", "opportunity cost",
            "시나리오", "scenario", "불확실성", "uncertainty"
        ],
        "technical": [
            "기술", "제품", "시스템", "technical", "product", "system",
            "개발", "develop", "설계", "design"
        ],
        "product": [
            "제품", "서비스", "개선", "product", "service", "improve",
            "고객", "customer", "사용자", "user"
        ],
        "organizational": [
            "조직", "팀", "프로세스", "organization", "team", "process",
            "생산성", "productivity", "효율", "efficiency"
        ],
        "personal": [
            "개인", "자기", "personal", "self", "성장", "growth",
            "인생", "life", "경력", "career", "후회", "regret"
        ]
    }

    def classify(self, problem_description: str) -> Dict[str, Any]:
        """
        문제 분류 및 방법론 추천

        Args:
            problem_description: 사용자의 문제 설명

        Returns:
            {
                "category": str,
                "confidence": float,
                "recommended_methods": List[Dict],
                "reasoning": str
            }
        """
        # 키워드 기반 분류
        category_scores = self._score_categories(problem_description)

        # 가장 높은 점수의 카테고리 선택
        best_category = max(category_scores, key=category_scores.get)
        confidence = category_scores[best_category] / sum(category_scores.values()) \
            if sum(category_scores.values()) > 0 else 0.0

        # 추천 방법론 선택
        recommended_methods = self._get_recommended_methods(
            best_category,
            problem_description
        )

        return {
            "category": best_category,
            "confidence": confidence,
            "recommended_methods": recommended_methods[:3],  # 상위 3개만
            "reasoning": self._generate_reasoning(
                best_category,
                problem_description,
                confidence
            )
        }

    def _score_categories(self, text: str) -> Dict[str, float]:
        """키워드 매칭으로 카테고리별 점수 계산"""
        text_lower = text.lower()
        scores = {category: 0.0 for category in self.KEYWORD_RULES}

        for category, keywords in self.KEYWORD_RULES.items():
            for keyword in keywords:
                if keyword in text_lower:
                    scores[category] += 1.0

        return scores

    def _get_recommended_methods(
        self,
        category: str,
        problem_description: str
    ) -> List[Dict[str, Any]]:
        """카테고리에 맞는 방법론 추천"""
        # 카테고리에 해당하는 방법론 ID 가져오기
        method_ids = CATEGORY_MAP.get(category, [])

        # 추가로 문제 특성에 따른 방법론 추가
        additional_methods = self._get_additional_methods(problem_description)

        # 중복 제거하고 합치기
        all_method_ids = list(set(method_ids + additional_methods))

        # 방법론 정보 구성
        recommendations = []
        for method_id in all_method_ids[:5]:  # 최대 5개
            if method_id in ALL_METHODS:
                method = ALL_METHODS[method_id]
                recommendations.append({
                    "id": method_id,
                    "name": method["name"],
                    "category": method["category"],
                    "best_for": method["best_for"],
                    "steps": method["steps"]
                })

        return recommendations

    def _get_additional_methods(self, text: str) -> List[str]:
        """문제 특성에 따른 추가 방법론"""
        text_lower = text.lower()
        additional = []

        # "왜"가 많으면 5 Whys 추천
        if text_lower.count("왜") >= 2 or text_lower.count("why") >= 2:
            additional.append("five_whys")

        # "제품" 관련이면 SCAMPER 추천
        if "제품" in text_lower or "product" in text_lower:
            additional.append("scamper")

        # "미래" 관련이면 Scenario Planning 추천
        if "미래" in text_lower or "future" in text_lower or "시나리오" in text_lower:
            additional.append("scenario_planning")

        # "팀", "조직" 관련이면 Six Hats 추천
        if "팀" in text_lower or "조직" in text_lower or \
           "team" in text_lower or "organization" in text_lower:
            additional.append("six_hats")

        # 전략/의사결정 관련
        if "결정" in text_lower or "decision" in text_lower or "선택" in text_lower or "choice" in text_lower:
            additional.append("decision_tree")

        if "swot" in text_lower:
            additional.append("swot")

        if "bcg" in text_lower:
            additional.append("bcg_matrix")

        if "포터" in text_lower or "porter" in text_lower or "경쟁" in text_lower or "competitive" in text_lower:
            additional.append("porter_five_forces")

        # 인과관계 분석
        if "원인" in text_lower or "cause" in text_lower or "인과" in text_lower:
            additional.append("fishbone")
            additional.append("systems_thinking")

        # 투자/비용 관련
        if "투자" in text_lower or "investment" in text_lower or "비용" in text_lower or "cost" in text_lower:
            additional.append("cost_benefit")

        # 리스크/실패 관련
        if "리스크" in text_lower or "risk" in text_lower or "실패" in text_lower or "fail" in text_lower:
            additional.append("pre_mortem")

        # 후회/인생 관련
        if "후회" in text_lower or "regret" in text_lower or "인생" in text_lower or "life" in text_lower:
            additional.append("regret_minimization")

        # 편향/객관성 관련
        if "편향" in text_lower or "bias" in text_lower or "객관" in text_lower:
            additional.append("mental_models")

        return additional

    def _generate_reasoning(
        self,
        category: str,
        problem: str,
        confidence: float
    ) -> str:
        """추천 이유 생성"""
        category_names = {
            "analytical": "분석적 접근",
            "creative": "창의적 사고",
            "strategic": "전략적 계획",
            "technical": "기술적 혁신",
            "product": "제품 개선",
            "organizational": "조직 개선",
            "personal": "개인 성장"
        }

        category_name = category_names.get(category, category)
        confidence_level = "높음" if confidence > 0.5 else \
                          "중간" if confidence > 0.3 else "낮음"

        return f"귀하의 문제는 '{category_name}'이 필요합니다. " \
               f"(신뢰도: {confidence_level})"

    def format_recommendations(
        self,
        classification: Dict[str, Any]
    ) -> str:
        """추천 결과를 사용자 친화적 형식으로 포맷팅"""
        output = "🎯 문제 분석 완료\n\n"
        output += f"분류: {classification['reasoning']}\n\n"
        output += "📋 추천 방법론:\n"

        for i, method in enumerate(classification["recommended_methods"], 1):
            output += f"{i}. {method['name']}\n"
            output += f"   - 적합한 상황: {method['best_for']}\n"
            output += f"   - 단계 수: {method['steps']}\n"

        output += "\n방법 선택: /{번호} (예: /1, /2, /3) 또는 /auto (AI 자동 선택)"

        return output


# 싱글톤 인스턴스
classifier = ProblemClassifier()
