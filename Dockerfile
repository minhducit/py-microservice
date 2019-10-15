FROM python:3.7-slim-buster

RUN apt-get update -qq && apt-get install -y \
    && apt-get install -y --no-install-recommends gcc python3-dev

COPY pip.conf /etc/

RUN pip3 install --user poetry uwsgi
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config settings.virtualenvs.in-project true

RUN mkdir -p /usr/lib/app
WORKDIR /usr/lib/app

# add .lock file to install python packages
COPY pyproject.toml pyproject.toml

# wait-for-it
COPY ./wait-for-it.sh .

# setup python environment
RUN poetry install --no-interaction --no-ansi --no-dev

# remove the extra packages
RUN apt-get purge -y --auto-remove unzip gcc python3-dev

# Source Code section
COPY README.rst README.rst

# Copy source and test package
COPY openapi openapi
COPY src src
COPY run.py run.py

EXPOSE 8765