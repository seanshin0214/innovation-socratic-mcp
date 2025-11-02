"""
Session Management
세션 상태를 압축하여 저장 (토큰 절약)
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict


@dataclass
class SessionState:
    """세션 상태 (압축 형식)"""
    session_id: str
    user_id: str
    problem: str  # 원본 문제
    category: str  # 분류된 카테고리
    method_id: str  # 선택된 방법론 ID
    method_name: str  # 방법론 이름
    current_step: int  # 현재 단계 (0-based)
    total_steps: int  # 총 단계 수
    answers: List[str]  # 사용자 답변들
    created_at: str
    updated_at: str
    is_completed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SessionState':
        """딕셔너리에서 생성"""
        return cls(**data)


class SessionManager:
    """세션 관리자"""

    def __init__(self, storage_dir: str = "data/user_sessions"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.current_session: Optional[SessionState] = None

    def create_session(
        self,
        user_id: str,
        problem: str,
        category: str,
        method_id: str,
        method_name: str,
        total_steps: int
    ) -> SessionState:
        """새 세션 생성"""
        # 세션 ID 생성 (해시)
        session_id = self._generate_session_id(user_id, problem)

        now = datetime.now().isoformat()

        session = SessionState(
            session_id=session_id,
            user_id=user_id,
            problem=problem,
            category=category,
            method_id=method_id,
            method_name=method_name,
            current_step=0,
            total_steps=total_steps,
            answers=[],
            created_at=now,
            updated_at=now,
            is_completed=False
        )

        self.current_session = session
        self._save_session(session)

        return session

    def add_answer(self, answer: str) -> bool:
        """답변 추가 및 단계 진행"""
        if not self.current_session:
            return False

        self.current_session.answers.append(answer)
        self.current_session.current_step += 1
        self.current_session.updated_at = datetime.now().isoformat()

        # 마지막 단계면 완료 표시
        if self.current_session.current_step >= self.current_session.total_steps:
            self.current_session.is_completed = True

        self._save_session(self.current_session)

        return True

    def get_current_session(self) -> Optional[SessionState]:
        """현재 세션 조회"""
        return self.current_session

    def load_session(self, session_id: str) -> Optional[SessionState]:
        """세션 로드"""
        session_file = self.storage_dir / f"{session_id}.json"

        if not session_file.exists():
            return None

        try:
            with open(session_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                session = SessionState.from_dict(data)
                self.current_session = session
                return session
        except Exception as e:
            print(f"세션 로드 실패: {e}")
            return None

    def end_session(self) -> Optional[Dict[str, Any]]:
        """세션 종료 및 요약 반환"""
        if not self.current_session:
            return None

        summary = self._generate_summary(self.current_session)

        # 세션 완료 표시
        self.current_session.is_completed = True
        self._save_session(self.current_session)

        # 현재 세션 초기화
        self.current_session = None

        return summary

    def _save_session(self, session: SessionState):
        """세션을 파일로 저장 (JSON 압축)"""
        session_file = self.storage_dir / f"{session.session_id}.json"

        try:
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session.to_dict(), f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"세션 저장 실패: {e}")

    def _generate_session_id(self, user_id: str, problem: str) -> str:
        """세션 ID 생성 (해시)"""
        timestamp = datetime.now().isoformat()
        content = f"{user_id}:{problem}:{timestamp}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]

    def _generate_summary(self, session: SessionState) -> Dict[str, Any]:
        """세션 요약 생성"""
        return {
            "session_id": session.session_id,
            "problem": session.problem,
            "method": session.method_name,
            "category": session.category,
            "total_questions": session.total_steps,
            "answers_provided": len(session.answers),
            "completed": session.is_completed,
            "insights": self._extract_insights(session)
        }

    def _extract_insights(self, session: SessionState) -> str:
        """간단한 인사이트 추출"""
        if session.method_id == "five_whys" and len(session.answers) >= 5:
            return f"근본 원인: {session.answers[-1]}"

        elif session.method_id == "scamper":
            techniques_used = []
            scamper_letters = ["S", "C", "A", "M", "P", "E", "R"]
            for i, answer in enumerate(session.answers):
                if answer.strip():
                    techniques_used.append(scamper_letters[i])

            return f"활용한 SCAMPER 기법: {', '.join(techniques_used)}"

        elif session.method_id == "six_hats":
            perspectives = ["사실", "감정", "위험", "기회", "창의", "프로세스"]
            explored = [perspectives[i] for i, ans in enumerate(session.answers) if ans.strip()]
            return f"탐색한 관점: {', '.join(explored)}"

        else:
            return f"{len(session.answers)}개의 질문에 답변하셨습니다."

    def get_next_question_context(self) -> Optional[Dict[str, Any]]:
        """다음 질문에 필요한 컨텍스트 반환"""
        if not self.current_session:
            return None

        return {
            "method_id": self.current_session.method_id,
            "current_step": self.current_session.current_step,
            "problem": self.current_session.problem,
            "previous_answers": self.current_session.answers
        }

    def format_session_summary(self, summary: Dict[str, Any]) -> str:
        """세션 요약을 사용자 친화적 형식으로 포맷팅"""
        output = "✅ 세션 완료\n\n"
        output += f"📌 문제: {summary['problem']}\n"
        output += f"🔧 사용 방법: {summary['method']}\n"
        output += f"📊 답변: {summary['answers_provided']}/{summary['total_questions']}\n\n"
        output += f"💡 인사이트:\n{summary['insights']}\n\n"
        output += "다음 단계:\n"
        output += "- 다른 방법론 시도: /method:[방법론]\n"
        output += "- 새 문제 분석: /think [문제]\n"
        output += "- 종료: /done"

        return output


# 싱글톤 인스턴스
session_manager = SessionManager()
