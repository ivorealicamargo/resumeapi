# ResumeAPI Documentation

## Overview

**ResumeAPI** is a Python-based API application designed to parse and evaluate resumes using LangServe. It provides a user-friendly interface accessible at `http://localhost:8080/process/playground/`. The application supports both local execution and Dockerized deployment, ensuring flexibility and ease of use. It leverages LangServe (FastAPI) and LangChain for efficient processing and supports features like confidence evaluation for extracted resume fields.

---

## Features

1. **Resume Parsing**:
   - Extracts key fields such as candidate name, professional introduction, and skills from uploaded resumes.
   - Supports PDF file format ONLY.

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
     - PDF parsing.
     - Dockerize script for deployment automation.

5. **Dockerized Deployment**:
   - Simplifies containerized deployment for consistent environments.
   - Manages Docker containers and images using the `dockerize` utility.

---

## Quick Start

For those who want to get started immediately, follow these steps:

1. Ensure you have the prerequisites installed:
   - Python 3.10 or higher.
   - [Poetry](https://python-poetry.org/docs/) for dependency management.
   - [Direnv](https://direnv.net/) to manage environment variables.
   - Docker for containerized deployment.

2. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/ivorealicamargo/resumeapi.git
    cd resumeapi
    ```

3. Set up the environment variables:
    - Create a `.envrc` file in the project root with the following content (see .envrc-example):
      ```bash
      export LANGCHAIN_API_KEY="your-api-key"  # Replace 'your-api-key' with your actual key
      export APP_PORT=8080
      ```
    - Run `direnv allow` to load the environment variables.

4. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

5. Run the application in Docker:
    ```bash
    poetry run dockerize
    ```

6. Access the LangServe playground at:
    ```bash
    http://localhost:8080/process/playground/
    ```

7. Stop and remove resources when finished:
    ```bash
    poetry run dockerize --destroy-all
    ```


### Running and Testing the Application
Once the application is running (locally or via Docker), open your browser and navigate to:
http://localhost:8080/process/playground/


-  **Testing with a Sample Resume**:
    - The project includes a sample resume file located at `tests/sample-resume.pdf`.
    - Upload this file through the interface and click **Start** to test the resume parsing functionality.

- **Viewing Results**:
    - The parsed resume data, including fields such as candidate name, professional introduction, skills, and confidence scores, will appear in the output section.

Ensure your environment variables are correctly set (e.g., `LANGCHAIN_API_KEY`) before running the application. The `sample-resume.pdf` provides a reliable test file to verify the app's capabilities.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher.
- Poetry for dependency management.
- Docker installed for containerized deployment.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ivorealicamargo/resumeapi.git
   cd resumeapi
   ```

2. Install dependencies using Poetry:
   ```bash
    poetry install
   ```

3. Ensure environment variables are set:
- Use a `.envrc`file with the following format:
    ```bash
    export LANGCHAIN_API_KEY="your-api-key" # Replace 'your-api-key' with your actual key
    export APP_PORT=8080
    ```
- Run direnv allow in the project's directory to load the environment variables.

### Running Locally

- Start the application locally:
    ```bash
    poetry run resumeapi
    ```

- Access the LangServe playground:
    - Navigate to http://localhost:8080/process/playground/ in your browser.


### Code Quality and Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to ensure code quality and enforce consistent formatting before commits. The hooks include checks for:

- Code formatting with `black`
- Code style issues with `flake8`
- Type safety validation with `mypy`

#### Running Pre-commit Hooks Manually

Before pushing your changes, ensure your code passes all pre-commit checks by running:

```bash
poetry run pre-commit run --all-files
```

#### Continuous Integration

Pre-commit checks are also part of the CI pipeline. Code that doesn’t pass these checks will fail the CI tests and cannot be merged. Make sure to resolve any issues locally before pushing your changes.

### Dockerized Deployment

#### Building and Running with Docker
Use the `dockerize` functionality to manage the Dockerized deployment.

1. Run the application in Docker:
    ```bash
    poetry run dockerize
    ```

2. Access the application:

    - Open the following link in your browser:
    ```bash
    http://localhost:8080/process/playground/
    ```

#### Additional Commands

- Stop and remove the Docker container:
    ```bash
    poetry run dockerize --kill-container
    ```

 - Remove both the Docker container and image:
    ```bash
    poetry run dockerize --destroy-all
    ```

---


### Testing

 - Run the tests with:
    ```bash
    poetry run pytest --cov=resumeapi
    ```
#### Coverage report:
 - Generate a coverage report:
    ```bash
    poetry run pytest --cov=resumeapi --cov-report=html
    ```
    View the report in htmlcov/index.html.


### Troubleshooting

1. Port Already in Use:
- Ensure port 8080 is free, or modify the APP_PORT variable in .envrc.

2. Docker Issues:
- If Docker fails to start the application, ensure Docker Desktop is running and accessible.

3. Pre-commit Hooks Not Installed:
- Install pre-commit hooks:
    ```bash
        poetry run pre-commit install
    ```
 ---

 ## References

- [LangServe Documentation](https://python.langchain.com/docs/langserve/)
- [LangChain Documentation](https://langchain.com/docs)

---
