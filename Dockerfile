FROM python:3.13-slim-bullseye

WORKDIR /app

RUN pip install pymilvus==2.5.0

COPY main.py .
