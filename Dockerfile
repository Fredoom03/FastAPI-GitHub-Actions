FROM python:3.11

RUN mkdir /app

COPY . ./app 

RUN pip install ruff pydantic pydantic[email] pytest