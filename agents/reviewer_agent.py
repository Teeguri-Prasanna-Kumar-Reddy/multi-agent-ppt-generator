import os
from typing import Dict, Any, List


def reviewer_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Final QA agent:
    - validates slides
    - checks PPT generation
    - cleans empty slides
    """

    print("In Reviewer Agent")

    slides = state.get("slides", [])
    ppt_path = state.get("ppt_path")

    if not slides:
        raise ValueError("No slides found for review")

    # Remove empty slides
    cleaned_slides = _remove_empty_slides(slides)

    state["slides"] = cleaned_slides

    # Validate PPT file
    if not ppt_path:
        raise ValueError("ppt_path missing")

    if not os.path.exists(ppt_path):
        raise FileNotFoundError(f"PPT file not found: {ppt_path}")

    # Add review metadata
    state["review"] = {
        "status": "approved",
        "total_slides": len(cleaned_slides),
        "ppt_path": ppt_path
    }

    return state


def _remove_empty_slides(slides: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Remove slides with no bullets
    """
    cleaned = []

    for slide in slides:
        bullets = slide.get("bullets", [])

        if bullets and len(bullets) > 0:
            cleaned.append(slide)

    return cleaned