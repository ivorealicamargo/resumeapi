import base64
from fastapi.testclient import TestClient
from resumeapi.server import app
import pytest

client = TestClient(app)


@pytest.mark.skip(reason="Test requires OPENAI_API_KEY, skipping in CI.")
def test_process_resume_valid():
    """
    Test the /process/invoke endpoint with a valid base64-encoded file.
    """

    with open("tests/sample-resume.pdf", "rb") as pdf_file:
        pdf_content = pdf_file.read()

    base64_encoded_file = base64.b64encode(pdf_content).decode("utf-8")

    payload = {"input": {"file": base64_encoded_file}}

    response = client.post("/process/invoke", json=payload)

    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    data = response.json()
    print(data)

    output = data.get("output", {})
    assert "candidate_name" in output
    assert output["candidate_name"] == "John Hui"
    assert "professional_intro" in output
    assert "skills" in output
    assert "confidence" in output
    assert output["confidence"] > 0
