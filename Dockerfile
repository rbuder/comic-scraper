FROM alpine:3.15.0
WORKDIR /usr/src/app

LABEL org.opencontainers.image.authors="ronald.buder@gmail.com"

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools


COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
