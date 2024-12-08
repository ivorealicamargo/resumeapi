from resumeapi.chains.resume_chain import ResumeOutputParser


def test_resume_output_parser():
    parser = ResumeOutputParser()
    mock_output = """
    Ivo Reali Camargo
    I am a seasoned IT professional...
    [Python, AWS, Docker, Kubernetes]
    """
    parsed = parser.parse(mock_output)
    assert parsed["candidate_name"] == "Ivo Reali Camargo"
    assert len(parsed["skills"]) == 4


def test_resume_output_parser_complete_input():
    parser = ResumeOutputParser()
    input_text = """
    Ivo Reali Camargo
    I am a seasoned IT professional...
    [Python, Docker, Kubernetes]
    """
    expected_output = {
        "candidate_name": "Ivo Reali Camargo",
        "professional_intro": "I am a seasoned IT professional...",
        "skills": ["[Python", "Docker", "Kubernetes"],
    }
    assert parser.parse(input_text) == expected_output


def test_resume_output_parser_missing_fields():
    parser = ResumeOutputParser()
    input_text = """
    Ivo
    I am a seasoned IT professional...
    []
    """
    expected_output = {
        "candidate_name": "Ivo",
        "professional_intro": "I am a seasoned IT professional...",
        "skills": [""],
    }
    assert parser.parse(input_text) == expected_output
