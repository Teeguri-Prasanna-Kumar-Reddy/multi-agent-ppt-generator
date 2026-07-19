from typing import Dict, Any
from tools.doc_loader import load_document


def parser_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts text from document and stores in state

    Expected state:
    {
        "input_type": "document",
        "document_path": "path/to/file"
    }
    """

    print("In Parser Agent")

    # Only run for document input
    if state.get("input_type") != "document":
        return state

    document_path = state.get("document_path")

    if not document_path:
        raise ValueError("document_path not found in state")

    try:
        # Load document text
        document_text = load_document(document_path)

        # store in state
        state["document_text"] = document_text

    except Exception as e:
        raise RuntimeError(f"Document parsing failed: {str(e)}")

    return state