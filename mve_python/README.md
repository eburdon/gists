# Requirements

pyenv
* https://github.com/pyenv/pyenv
* https://github.com/pyenv/pyenv-installer

poetry

Docker

## Usage

```
-- build an image; tag it with something you can find later
docker build -t mve-python .

-- To run a disposable new container, you can simply attach a tty and standard input:
docker run --rm -it --entrypoint /bin/sh mve-python:latest

$ python src/getting_started.py
```

### Other

```
-- immediately run getting_started.py
docker container run mve-python:latest
```
