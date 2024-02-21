# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.5
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pwd && ls && \
    apt-get update && \
    apt-get install -y libpq-dev gcc

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE  8000