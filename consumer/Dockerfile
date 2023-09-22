FROM python:3.9.18-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y

RUN pip install pika

WORKDIR /code

COPY --chown=zeny:zeny src/ .

CMD ["python", "main.py"]
