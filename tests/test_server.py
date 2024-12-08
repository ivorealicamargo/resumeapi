import base64
from fastapi.testclient import TestClient
from resumeapi.server import app

# Initialize the FastAPI test client
client = TestClient(app)


def test_process_resume_valid():
    """
    Test the /process/invoke endpoint with a valid base64-encoded file.
    """
    # Read the sample resume PDF
    with open("tests/sample-resume.pdf", "rb") as pdf_file:
        pdf_content = pdf_file.read()

    # Encode the PDF content to base64
    base64_encoded_file = base64.b64encode(pdf_content).decode("utf-8")

    # Prepare the payload
    payload = {"input": {"file": base64_encoded_file}}

    # Send POST request to the invoke endpoint
    response = client.post("/process/invoke", json=payload)

    # Check the response status code
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    # Parse response JSON
    data = response.json()
    print(data)

    # Validate expected fields in the output
    output = data.get("output", {})
    assert "candidate_name" in output
    assert output["candidate_name"] == "John Hui"
    assert "professional_intro" in output
    assert "skills" in output
    assert "confidence" in output
    assert output["confidence"] > 0
