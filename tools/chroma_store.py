from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings


class ChromaStore:
    """
    Handles:
    - chunking
    - embedding
    - storing
    - retrieval

    Uses FastEmbed (local, ONNX-based, no API key / no Ollama needed) for
    embeddings, while chat completions are handled separately by Groq.
    """

    def __init__(self, persist_directory: str = "chroma_db"):
        self.persist_directory = persist_directory

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100
        )

        # Loaded lazily on first use, so importing this module / starting the
        # server never blocks on a model download.
        self._embedding_model = None

        self.vector_store = None

    @property
    def embedding_model(self) -> FastEmbedEmbeddings:
        if self._embedding_model is None:
            self._embedding_model = FastEmbedEmbeddings()
        return self._embedding_model

    def create_vector_store(self, text: str):
        """
        Create vector DB from document text
        """
        chunks = self.text_splitter.split_text(text)

        self.vector_store = Chroma.from_texts(
            texts=chunks,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )

        self.vector_store.persist()

    def load_vector_store(self):
        """
        Load existing Chroma DB
        """
        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model,
        )

    def similarity_search(self, query: str, k: int = 5) -> List[str]:
        """
        Retrieve relevant chunks
        """
        if not self.vector_store:
            self.load_vector_store()

        docs = self.vector_store.similarity_search(query, k=k)

        return [doc.page_content for doc in docs]


# convenience functions
_store = ChromaStore()


def create_chroma_store(text: str):
    _store.create_vector_store(text)


def retrieve_chunks(query: str, k: int = 5) -> List[str]:
    return _store.similarity_search(query, k)
