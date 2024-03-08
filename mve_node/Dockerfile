## Simple Dockerfile to create an image for a container to run any
## Node (TS) MVE Script
## (consistent, pre-built environment with any deps)

# Good, lightweight default image
# Don't need any tooling at all? github.com/GoogleContainerTools/distroless
# NOTE: DOES NOT INCLUDE PKG MANAGERS OR SHELLS (`sh`, `bash`, `apk`)
FROM node:lts-alpine as builder

# Add Maintainer Info
LABEL maintainer="Erika Wiedemann"

# I can already connect to the image with `sh`, classic minimalistic shell
# I could also install bash
# Why? Bash supports
# - safer syntax; [[ ]] vs []
# - arrays
# - and more
# RUN apk add bash

# Create app directory for the docker image
# WORKDIR /usr/src/app
# Set the working directory. Indicates where all further commands should be run
# Creates the directory.
WORKDIR /build

# Install app dependencies from package.json. If modules are not included in
# the package.json file enter a RUN command. E.g. RUN npm install <module-name>
COPY ./package.json ./package-lock.json ./

# install deps (clean; only those versions in package-lock)
RUN npm ci

COPY ./ .

# FROM builder as production
# ENV NODE_PATH=./build

# Code is written in Typescript! Must compile to JavaScript!
# While we can run TS directly, I'm going to pretend this is a multi-stage
# build where I'm going to use this large builder to generate my JS, and then
# a second `export` target to copy just what I need. Similar pattern for 
# making go binaries
RUN npm run build

# Sample; this allows the image to be run and immediately execute SOMETHING
# rather than silently exiting. If this were a production lambda, this could
# be the handler.js. But I'm pretty sure AWS handles that for us...
CMD ["node", "build/getting_started.js"]
