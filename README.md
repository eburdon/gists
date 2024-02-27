# GISTS

A place to quickly get MVEs up and running without having to configure an environment every time.

## Requirements

Docker
* https://docs.docker.com/engine/install/ubuntu/
* https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket

### Docker Notes

On images...
```
-- list files copied into image
docker run mve-python ls -la

-- list all images you've created
docker image list

-- clean all dangling images now and again
docker image prune -a

-- docker images -a will always show lots of “none” images, since it shows every layer of every image.
-- you cannot delete intermediate images
https://projectatomic.io/blog/2015/07/what-are-docker-none-none-images/
```

On containers...
```
-- creates a new container from the specified image (above) without starting it
docker container create -i -t --name python-container mve-python

-- starts the container and attaches to it; must have long-running task
docker container start --attach -i pyth-container

-- check running containers
docker ps
```
