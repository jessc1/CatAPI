# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /c_api

# Install dependencies
COPY Pipfile Pipfile.lock /c_api/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /c_api/