# syntax=docker/dockerfile:1
FROM python:alpine
WORKDIR /challenge
COPY converter.py /challenge/
CMD [ "python3", "-u", "converter.py" ]