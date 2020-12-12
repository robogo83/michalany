# pull official base image
FROM python:3.8.3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /michalany

# install dependencies
COPY Pipfile Pipfile.lock /michalany/
RUN pip install pipenv && pipenv install --system

# copy project
COPY . /michalany/
