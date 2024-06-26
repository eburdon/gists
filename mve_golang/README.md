# Requirements

Golang

```
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version
```

## Usage

```
-- build an image; tag it with something you can find later
docker build -t mve-golang .

-- To run a disposable new container, you can simply attach a tty and standard input:
docker run --rm -it --entrypoint /bin/sh mve-golang:latest

$ go run src/getting_started.go
```

### Other

```
-- run the "default" command defined in the docker image (getting_started.go)
docker container run mve-golang:latest
```
