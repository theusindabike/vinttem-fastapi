FROM python:3.11.1-alpine3.17 as builder

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers \    
    && apk del .tmp-build-deps \
    && pip install --upgrade pip \
    && pip install poetry

WORKDIR /api

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /api