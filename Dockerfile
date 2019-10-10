FROM python:3.7-slim-buster

WORKDIR /usr/lib/app

# add .lock file to install python packages
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

# setup python environment
RUN pip install poetry
RUN pip install kafka-python
RUN poetry install --no-interaction --no-ansi --no-dev

# Source Code section
COPY README.rst README.rst

# Copy source and test package
COPY openapi openapi
COPY src src
COPY run.py run.py

EXPOSE 8765

# command to start python service
# CMD ["uwsgi", "--ini", "uwsgi.ini"]