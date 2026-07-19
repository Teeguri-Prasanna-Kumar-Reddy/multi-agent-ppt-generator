from typing import Dict, Any
from tools.chroma_store import create_chroma_store, retrieve_chunks


def rag_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Performs RAG:
    - creates vector DB
    - retrieves relevant chunks

    Expected state:
    {
        "input_type": "document",
        "document_text": str,
        "topic": optional
    }
    """

    print("In RAG Agent")

    # Run only for document input
    if state.get("input_type") != "document":
        return state

    document_text = state.get("document_text")

    if not document_text:
        raise ValueError("document_text not found in state")

    try:
        # Step 1: create vector store
        create_chroma_store(document_text)

        # Step 2: decide retrieval query
        query = state.get("topic")

        if not query:
            # fallback query
            query = "Summarize the key topics of this document"

        # Step 3: retrieve chunks
        chunks = retrieve_chunks(query, k=5)

        # store in state
        state["retrieved_chunks"] = chunks

    except Exception as e:
        raise RuntimeError(f"RAG agent failed: {str(e)}")

    return state