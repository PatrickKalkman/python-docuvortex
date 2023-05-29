import pytest

from app.ingest.vortex_pdf_parser import VortexPdfParser


@pytest.fixture
def pdf_file():
    return "./tests/test_docs/Cyber_Security_Threats_in_Cloud_Literature_Review.pdf"


pdf_test_cases = [
    ("./tests/test_docs/Cyber_Security_Threats_in_Cloud_Literature_Review.pdf",
     "Cyber Security Threats in Cloud: Literature Review", "Almaiah", "2021-06-15"),
    ("./tests/test_docs/mirkovic_benzel_teachingcybersecurity.pdf",
     "", "", ""),
    ("./tests/test_docs/w28196.pdf",
     "Cybersecurity Risk", "", "")
]


@pytest.mark.parametrize("pdf_file,title,author,creation_date", pdf_test_cases)
def test_extract_metadata_from_pdf(pdf_file, title, author, creation_date):
    parser = VortexPdfParser()
    parser.set_pdf_file_path(pdf_file)
    metadata = parser.extract_metadata_from_pdf()
    assert metadata['title'] == title
    assert author in metadata['author']
    assert creation_date in metadata['creation_date']


def test_extract_pages_from_pdf(pdf_file):
    parser = VortexPdfParser()
    parser.set_pdf_file_path(pdf_file)
    pages = parser.extract_pages_from_pdf()
    assert (len(pages) == 8)
    assert ('collection of most\n352 studies are remained' in pages[0][1])


def test_parse_pdf(pdf_file):
    parser = VortexPdfParser()
    parser.set_pdf_file_path(pdf_file)
    pages, metadata = parser.parse_pdf()
    assert (metadata['title'] == "Cyber Security Threats in Cloud: Literature Review")
    assert ('Almaiah' in metadata['author'])
    assert ('2021-06-15' in metadata['creation_date'])
    assert (len(pages) == 8)
    assert ('collection of most\n352 studies are remained' in pages[0][1])


def test_clean_text(pdf_file):
    parser = VortexPdfParser()
    parser.set_pdf_file_path(pdf_file)
    pages = parser.extract_pages_from_pdf()
    cleaning_functions = [parser.merge_hyphenated_words, parser.fix_newlines,
                          parser.remove_multiple_newlines]
    cleaned_pages = parser.clean_text(pages, cleaning_functions)
    assert (len(cleaned_pages) == 8)
    assert ('collection of most 352 studies are remained' in cleaned_pages[0][1])


def test_text_to_docs(pdf_file):
    parser = VortexPdfParser()
    parser.set_pdf_file_path(pdf_file)
    pages = parser.extract_pages_from_pdf()
    metadata = parser.extract_metadata_from_pdf()
    docs = parser.text_to_docs(pages, metadata)
    assert ('In recent years, data has been expanding' in docs[0].page_content)
