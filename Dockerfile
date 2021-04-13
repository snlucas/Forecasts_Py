FROM python:3

WORKDIR /code

COPY requirements.tx /code/

RUN pip install -r requirements.txt

COPY . /code/

