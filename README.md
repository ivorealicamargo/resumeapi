# ResumeAPI Documentation

## Overview

**ResumeAPI** is a Python-based API application designed to parse and evaluate resumes using LangServe. It provides a user-friendly interface accessible at `http://localhost:8080/process/playground/`. The application supports both local execution and Dockerized deployment, ensuring flexibility and ease of use. It leverages LangServe (FastAPI) and LangChain for efficient processing and supports features like confidence evaluation for extracted resume fields.

---

## Features

1. **Resume Parsing**:
   - Extracts key fields such as candidate name, professional introduction, and skills from uploaded resumes.
   - Currently supports PDF file format only.

2. **Confidence Evaluation**:
   - Provides a heuristic-based confidence score for the extracted resume fields.
   - Scores are calculated based on field completeness.

3. **LangServe Integration**:
   - Uses LangServe's playground at `http://localhost:8080/process/playground/` for interactive testing of LangChain chains.

4. **Testing Suite**:
   - Comprehensive unit tests using `pytest` for ensuring reliability.
   - Coverage includes:
     - Resume parsing logic.
     - Confidence evaluation scoring.
     - PDF file handling.
     - Dockerize script for deployment automation.

5. **Dockerized Deployment**:
   - Simplifies containerized deployment with consistent environments using the dockerize utility.

---

## Quick Start

#### Prerequisites

Ensure you have the prerequisites installed:
   - Python 3.10 or higher.
   - [Poetry](https://python-poetry.org/docs/) for dependency management.
   - [Direnv](https://direnv.net/) to manage environment variables.
   - Docker for containerized deployment.

#### Steps to Run

1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/ivorealicamargo/resumeapi.git
    cd resumeapi
    ```

2. Set up the environment variables:
    - Create a `.envrc` file in the project root with the following content (see .envrc-example):
      ```bash
      export LANGCHAIN_API_KEY="your-api-key"  # Replace 'your-api-key' with your actual key
      export APP_PORT=8080
      ```
    - Load variables using:
      ```bash
      direnv allow
      ```

3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

5. Run the application in Docker:
    ```bash
    poetry run dockerize
    ```

6. Access the LangServe playground in your browser at:
    ```bash
    http://localhost:8080/process/playground/
    ```

7. Clean Up Resources
- Stop and remove container:
    ```bash
    poetry run dockerize --destroy-all
    ```
---

## Usage

1. Upload a Resume:
- Use the interface to upload a PDF file (e.g., tests/sample-resume.pdf).

2. View Results:
- The application parses fields like candidate name, professional introduction, and skills.
- Confidence scores will also be displayed in the output.

---



## Other Topics

### Running Locally

You can also run your application without using Docker locally by
- Start the application locally:
    ```bash
    poetry run resumeapi
    ```

- Access the LangServe playground:
    - Navigate to http://localhost:8080/process/playground/ in your browser.


### Testing

- Run the test suite:
    ```bash
    poetry run pytest --cov=resumeapi
    ```
- Generate a coverage report:
    ```bash
    poetry run pytest --cov=resumeapi --cov-report=html
    ```
View the report in htmlcov/index.html.

---

### Considerations

#### Assumptions
 - **Confidence Score:** The confidence score implementation is heuristic-based for demonstration purposes. A more refined scoring methodology should be developed to enhance accuracy.

 #### Additional Features with More Time
 - If given more time, the following enhancements would be prioritized:
 1. **Tracing and Logging:** Implementing robust tracing and logging throughout the system for easier debugging and monitoring.
 2. **Advanced Parsing:** Integrating libraries like Marker or Docling for improved parsing accuracy and flexibility in file formats.

  #### Ideas for Future Development
  1. **Multi-Format Support:**
  - Extend parsing capabilities to handle additional formats like .docx and .txt.
  2. **Agentic Workflow:**
  - Develop a LangGraph-based agentic workflow to dynamically manage and optimize parsing, scoring, and error handling.
  3. **LangGraph Transition:**
  - Although LangServe was used for this project, future development should consider migrating to the [LangGraph Platform](https://github.com/langchain-ai/langserve/tree/main/MIGRATION.md) as recommended by the LangChain team for new projects.

### References
- [LangServe Documentation](https://python.langchain.com/docs/langserve/)
- [LangChain Documentation](https://python.langchain.com/docs/introduction/)
