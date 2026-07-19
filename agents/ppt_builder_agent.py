from typing import Dict, Any
from tools.ppt_generator import generate_ppt


def ppt_builder_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Builds PowerPoint from slides
    """

    print("In PPT Builder Agent")

    slides = state.get("slides")

    if not slides:
        raise ValueError("slides not found in state")

    try:
        # Generate PPT
        ppt_path = generate_ppt(slides)

        # store path
        state["ppt_path"] = ppt_path

    except Exception as e:
        raise RuntimeError(f"PPT generation failed: {str(e)}")

    return state