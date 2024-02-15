#syntax=docker/dockerfile:1

FROM python:3.10-alpine3.15
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./README.md /app/README.md
COPY ./main /app/main
