import base64
from fastapi import FastAPI
from resumeapi.parsers.pdf_parser import PDFParser
from resumeapi.chains.resume_chain import create_resume_chain
from resumeapi.utils.confidence_evaluator import ConfidenceEvaluator
from langserve import CustomUserType, add_routes
from pydantic import Field
from langchain_core.runnables import RunnableLambda
from typing import Dict
import uvicorn

app = FastAPI(
    title="LangChain Resume Parser",
    version="1.2",
    description="Resume parser using PDFMiner and LangChain.",
)


class FileProcessingRequest(CustomUserType):
    """
    Schema for the request payload, including a base64 encoded file.

    Attributes:
        file (str): A base64-encoded string representing the uploaded file.
    """

    file: str = Field(..., extra={"widget": {"type": "base64file"}})


def process_resume(request: FileProcessingRequest) -> Dict[str, object]:
    """
    Process an uploaded resume file, extracting structured data.

    This function decodes the base64-encoded file, extracts text content from the
    PDF, processes the content using a LangChain pipeline, and evaluates the
    confidence of the extracted data.

    Args:
        request (FileProcessingRequest): Request containing the base64-encoded file.

    Returns:
        Dict[str, object]: Structured data extracted from the resume, including:
            - Candidate's full name.
            - Professional introduction.
            - List of skills.
            - Confidence score for the extracted data.
    """
    # Decode and parse PDF
    content = base64.b64decode(request.file.encode("utf-8"))
    resume_text = PDFParser.parse(content)

    # Extract data using the resume chain
    chain = create_resume_chain()
    extracted_data = chain.invoke({"resume_text": resume_text})

    # Evaluate confidence score
    confidence_score = ConfidenceEvaluator.calculate(extracted_data)
    extracted_data["confidence"] = confidence_score
    return extracted_data


add_routes(
    app,
    RunnableLambda(process_resume).with_types(input_type=FileProcessingRequest),
    path="/process",
)


def main():
    """
    Entrypoint for running the FastAPI app using Uvicorn.
    """
    uvicorn.run("resumeapi.server:app", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
