"""
Submarine Mode & Trigger Detection
잠수함 모드: 대부분의 시간 동안 조용히 대기
트리거 감지 시에만 활성화
"""

from typing import Optional, Dict, Any
import re


class TriggerDetector:
    """트리거 감지 및 명령 파싱"""

    # 활성화 트리거
    ACTIVATION_TRIGGERS = [
        "/think",
        "/innovate",
        "/question",
        "/창의적",
        "/혁신",
        "/질문",
        "/문제해결",
        "/씽킹툴",
        "씽킹툴",
        "thinking-tools",
        "thinking tools"
    ]

    # 방법론 선택 트리거
    METHOD_TRIGGER = "/method:"

    # 자동 모드
    AUTO_TRIGGER = "/auto"

    # RAG 활성화
    RAG_TRIGGER = "/rag"

    # 종료
    DONE_TRIGGER = "/done"

    # 도움말
    HELP_TRIGGER = "/help"

    def __init__(self):
        self.is_active = False
        self.current_session = None

    def detect(self, message: str) -> Dict[str, Any]:
        """
        메시지 분석 및 트리거 감지

        Returns:
            {
                "triggered": bool,
                "action": str,  # "activate", "method", "auto", "rag", "done", "help", None
                "value": Any,   # 추가 파라미터
                "message": str  # 처리된 메시지
            }
        """
        message_lower = message.lower().strip()

        # 활성화 트리거 감지
        for trigger in self.ACTIVATION_TRIGGERS:
            if trigger in message_lower:
                # 트리거 제거한 실제 메시지 추출
                clean_message = message.replace(trigger, "").strip()
                return {
                    "triggered": True,
                    "action": "activate",
                    "value": None,
                    "message": clean_message if clean_message else "도전과제를 설명해주세요."
                }

        # 방법론 선택 트리거
        if self.METHOD_TRIGGER in message_lower:
            method_match = re.search(r'/method:(\w+)', message_lower)
            if method_match:
                method_name = method_match.group(1)
                return {
                    "triggered": True,
                    "action": "method",
                    "value": method_name,
                    "message": message
                }

        # 숫자로 방법론 선택 (/1, /2, /3)
        number_match = re.search(r'/(\d+)', message)
        if number_match:
            method_number = int(number_match.group(1))
            return {
                "triggered": True,
                "action": "select_number",
                "value": method_number,
                "message": message
            }

        # 자동 모드
        if self.AUTO_TRIGGER in message_lower:
            return {
                "triggered": True,
                "action": "auto",
                "value": None,
                "message": message
            }

        # RAG 활성화
        if self.RAG_TRIGGER in message_lower:
            return {
                "triggered": True,
                "action": "rag",
                "value": None,
                "message": message.replace(self.RAG_TRIGGER, "").strip()
            }

        # 종료
        if self.DONE_TRIGGER in message_lower:
            return {
                "triggered": True,
                "action": "done",
                "value": None,
                "message": message
            }

        # 도움말
        if self.HELP_TRIGGER in message_lower:
            return {
                "triggered": True,
                "action": "help",
                "value": None,
                "message": message
            }

        # 트리거 없음 - 잠수함 모드 유지
        # 활성화된 세션이 있으면 답변으로 처리
        if self.is_active:
            return {
                "triggered": True,
                "action": "answer",
                "value": None,
                "message": message
            }

        return {
            "triggered": False,
            "action": None,
            "value": None,
            "message": message
        }

    def activate(self):
        """세션 활성화"""
        self.is_active = True

    def deactivate(self):
        """세션 비활성화 (잠수함 모드로 복귀)"""
        self.is_active = False
        self.current_session = None

    def get_help_message(self) -> str:
        """도움말 메시지 반환"""
        return """
🤖 Innovator's Thinking Tools MCP

== 활성화 ==
씽킹툴 [문제]      - 사고 도구 시작
/think [문제]      - 사고 도구 시작
/innovate [문제]   - 혁신 도구 시작
/question [문제]   - 질문 생성 시작

== 방법론 선택 ==
/1, /2, /3         - 추천된 방법론 선택
/method:scamper    - 특정 방법론 선택
/auto              - AI 자동 선택

== 기타 ==
/rag               - 문서 분석 모드
/done              - 세션 종료
/help              - 이 도움말

== 사용 예시 ==
"씽킹툴 사용해서 팀 생산성 문제 분석해줘"
"하버드 석사를 해야 할지 고민이에요 /think"
→ 문제 분석 후 방법론 추천
        """.strip()


# 싱글톤 인스턴스
detector = TriggerDetector()
