FROM python:3.11.4-slim

WORKDIR /FamPay

COPY . /FamPay/

RUN pip install -r requirements.txt