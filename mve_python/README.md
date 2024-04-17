# Requirements

pyenv
* https://github.com/pyenv/pyenv
* https://github.com/pyenv/pyenv-installer

poetry

Docker

## Usage

```
-- build an image; tag it with something you can find later
-- NEEDS INTERNET CONNECTION!
docker build -t mve-python .

-- To run a disposable new container, you can simply attach a tty and standard input:
docker run --rm -it --entrypoint /bin/sh mve-python:latest

-- In another tab; get container name
docker ps

-- In another tab; copy unbuilt file into your container
docker cp ./hello.py clever_ellis:/src

-- back to original tab running disposable container
$ python ./hello.py

-- Installed something via poetry?
$ docker run --rm -it --entrypoint /bin/sh mve-python:latest

/src # poetry add pytz

-- don't forget to copy it back from container to host
-- in another tab
$ docker ps
$ docker cp crazy_jemison:./src/pyproject.toml ./
$ python src/getting_started.py
```

### Docker compose

Docker compose is... unecessary for this project.

> helps you define and share multi-container applications. With Compose, you can create a YAML file to define the services and with a single command, you can spin everything up or tear it all down.

However, it still has some helpful features like

1. Consistent commands - enter any project with a Dockerfile and run `docker compose up` - no more thinking needed
2. Simpler commands - just run `docker compose build && docker compose run composed-app` and you're already into the bash container!

### Other

```
-- immediately run getting_started.py
docker container run mve-python:latest
```
