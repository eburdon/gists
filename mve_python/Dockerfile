FROM python:3.12-alpine3.19 as builder

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir /src

COPY /src /src
COPY pyproject.toml /src

WORKDIR /src
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

# This line ensures when packages are installed with Poetry a virtual
# environment is NOT created first. You’re already in a virtual
# environment by using a docker image
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD ["python", "getting_started.py"]
