FROM python:3.7

MAINTAINER Jose Ramon Cano "joserc87@gmail.com"

#RUN apt-get update -y && \
#    apt-get install -y python3-pip python3-dev


WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

