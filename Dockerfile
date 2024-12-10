FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.4

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main

COPY . .


CMD ["sh", "-c", "poetry run resumeapi --port ${APP_PORT}"]
