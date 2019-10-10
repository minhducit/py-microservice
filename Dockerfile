FROM am-wfa-prd.asml.com:18443/white-rabbit-base-python-oracle:3.7-slim-buster

WORKDIR /usr/lib/app

# add .lock file to install python packages
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

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

COPY data data
COPY tests tests


EXPOSE 8765

# command to start python service
# CMD ["uwsgi", "--ini", "uwsgi.ini"]