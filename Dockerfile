# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# buffering 하지 않음
ENV PYTHONUNBUFFERED 1

# 우분투 리눅스에서 사용
# RUN apk update
# RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . /usr/src/app/
#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt