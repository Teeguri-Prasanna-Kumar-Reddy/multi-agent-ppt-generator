import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:  # pragma: no cover - optional dependency
    ChatGoogleGenerativeAI = None

try:
    from langchain_groq import ChatGroq
except ImportError:  # pragma: no cover - optional dependency
    ChatGroq = None


# Load environment variables
load_dotenv()


class LLMProvider:
    """Provides an LLM instance with Groq as the primary option."""

    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.groq_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")

    def get_groq(self) -> Optional[BaseChatModel]:
        """Return Groq LLM if the API key is available."""
        if not self.groq_api_key or ChatGroq is None:
            return None

        try:
            return ChatGroq(
                model=self.groq_model,
                groq_api_key=self.groq_api_key,
                temperature=0.3,
            )
        except Exception as exc:
            print(f"Groq initialization failed: {exc}")
            return None

    def get_gemini(self) -> Optional[BaseChatModel]:
        """Return Gemini LLM if the API key is available."""
        if not self.gemini_api_key or ChatGoogleGenerativeAI is None:
            return None

        try:
            return ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key=self.gemini_api_key,
                temperature=0.3,
            )
        except Exception as exc:
            print(f"Gemini initialization failed: {exc}")
            return None

    def get_llm(self) -> BaseChatModel:
        """Return Groq first, then Gemini."""
        groq = self.get_groq()
        if groq:
            print("Using Groq LLM")
            return groq

        gemini = self.get_gemini()
        if gemini:
            print("Using Gemini LLM")
            return gemini

        raise RuntimeError(
            "No LLM provider is configured. Set GROQ_API_KEY or GEMINI_API_KEY."
        )


# Singleton instance
_llm_provider = LLMProvider()


def get_llm() -> BaseChatModel:
    """Global access function."""
    return _llm_provider.get_llm()
