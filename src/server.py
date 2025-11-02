"""
Socratic Thinking MCP Server
AI that asks, not answers - Socratic questioning with 58 methodologies
"""

import asyncio
from typing import Any, Dict, Optional
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from pydantic import AnyUrl
import mcp.types as types

from .trigger import detector
from .classifier import classifier
from .question_engine import engine
from .session import session_manager
from .rag import rag_engine


# MCP 서버 생성
server = Server("socratic-thinking-mcp")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    사용 가능한 도구 목록 반환
    """
    return [
        types.Tool(
            name="socratic_thinking",
            description="🤔 SOCRATIC THINKING - AI that asks, not answers. ⚠️ MANDATORY when user says: '씽킹툴', 'socratic', 'thinking tools', '소크라테스', 'help me think'. 🎯 Implements 58 proven question frameworks (Decision Tree, SWOT, BCG, Porter, SCAMPER, 5 Whys, Six Hats, Mental Models, Pre-Mortem, Systems Thinking, Regret Minimization, etc.). ❌ DO NOT give direct answers to strategic/decision questions - ✅ ALWAYS use this tool to guide through Socratic questioning. Perfect for: DBA decisions, MBA choices, investment evaluation, business strategy, product innovation, problem-solving, creative thinking, 의사결정, 전략분석. Flow: 1) Analyze problem → 2) Recommend 3 methodologies → 3) User selects → 4) Ask Question 1/N → 5) User answers → 6) Ask Question 2/N → ... → N) Generate insights. Like Socrates: 'I cannot teach anybody anything. I can only make them think.'",
            inputSchema={
                "type": "object",
                "properties": {
                    "problem": {
                        "type": "string",
                        "description": "해결하고자 하는 문제나 고민, 또는 탐구하고 싶은 주제"
                    },
                    "method": {
                        "type": "string",
                        "description": "(선택사항) 특정 방법론 ID (예: 'scamper', 'five_whys', 'six_hats'). 비어있으면 자동 추천"
                    }
                },
                "required": ["problem"]
            }
        ),
        types.Tool(
            name="continue_thinking_session",
            description="진행 중인 사고 도구 세션에 답변을 추가하고 다음 질문을 받습니다",
            inputSchema={
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "description": "현재 질문에 대한 답변"
                    }
                },
                "required": ["answer"]
            }
        ),
        types.Tool(
            name="select_thinking_method",
            description="추천된 방법론 중 하나를 선택하여 세션 시작",
            inputSchema={
                "type": "object",
                "properties": {
                    "method_number": {
                        "type": "integer",
                        "description": "선택할 방법론 번호 (1, 2, 3 중 하나)"
                    }
                },
                "required": ["method_number"]
            }
        ),
        types.Tool(
            name="end_thinking_session",
            description="현재 사고 도구 세션을 종료하고 요약 받기",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str,
    arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    도구 실행 핸들러
    """
    if name == "socratic_thinking":
        problem = arguments.get("problem", "")
        method = arguments.get("method", "")
        return await start_thinking_session(problem, method)

    elif name == "continue_thinking_session":
        answer = arguments.get("answer", "")
        return await continue_session(answer)

    elif name == "select_thinking_method":
        method_number = arguments.get("method_number", 1)
        return await select_method(method_number)

    elif name == "end_thinking_session":
        return await end_session()

    else:
        raise ValueError(f"Unknown tool: {name}")


async def start_thinking_session(problem: str, method: str = "") -> list[types.TextContent]:
    """
    새로운 사고 도구 세션 시작
    """
    detector.activate()

    # 문제 분류
    classification = classifier.classify(problem)

    # 특정 방법론 지정된 경우
    if method:
        # 방법론 ID로 직접 세션 시작
        from .methods.templates import ALL_METHODS
        if method in ALL_METHODS:
            method_data = ALL_METHODS[method]
            session = session_manager.create_session(
                user_id="default",
                problem=problem,
                category=classification["category"],
                method_id=method,
                method_name=method_data["name"],
                total_steps=method_data["steps"]
            )

            # 첫 번째 질문 생성
            question_data = engine.generate_question(method, 0)
            response_text = f"🤖 방법론: {method_data['name']}\n\n"
            response_text += engine.format_question_output(question_data)

            detector.current_session = {
                "problem": problem,
                "classification": classification,
                "state": "questioning"
            }
        else:
            response_text = f"❌ 알 수 없는 방법론: {method}\n\n"
            response_text = classifier.format_recommendations(classification)
            detector.current_session = {
                "problem": problem,
                "classification": classification,
                "state": "method_selection"
            }
    else:
        # 방법론 추천
        response_text = classifier.format_recommendations(classification)
        detector.current_session = {
            "problem": problem,
            "classification": classification,
            "state": "method_selection"
        }

    return [types.TextContent(type="text", text=response_text)]


async def select_method(method_number: int) -> list[types.TextContent]:
    """
    추천된 방법론 중 하나 선택
    """
    if not detector.current_session:
        return [types.TextContent(
            type="text",
            text="❌ 활성화된 세션이 없습니다. 먼저 socratic_thinking을 사용하세요."
        )]

    classification = detector.current_session["classification"]

    if method_number < 1 or method_number > len(classification["recommended_methods"]):
        return [types.TextContent(
            type="text",
            text=f"❌ 잘못된 선택입니다. 1-{len(classification['recommended_methods'])} 중 선택하세요."
        )]

    # 선택된 방법론
    selected_method = classification["recommended_methods"][method_number - 1]
    method_id = selected_method["id"]

    # 세션 생성
    session = session_manager.create_session(
        user_id="default",
        problem=detector.current_session["problem"],
        category=classification["category"],
        method_id=method_id,
        method_name=selected_method["name"],
        total_steps=selected_method["steps"]
    )

    # 첫 번째 질문 생성
    question_data = engine.generate_question(method_id, 0)
    response_text = engine.format_question_output(question_data)

    # 상태 업데이트
    detector.current_session["state"] = "questioning"

    return [types.TextContent(type="text", text=response_text)]


async def continue_session(answer: str) -> list[types.TextContent]:
    """
    현재 질문에 답변하고 다음 질문 받기
    """
    session = session_manager.get_current_session()

    if not session:
        return [types.TextContent(
            type="text",
            text="❌ 활성화된 세션이 없습니다."
        )]

    # 답변 저장 및 다음 단계로
    session_manager.add_answer(answer)

    # 세션 완료 확인
    if session.is_completed:
        summary = session_manager.end_session()
        response_text = session_manager.format_session_summary(summary)
        detector.deactivate()
    else:
        # 다음 질문
        question_data = engine.generate_question(
            session.method_id,
            session.current_step
        )
        response_text = engine.format_question_output(question_data)

    return [types.TextContent(type="text", text=response_text)]


async def end_session() -> list[types.TextContent]:
    """
    현재 세션 종료
    """
    if session_manager.current_session:
        summary = session_manager.end_session()
        response_text = session_manager.format_session_summary(summary)
    else:
        response_text = "세션이 종료되었습니다."

    detector.deactivate()

    return [types.TextContent(type="text", text=response_text)]


async def main():
    """서버 실행"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="socratic-thinking-mcp",
                server_version="2.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
