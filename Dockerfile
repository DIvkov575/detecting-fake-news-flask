# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

MAINTAINER Dmitriy Ivkov "Dmitriy@ivkov.net"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "App.py" ]
