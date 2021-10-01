# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

RUN pip install --upgrade pip
COPY requirements.txt /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app/

RUN chmod +x /opt/app/docker-entrypoint.sh
ENTRYPOINT [ "/opt/app/docker-entrypoint.sh" ]