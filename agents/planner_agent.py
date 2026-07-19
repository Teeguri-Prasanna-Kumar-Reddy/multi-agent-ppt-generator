from typing import Dict, Any, List
from llm.llm_provider import get_llm


def planner_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates slide outline for PPT
    """

    print("In Planner Agent")

    llm = get_llm()

    input_type = state.get("input_type")
    topic = state.get("topic")
    retrieved_chunks = state.get("retrieved_chunks", [])

    # Build context
    if input_type == "document" and retrieved_chunks:
        context = "\n\n".join(retrieved_chunks)
        prompt = f"""
You are an expert presentation planner.

Create a professional PowerPoint outline from the given document content.

Document Content:
{context}

Instructions:
- Generate 6 to 10 slide titles
- First slide must be title slide
- Keep titles short
- Output only bullet list

Example:
1. Introduction
2. Architecture
3. Workflow
"""

    else:
        prompt = f"""
YYou are an expert presentation planner.

Create a professional PowerPoint outline for the topic: {topic}

Rules:
- Only return slide titles
- No numbering
- No explanations
- Max 8 slides
- Use short titles (max 5 words)
- Keep topic consistent

Return as newline separated list.
"""

    response = llm.invoke(prompt)

    # outline = _parse_outline(response.content)
    outline = [
        line.strip("- ").strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    # print("STATE KEYS:", state.keys())

    state["outline"] = outline
    # print("STATE KEYS:", state.keys())

    return state


def _parse_outline(text: str) -> List[str]:
    """
    Convert LLM output to list
    """
    lines = text.split("\n")

    cleaned = []
    for line in lines:
        line = line.strip()

        if not line:
            continue

        # remove numbering
        if "." in line:
            line = line.split(".", 1)[1].strip()

        cleaned.append(line)

    return cleaned