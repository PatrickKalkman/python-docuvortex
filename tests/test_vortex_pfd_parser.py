
from calendar import c
from loguru import logger
import pytest

import logging

from app.ingest.vortext_pdf_parser import VortexPdfParser

LOGGER = logging.getLogger(__name__)

@pytest.fixture
def pdf_file():
    return "./tests/test_docs/Cyber_Security_Threats_in_Cloud_Literature_Review.pdf"


def test_extract_metadata_from_pdf(pdf_file):
    parser = VortexPdfParser(pdf_file)
    metadata = parser.extract_metadata_from_pdf()
    assert (metadata['title'] == "Cyber Security Threats in Cloud: Literature Review")
    assert ('Almaiah' in metadata['author'])
    assert ('20210615' in metadata['creation_date'])


def test_extract_pages_from_pdf(pdf_file):
    parser = VortexPdfParser(pdf_file)
    pages = parser.extract_pages_from_pdf()
    assert (len(pages) == 8)
    assert ('collection of most\n352 studies are remained' in pages[0][1])


def test_parse_pdf(pdf_file):
    parser = VortexPdfParser(pdf_file)
    pages, metadata = parser.parse_pdf()
    assert (metadata['title'] == "Cyber Security Threats in Cloud: Literature Review")
    assert ('Almaiah' in metadata['author'])
    assert ('20210615' in metadata['creation_date'])
    assert (len(pages) == 8)
    assert ('collection of most\n352 studies are remained' in pages[0][1])


def test_clean_text(pdf_file):
    parser = VortexPdfParser(pdf_file)
    pages = parser.extract_pages_from_pdf()
    cleaning_functions = [parser.merge_hyphenated_words, parser.fix_newlines,
                          parser.remove_multiple_newlines]
    cleaned_pages = parser.clean_text(pages, cleaning_functions)
    assert (len(cleaned_pages) == 8)
    assert ('collection of most 352 studies are remained' in cleaned_pages[0][1])


def test_text_to_docs(pdf_file):
    parser = VortexPdfParser(pdf_file)
    pages = parser.extract_pages_from_pdf()
    metadata = parser.extract_metadata_from_pdf()
    docs = parser.text_to_docs(pages, metadata)
    assert ('In recent years, data has been expanding' in docs[0].page_content)
