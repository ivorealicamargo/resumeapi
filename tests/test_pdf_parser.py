import pytest
from pdfminer.pdfparser import PDFSyntaxError
from resumeapi.parsers.pdf_parser import PDFParser


def test_pdf_parser_with_invalid_pdf():
    """Test that the parser raises an error for invalid PDF content."""
    invalid_pdf_content = b"Not a PDF content"
    with pytest.raises(
        PDFSyntaxError, match="No /Root object! - Is this really a PDF?"
    ):
        PDFParser.parse(invalid_pdf_content)


def test_pdf_parser_with_valid_pdf():
    """Test that the parser correctly extracts text from a valid PDF."""
    with open("tests/sample-resume.pdf", "rb") as pdf_file:
        valid_pdf_content = pdf_file.read()
    parsed_text = PDFParser.parse(valid_pdf_content)

    assert parsed_text.strip() != "", "PDF parser should extract text from valid PDFs"
    assert (
        "John Hui" in parsed_text
    ), "PDF parser should correctly extract the candidate's name"
    assert (
        "real-time reactive computing" in parsed_text
    ), "PDF parser should extract relevant professional intro"


def test_pdf_parser_with_empty_pdf():
    """Test that the parser raises an error for an empty PDF."""
    empty_pdf_content = b""
    with pytest.raises(
        PDFSyntaxError, match="No /Root object! - Is this really a PDF?"
    ):
        PDFParser.parse(empty_pdf_content)
