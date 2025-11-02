"""
Thinking Tools MCP 테스트 스크립트
"""

import asyncio
import sys
import io

# Windows 콘솔 인코딩 문제 해결
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
from src.trigger import detector
from src.classifier import classifier
from src.question_engine import engine
from src.session import session_manager


async def test_basic_flow():
    """기본 흐름 테스트"""
    print("=== Thinking Tools MCP 테스트 ===\n")

    # 1. 트리거 감지 테스트
    print("1. 트리거 감지 테스트")
    messages = [
        "안녕하세요",  # 트리거 없음
        "팀 생산성이 낮아요 /think",  # 활성화
        "/1",  # 방법론 선택
        "회의가 너무 많아요",  # 답변
    ]

    for msg in messages:
        result = detector.detect(msg)
        print(f"  메시지: '{msg}'")
        print(f"  → 트리거: {result['triggered']}, 액션: {result['action']}\n")

    # 2. 문제 분류 테스트
    print("\n2. 문제 분류 테스트")
    problems = [
        "팀 생산성이 낮아요",
        "새로운 제품 아이디어가 필요해요",
        "왜 매출이 떨어지는지 모르겠어요",
    ]

    for problem in problems:
        classification = classifier.classify(problem)
        print(f"  문제: {problem}")
        print(f"  → 카테고리: {classification['category']}")
        print(f"  → 추천: {[m['name'] for m in classification['recommended_methods'][:2]]}\n")

    # 3. 질문 생성 테스트
    print("\n3. 질문 생성 테스트")
    methods_to_test = ["five_whys", "scamper", "six_hats"]

    for method_id in methods_to_test:
        print(f"\n  [{method_id.upper()}]")
        for step in range(min(3, engine.methods[method_id]["steps"])):
            question = engine.generate_question(method_id, step)
            output = engine.format_question_output(question)
            print(f"  {output}\n")

    # 4. 세션 관리 테스트
    print("\n4. 세션 관리 테스트")
    session = session_manager.create_session(
        user_id="test_user",
        problem="팀 생산성 개선",
        category="organizational",
        method_id="five_whys",
        method_name="5 WHYS",
        total_steps=5
    )
    print(f"  세션 생성: {session.session_id}")

    # 답변 추가
    answers = ["회의가 많아서", "결정을 못해서", "권한이 불명확해서"]
    for answer in answers:
        session_manager.add_answer(answer)
        print(f"  답변 추가: '{answer}' (단계: {session.current_step}/{session.total_steps})")

    # 세션 종료
    summary = session_manager.end_session()
    print(f"\n  세션 요약:\n{session_manager.format_session_summary(summary)}")

    print("\n=== 테스트 완료 ===")


async def test_all_methods():
    """모든 방법론 테스트"""
    print("\n=== 전체 방법론 테스트 ===\n")

    from src.methods.templates import ALL_METHODS

    for method_id, method in ALL_METHODS.items():
        print(f"✓ {method['name']}")
        print(f"  - 카테고리: {method['category']}")
        print(f"  - 단계 수: {method['steps']}")
        print(f"  - 최적: {method['best_for']}")

        # 첫 번째 질문만 테스트
        question = engine.generate_question(method_id, 0)
        if "error" not in question:
            print(f"  - 첫 질문: {question['question'][:50]}...")
        print()

    print(f"총 {len(ALL_METHODS)}개 방법론 테스트 완료")


async def interactive_demo():
    """대화형 데모"""
    print("\n=== 대화형 데모 ===")
    print("종료하려면 'exit' 입력\n")

    while True:
        user_input = input("사용자: ")

        if user_input.lower() == 'exit':
            break

        # 트리거 감지
        result = detector.detect(user_input)

        if not result["triggered"]:
            print("MCP: [잠수함 모드 - 조용히 대기]\n")
            continue

        action = result["action"]

        if action == "activate":
            detector.activate()
            problem = result["message"]

            # 분류
            classification = classifier.classify(problem)
            response = classifier.format_recommendations(classification)
            print(f"MCP:\n{response}\n")

            # 세션 정보 저장
            detector.current_session = {
                "problem": problem,
                "classification": classification,
                "state": "method_selection"
            }

        elif action == "select_number" and detector.current_session:
            method_num = result["value"]
            classification = detector.current_session["classification"]

            if 1 <= method_num <= len(classification["recommended_methods"]):
                selected = classification["recommended_methods"][method_num - 1]

                # 세션 생성
                session = session_manager.create_session(
                    user_id="demo_user",
                    problem=detector.current_session["problem"],
                    category=classification["category"],
                    method_id=selected["id"],
                    method_name=selected["name"],
                    total_steps=selected["steps"]
                )

                # 첫 질문
                question = engine.generate_question(selected["id"], 0)
                output = engine.format_question_output(question)
                print(f"MCP:\n{output}\n")

                detector.current_session["state"] = "questioning"

        elif action == "answer":
            session = session_manager.get_current_session()

            if session:
                session_manager.add_answer(user_input)

                if session.is_completed:
                    summary = session_manager.end_session()
                    print(f"MCP:\n{session_manager.format_session_summary(summary)}\n")
                    detector.deactivate()
                else:
                    question = engine.generate_question(session.method_id, session.current_step)
                    output = engine.format_question_output(question)
                    print(f"MCP:\n{output}\n")

        elif action == "help":
            print(f"MCP:\n{detector.get_help_message()}\n")

        elif action == "done":
            if session_manager.current_session:
                summary = session_manager.end_session()
                print(f"MCP:\n{session_manager.format_session_summary(summary)}\n")

            detector.deactivate()
            print("MCP: [잠수함 모드로 복귀]\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        asyncio.run(interactive_demo())
    elif len(sys.argv) > 1 and sys.argv[1] == "all":
        asyncio.run(test_all_methods())
    else:
        asyncio.run(test_basic_flow())
