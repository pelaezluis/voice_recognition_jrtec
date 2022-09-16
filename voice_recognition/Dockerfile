FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /app

# Install Poetry
RUN apt clean && apt update && apt install libsndfile1 -y
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


COPY pyproject.toml poetry.lock* /app/

RUN bash -c "poetry install --no-root"

ENV PYTHONPATH=/app
EXPOSE 8000