from typing import Dict, Any, List
from llm.llm_provider import get_llm


def research_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Expands outline into detailed research content
    """

    print("In Research Agent")

    llm = get_llm()

    outline = state.get("outline", [])
    retrieved_chunks = state.get("retrieved_chunks", [])
    topic = state.get("topic")

    if not outline:
        raise ValueError("Outline not found in state")

    context = ""
    if retrieved_chunks:
        context = "\n\n".join(retrieved_chunks)

    research_content = []

    for slide_title in outline:
        prompt = f"""
You are an expert technical researcher.

Generate slide research content.

Topic: {topic}
Slide Title: {slide_title}

Context (optional):
{context}

Instructions:
- 3 to 4 bullet points only
- Each bullet max 12 words
- No paragraphs
- No numbering
- No intro text
- No "Slide Title" words
- Keep content concise
- Stay strictly within topic

Return bullet points only.
"""

        response = llm.invoke(prompt)

        # bullets = _parse_bullets(response.content)
        bullets = [
            line.strip("- ").strip()
            for line in response.content.split("\n")
            if line.strip()
        ]

        research_content.append(
            {
                "title": slide_title,
                "bullets": bullets[:4]
            }
        )

    state["research_content"] = research_content

    print("Research Agent --")
    print("STATE KEYS:", state.keys())

    return state


def _parse_bullets(text: str) -> List[str]:
    lines = text.split("\n")
    bullets = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # remove bullet characters
        line = line.lstrip("-•* ")

        bullets.append(line)

    return bullets