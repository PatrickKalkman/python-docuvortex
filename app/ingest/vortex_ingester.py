from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from loguru import logger

from settings import COLLECTION_NAME, PERSIST_DIRECTORY
from .vortex_pdf_parser import VortexPdfParser


class VortexIngester:

    def __init__(self, vortex_pdf_parser: VortexPdfParser):
        self.vortext_pdf_parser = vortex_pdf_parser

    def ingest(self):
        chunks = self.vortext_pdf_parser.clean_text_to_docs()
        logger.info(f"Extracted {len(chunks)} chunks from PDF")
        embeddings = OpenAIEmbeddings()
        logger.info("Loaded embeddings")
        vector_store = Chroma.from_documents(
            chunks,
            embeddings,
            collection_name=COLLECTION_NAME,
            persist_directory=PERSIST_DIRECTORY,
        )

        logger.info("Created Chroma vector store")
        vector_store.persist()
        logger.info("Persisted Chroma vector store")
