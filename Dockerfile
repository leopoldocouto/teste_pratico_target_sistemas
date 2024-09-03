FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /questoes
COPY . .

RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

CMD poetry test