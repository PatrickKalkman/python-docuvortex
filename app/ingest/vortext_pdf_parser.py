import os
import re
from typing import Callable, Dict, List, Tuple

import langchain.docstore.document as docstore
import langchain.embeddings as embeddings
import langchain.text_splitter as splitter
import langchain.vectorstores as vectorstores
import pdfplumber
import PyPDF4


class VortexPdfParser:
    """A parser for extracting and cleaning text from PDF documents."""

    def __init__(self, pdf_file_path: str):
        """Initialise with the path to the PDF file."""
        if not os.path.isfile(pdf_file_path):
            raise FileNotFoundError(f"File not found: {pdf_file_path}")
        self.pdf_file_path = pdf_file_path

    def parse_pdf(self) -> Tuple[List[Tuple[int, str]], Dict[str, str]]:
        """Extract and return the pages and metadata from the PDF."""
        metadata = self.extract_metadata_from_pdf()
        pages = self.extract_pages_from_pdf()
        return pages, metadata

    def extract_metadata_from_pdf(self) -> Dict[str, str]:
        """Extract and return the metadata from the PDF."""
        with open(self.pdf_file_path, "rb") as pdf_file:
            reader = PyPDF4.PdfFileReader(pdf_file)
            metadata = reader.getDocumentInfo()
            return {
                "title": metadata.get("/Title", "").strip(),
                "author": metadata.get("/Author", "").strip(),
                "creation_date": metadata.get("/CreationDate", "").strip(),
            }

    def extract_pages_from_pdf(self) -> List[Tuple[int, str]]:
        """Extract and return the text of each page from the PDF."""
        with pdfplumber.open(self.pdf_file_path) as pdf:
            return [(i + 1, p.extract_text())
                    for i, p in enumerate(pdf.pages) if p.extract_text().strip()]

    def clean_text(self, pages: List[Tuple[int, str]],
                   cleaning_functions: List[Callable[[str], str]]) -> List[Tuple[int, str]]:
        """Apply the cleaning functions to the text of each page."""
        cleaned_pages = []
        for page_num, text in pages:
            for cleaning_function in cleaning_functions:
                text = cleaning_function(text)
            cleaned_pages.append((page_num, text))
        return cleaned_pages

    def merge_hyphenated_words(self, text: str) -> str:
        """Merge words in the text that have been split with a hyphen."""
        return re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    def fix_newlines(self, text: str) -> str:
        """Replace single newline characters in the text with spaces."""
        return re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    def remove_multiple_newlines(self, text: str) -> str:
        """Reduce multiple newline characters in the text to a single newline."""
        return re.sub(r"\n{2,}", "\n", text)

    def text_to_docs(self, text: List[Tuple[int, str]],
                     metadata: Dict[str, str]) -> List[docstore.Document]:
        """Split the text into chunks and return them as Documents."""
        doc_chunks = []

        for page_num, page in text:
            text_splitter = splitter.RecursiveCharacterTextSplitter(
                chunk_size=1000,
                separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
                chunk_overlap=200,
            )
            chunks = text_splitter.split_text(page)
            for i, chunk in enumerate(chunks):
                doc = docstore.Document(
                    page_content=chunk,
                    metadata={
                        "page_number": page_num,
                        "chunk": i,
                        "source": f"p{page_num}-{i}",
                        **metadata,
                    },
                )
                doc_chunks.append(doc)
        return doc_chunks
