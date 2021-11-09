From python:3.8

RUN pip install --upgrade pip
WORKDIR /demo/
COPY requirements.txt /demo
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y vim
ADD server /demo