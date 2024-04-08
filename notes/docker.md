# Docker Notes

## QUESTIONS

1. Can I not use this offline? Re: pulling docker images. Cached? I thought it was forever.


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
## Resources

Multi-stage builds: https://docs.docker.com/build/building/multi-stage/ 

* With multi-stage builds, you use multiple FROM statements in your Dockerfile.
* You can selectively copy artifacts from one stage to another, leaving behind everything you don't want in the final image.
* The end result is a tiny production image with nothing but the binary inside. None of the build tools required to build the application are included in the resulting image.
* By default, the stages aren't named, and you refer to them by their integer number, starting with 0 for the first FROM instruction. Sample: `COPY --from=0 /bin/hello /bin/hello`
* You can name your stages and use that name in `COPY`; better defense against re-ordering instructions in the Dockerfile
* When you build your image, you don't necessarily need to build the entire Dockerfile including every stage. You can specify a target build stage (and it'll stop there)
* You can pick up where a previous stage left off by referring to it when using the FROM directive.

Docker Multi-Stage Builds: An In-depth Guide: https://ercanermis.com/docker-multi-stage-builds-an-in-depth-guide/

* Multi-stage builds seem extremely common for GoLang - preferred? Best practice?
* Docker builds represents a pinnacle best practice in the domain of containerization
* Use Specific Base Images. Use a Node.js image for a build stage that involves a Node.js application, and an Alpine image for a lightweight final stage.
* Optimize Layer Creation: Docker builds images in layers. To make your builds faster and your images smaller, try to minimize the number of layers by combining commands using &&.
* In the [build stage], clean up unnecessary files and artifacts after you’re done with them. This will make the build cache smaller and faster.

## GoLang

* https://christiangiacomi.com/posts/multi-stage-docker-image-go/
* https://tutorialedge.net/golang/go-multi-stage-docker-tutorial/ 

## Node (TS)

## Python
