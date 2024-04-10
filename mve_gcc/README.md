## Usage

```
-- build an image; tag it with something you can find later
docker build -t mve-gcc .

-- To run a disposable new container, you can simply attach a tty and standard input:
docker run --rm -it --entrypoint /bin/sh mve-gcc:latest

$ gcc -o getting_started src/getting_started.c
$ ./getting_started
```

### Other

```
-- run the "default" command defined in the docker image (getting_started.go)
docker container run mve-gcc:latest
```
