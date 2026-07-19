from typing import Dict, Any, List


def design_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Applies simple design rules to slides
    """

    print("In Design Agent")

    slides = state.get("slides")

    if not slides:
        raise ValueError("slides not found in state")

    designed_slides = []

    for slide in slides:
        title = _format_title(slide["title"])
        bullets = _format_bullets(slide["bullets"])

        designed_slides.append(
            {
                "title": title,
                "bullets": bullets,
                "layout": "title_content",
                "theme": "modern"
            }
        )

    state["slides"] = designed_slides
    state["design"] = {
        "theme": "modern",
        "font": "default",
        "layout": "title_content"
    }

    return state


def _format_title(title: str) -> str:
    """
    Capitalize title properly
    """
    return title.strip().title()


def _format_bullets(bullets: List[str]) -> List[str]:
    """
    Apply bullet formatting rules
    """
    formatted = []

    for bullet in bullets:
        bullet = bullet.strip()

        # limit length
        if len(bullet) > 120:
            bullet = bullet[:117] + "..."

        # capitalize first letter
        bullet = bullet[0].upper() + bullet[1:] if bullet else bullet

        formatted.append(bullet)

    # max 5 bullets
    return formatted[:5]