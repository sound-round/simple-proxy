FROM python:3.11.6-slim

ENV POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN apt-get remove -y --purge curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --only main --no-interaction --no-ansi --no-root

COPY . /app

CMD ["poetry", "run", "uvicorn", "simple_proxy.main:app", "--reload", "--host", "127.0.0.1", "--port", "80"]
