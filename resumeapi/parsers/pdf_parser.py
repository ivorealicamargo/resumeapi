from langchain_community.document_loaders.parsers.pdf import PDFMinerParser
from langchain.document_loaders import Blob


class PDFParser:
    """
    A class for handling PDF parsing using the PDFMiner parser.

    This class provides functionality to extract text content from PDF files, converting
    the binary content of a PDF into a readable string.
    """

    @staticmethod
    def parse(content: bytes) -> str:
        """
        Parse the binary content of a PDF and return the extracted text.

        Args:
            content (bytes): The binary content of the PDF file.

        Returns:
            str: The extracted text content from the PDF. Returns an empty string if no
                 text is extracted or the PDF is empty.
        """
        blob = Blob(data=content)
        documents = list(PDFMinerParser().lazy_parse(blob))
        return documents[0].page_content if documents else ""
