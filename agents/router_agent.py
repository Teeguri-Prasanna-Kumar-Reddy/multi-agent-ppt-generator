from typing import Dict, Any


def router_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Determines input type:
    - topic
    - text
    - document

    Expected incoming state:
    {
        "topic": str (optional),
        "document_path": str (optional),
        "raw_text": str (optional)
    }
    """

    print("In Router Agent")

    topic = state.get("topic")
    document_path = state.get("document_path")
    raw_text = state.get("raw_text")

    # Decide input type
    if document_path:
        input_type = "document"

    elif raw_text:
        input_type = "text"

    elif topic:
        input_type = "topic"

    else:
        raise ValueError("No valid input provided")

    # Update state
    state["input_type"] = input_type


    return state