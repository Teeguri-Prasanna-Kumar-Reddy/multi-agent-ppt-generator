import os
from typing import Optional

import fitz  # PyMuPDF
from docx import Document


class DocumentLoader:
    """
    Utility class to load different document types and extract text
    Supported formats: PDF, DOCX, TXT
    """

    @staticmethod
    def load(file_path: str) -> str:
        """
        Detect file type and load accordingly
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = file_path.split(".")[-1].lower()

        if extension == "pdf":
            return DocumentLoader._load_pdf(file_path)

        elif extension == "docx":
            return DocumentLoader._load_docx(file_path)

        elif extension == "txt":
            return DocumentLoader._load_txt(file_path)

        else:
            raise ValueError(f"Unsupported file format: {extension}")

    @staticmethod
    def _load_pdf(file_path: str) -> str:
        """Extract text from PDF using PyMuPDF"""
        text = []

        with fitz.open(file_path) as doc:
            for page in doc:
                text.append(page.get_text())

        return "\n".join(text)

    @staticmethod
    def _load_docx(file_path: str) -> str:
        """Extract text from DOCX"""
        doc = Document(file_path)
        text = [para.text for para in doc.paragraphs]
        return "\n".join(text)

    @staticmethod
    def _load_txt(file_path: str) -> str:
        """Extract text from TXT"""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()


def load_document(file_path: str) -> str:
    """
    Convenience function
    """
    return DocumentLoader.load(file_path)