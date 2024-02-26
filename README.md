# GISTS

A place to quickly get MVEs up and running without having to configure an environment every time.

## Requirements

Docker
* https://docs.docker.com/engine/install/ubuntu/
* https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket

### Docker

```
-- build an image; tag it with something you can find later
docker build -t mve-python .

-- jump immediately into main.py
docker container run mve-python:latest

-- creates a new container from the specified image, without starting it
-- volumes are created here
docker container create -i -t --name gs-container mve-python

-- starts the container and attaches to it
docker container start --attach -i gs-container

-- list files copied into container (via Dockerfile image)
docker run mve-python ls -la

-- check running containers
docker ps

-- list all images you've created
docker image list

-- clean all images now and again
-- Remove all dangling images
docker image prune -a

-- docker images -a will always show lots of “none” images, since it shows every layer of every image.
-- you cannot delete intermediate images
https://projectatomic.io/blog/2015/07/what-are-docker-none-none-images/
```
