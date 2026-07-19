from typing import Dict, Any, List
from llm.llm_provider import get_llm


def content_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Polishes slide content for final presentation quality
    """

    print("In Content Agent")

    llm = get_llm()

    slides = state.get("slides")

    if not slides:
        raise ValueError("slides not found in state")

    polished_slides = []

    for slide in slides:
        title = clean_text(slide["title"])
        bullets = "\n".join(slide["bullets"])

        if len(slide["bullets"]) <= 4 and all(len(b) < 80 for b in slide["bullets"]):
            polished_slides.append(slide)
            continue

        prompt = f"""
    You are a professional PowerPoint editor.

    Rewrite the bullets for clarity.

    Slide Title: {title}

    Bullets:
    {bullets}

    Rules:
    - Return bullet points only
    - Same number of bullets
    - Each bullet max 12 words
    - No numbering
    - No paragraph
    - No title
    - No extra explanation
    - One bullet per line
    """

        response = llm.invoke(prompt)

        refined_bullets = _parse_bullets(response.content)

        if not refined_bullets:
            refined_bullets = slide["bullets"]

        refined_bullets = refined_bullets[:4]

        polished_slides.append({
            "title": title,
            "bullets": refined_bullets
        })

    state["slides"] = polished_slides

    return state


def _parse_bullets(text: str) -> List[str]:
    lines = text.split("\n")
    bullets = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # remove numbering
        line = line.lstrip("0123456789. ")
        line = line.lstrip("-•* ")

        # remove noise
        line = clean_text(line)

        if line:
            bullets.append(line)

    return bullets

def clean_text(text):
    remove_words = [
        "Slide Title:",
        "Slide Content:",
        "Bullets:",
        "Content Suggestions:",
        "Conclusion and Next Steps:"
    ]

    for w in remove_words:
        text = text.replace(w, "")

    text = text.strip(" -•0123456789.")
    return text.strip()