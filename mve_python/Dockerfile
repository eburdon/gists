## Simple Dockerfile to create an image for a container to run any
## Python MVE Script
## (consistent, pre-built environment with any deps).
## New build stage AND set base stage for subsequent stages

# Good, lightweight default image
# Don't need any tooling at all? github.com/GoogleContainerTools/distroless
# NOTE: DOES NOT INCLUDE PKG MANAGERS OR SHELLS (`sh`, `bash`, `apk`)
FROM python:3.12-alpine3.19 as builder

# Add Maintainer Info
LABEL maintainer="Erika Wiedemann"

# TODO: FOLLOWUP
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# TODO: FOLLOWUP
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the working directory. Indicates where all further commands should be run
# Creates the directory.
WORKDIR /app

# COPY /src /src
COPY ./pyproject.toml ./

# ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

# This line ensures when packages are installed with Poetry a virtual
# environment is NOT created first. You’re already in a virtual
# environment by using a docker image
RUN poetry config virtualenvs.create false

# dep installation
RUN poetry install --no-dev

RUN mkdir src
COPY ./src ./src/

# all dependencies installed to
#       /usr/local/lib/python3.12/site-packages
# to create a complete lambda build, .zip the deps and put it somewhere
# a later docker stage can copy from. 
#       zip -r ../../../../my_deployment_package.zip .
# you'd also need to copy the function you want to run.
#       cd ./src/
#       zip my_deployment_package.zip lambda_function.py

CMD ["python", "src/getting_started.py"]
