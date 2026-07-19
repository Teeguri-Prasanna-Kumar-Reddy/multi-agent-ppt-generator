from typing import Dict, Any, List
from llm.llm_provider import get_llm


def structure_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts research content into slide-friendly structure
    """

    print("In Structure Agent")

    llm = get_llm()

    research_content = state.get("research_content")

    if not research_content:
        raise ValueError("research_content not found in state")

    structured_slides = []

    for slide in research_content:
        title = slide["title"]
        bullets = "\n".join(slide["bullets"])

        prompt = f"""
You are a presentation formatting expert.

Convert the following content into slide-friendly bullet points.

Slide Title: {title}

Content:
{bullets}

Instructions:
- Keep maximum 5 bullets
- Short sentences
- Professional tone
- No numbering
- No title
"""

        response = llm.invoke(prompt)

        formatted_bullets = _parse_bullets(response.content)

        structured_slides.append(
            {
                "title": title,
                "bullets": formatted_bullets
            }
        )

    state["slides"] = structured_slides

    return state


def _parse_bullets(text: str) -> List[str]:
    lines = text.split("\n")
    bullets = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        line = line.lstrip("-•* ")

        bullets.append(line)

    return bullets[:5]