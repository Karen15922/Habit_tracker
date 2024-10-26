FROM python:latest
WORKDIR /app
COPY ./pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main --no-root
COPY . .