from resumeapi.utils.confidence_evaluator import ConfidenceEvaluator


def test_confidence_evaluator_complete_data():
    """Test confidence calculation with complete data."""
    output = {
        "candidate_name": "John Doe",
        "professional_intro": (
            "An experienced IT professional with a strong background..."
        ),
        "skills": [
            "Python",
            "AWS",
            "Kubernetes",
            "Docker",
            "Terraform",
            "GCP",
            "Pandas",
        ],
    }
    score = ConfidenceEvaluator.calculate(output)
    assert score == 1.0, f"Expected 1.0 but got {score}"


def test_confidence_evaluator_partial_data():
    """Test confidence calculation with partial data."""
    output = {
        "candidate_name": "Jane",
        "professional_intro": "An IT professional with expertise.",
        "skills": ["Python", "AWS"],
    }
    score = ConfidenceEvaluator.calculate(output)
    assert score == 0.55, f"Expected 0.55 but got {score}"


def test_confidence_evaluator_edge_cases():
    """Test confidence calculation with borderline cases."""
    output = {
        "candidate_name": "Joe",
        "professional_intro": "This is an intro with exactly fifty characters!!",
        "skills": ["Python"],
    }
    score = ConfidenceEvaluator.calculate(output)
    assert score == 0.22, f"Expected 0.22 but got {score}"
