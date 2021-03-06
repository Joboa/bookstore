# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /bookstore-app

# Install dependencies
COPY Pipfile Pipfile.lock /bookstore-app/
RUN pip install pipenv && pipenv install --system --ignore-pipfile

# Copy project
COPY . /bookstore-app/
