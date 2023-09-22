
FROM python:3.9.18-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv requirements > requirements.txt

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

WORKDIR /code

COPY src/ .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
