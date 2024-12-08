from typing import Dict, Any


class ConfidenceEvaluator:
    """
    A class to calculate a confidence score for extracted resume data based on heuristic
    evaluation.

    This class evaluates the completeness and quality of extracted data fields such as
    candidate name, professional introduction, and skills, and assigns a confidence score
    accordingly.
    """

    @staticmethod
    def calculate(output: Dict[str, Any]) -> float:
        """
        Calculate a confidence score based on extracted data fields.

        Args:
            output (Dict[str, Any]): A dictionary containing extracted resume fields:
                - "candidate_name" (str)
                - "professional_intro" (str)
                - "skills" (list[str])

        Returns:
            float: A confidence score between 0.0 and 1.0, based on the completeness of
                   extracted fields.
        """
        score = 0.0

        candidate_name = output.get("candidate_name")
        if isinstance(candidate_name, str) and len(candidate_name.strip()) > 3:
            score += 0.33

        professional_intro = output.get("professional_intro")
        if (
            isinstance(professional_intro, str)
            and len(professional_intro.strip()) >= 50
        ):
            score += 0.33

        skills = output.get("skills")
        if isinstance(skills, list):
            skills_count = len(skills)
            if skills_count > 6:
                score += 0.34
            elif 4 <= skills_count <= 6:
                score += 0.30
            elif 1 <= skills_count <= 3:
                score += 0.22

        return round(min(score, 1.0), 2)
