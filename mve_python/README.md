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
Successfully copied 2.05kB to clever_ellis:/src

-- back to original tab running disposable container
$ python ./hello.py

-- Installed something via poetry?
$ docker run --rm -it --entrypoint /bin/sh mve-python:latest
/src # poetry add pytz
-- don't forget to copy it back from container to host
-- in another tab
$ docker ps
$ docker cp crazy_jemison:./src/pyproject.toml ./
```

### Other

```
-- immediately run getting_started.py
docker container run mve-python:latest
```
