# pull official base image
FROM python:3.8
RUN apt-get update && apt-get install --no-install-recommends -y \
  vim-tiny \
 && rm -rf /var/lib/apt/lists/*

# set working directory
RUN mkdir -p /usr/src/jira
WORKDIR /usr/src/jira

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .