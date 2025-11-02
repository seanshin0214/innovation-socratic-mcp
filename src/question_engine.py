"""
Question Generation Engine
한 번에 하나의 질문만 생성 (토큰 최소화)
"""

from typing import Optional, Dict, Any
from .methods.templates import ALL_METHODS


class QuestionEngine:
    """단일 질문 생성 엔진"""

    def __init__(self):
        self.methods = ALL_METHODS

    def generate_question(
        self,
        method_id: str,
        step: int,
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        단일 질문 생성

        Args:
            method_id: 방법론 ID (예: "scamper", "five_whys")
            step: 현재 단계 (0-based index)
            context: 사용자 컨텍스트 (선택사항)

        Returns:
            {
                "method": str,           # 방법론 이름
                "category": str,         # 카테고리
                "question": str,         # 질문 텍스트
                "step": int,             # 현재 단계 (1-based)
                "total_steps": int,      # 총 단계 수
                "is_last": bool          # 마지막 질문 여부
            }
        """
        if method_id not in self.methods:
            return {
                "error": f"Unknown method: {method_id}",
                "available_methods": list(self.methods.keys())
            }

        method = self.methods[method_id]
        total_steps = method["steps"]

        # 단계 범위 확인
        if step < 0 or step >= total_steps:
            return {
                "error": f"Invalid step {step}. Must be 0-{total_steps-1}",
                "method": method["name"],
                "total_steps": total_steps
            }

        # 질문 추출
        question_text = method["questions"][step]

        # 컨텍스트 기반 질문 커스터마이징 (선택사항)
        if context:
            question_text = self._contextualize_question(
                question_text, context, method_id
            )

        return {
            "method": method["name"],
            "category": method["category"],
            "question": question_text,
            "step": step + 1,  # 1-based for display
            "total_steps": total_steps,
            "is_last": (step == total_steps - 1)
        }

    def _contextualize_question(
        self,
        question: str,
        context: str,
        method_id: str
    ) -> str:
        """
        컨텍스트에 따라 질문을 약간 조정
        (토큰 최소화를 위해 매우 간단하게)
        """
        # 기본적으로 그대로 반환
        # 필요시 간단한 템플릿 치환만 수행
        return question

    def get_method_info(self, method_id: str) -> Optional[Dict[str, Any]]:
        """방법론 메타데이터 조회"""
        if method_id not in self.methods:
            return None

        method = self.methods[method_id]
        return {
            "id": method_id,
            "name": method["name"],
            "category": method["category"],
            "steps": method["steps"],
            "best_for": method["best_for"]
        }

    def list_methods(
        self,
        category: Optional[str] = None
    ) -> list[Dict[str, Any]]:
        """
        방법론 목록 조회

        Args:
            category: 카테고리 필터 (선택사항)

        Returns:
            방법론 정보 리스트 (메타데이터만)
        """
        methods_list = []

        for method_id, method in self.methods.items():
            # 카테고리 필터
            if category and method["category"] != category:
                continue

            methods_list.append({
                "id": method_id,
                "name": method["name"],
                "category": method["category"],
                "steps": method["steps"],
                "best_for": method["best_for"]
            })

        return methods_list

    def format_question_output(self, question_data: Dict[str, Any]) -> str:
        """
        질문을 사용자 친화적 형식으로 포맷팅

        Format:
        [방법론: METHOD_NAME - CATEGORY]
        질문 X/Y: QUESTION_TEXT
        """
        if "error" in question_data:
            return f"❌ 오류: {question_data['error']}"

        method = question_data["method"]
        category = question_data["category"]
        question = question_data["question"]
        step = question_data["step"]
        total = question_data["total_steps"]

        output = f"[방법론: {method} - {category.upper()}]\n"
        output += f"질문 {step}/{total}: {question}"

        if question_data["is_last"]:
            output += "\n\n✅ 마지막 질문입니다."

        return output


# 싱글톤 인스턴스
engine = QuestionEngine()
