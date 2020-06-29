FROM python:3.8.3-alpine

WORKDIR /home/src

RUN pip install --upgrade pip \
    "graphene==2.1.8" \
    "Flask==1.1.2" \
    "Flask-GraphQL==2.0.1" 

