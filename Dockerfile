FROM python:3.10-slim

RUN apt-get update && apt-get install -y iputils-ping curl

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY src src/
COPY vectorstore vectorstore/
COPY docs docs/


CMD ["python", "-m", "src.main"]