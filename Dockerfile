FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY api/requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

COPY . /api