## Simple Dockerfile to create an image for a container to run any
## GoLang MVE Script
## (consistent, pre-built environment with any deps)

# Good, lightweight default image
# Don't need any tooling at all? github.com/GoogleContainerTools/distroless
# NOTE: DOES NOT INCLUDE PKG MANAGERS OR SHELLS (`sh`, `bash`, `apk`)
FROM golang:1.22-alpine3.19 as builder

# Add Maintainer Info
LABEL maintainer="Erika Wiedemann"

# I can already connect to the image with `sh`, classic minimalistic shell
# I could also install bash
# Why? Bash supports
# - safer syntax; [[ ]] vs []
# - arrays
# - and more
# RUN apk add bash

# Set the working directory. Indicates where all further commands should be run
# Creates the directory.
WORKDIR /build

# Add when dependencies are added
# COPY go.mod go.sum ./
COPY go.mod ./

# Add when dependencies are added
# Copy the source from the current directory to the Working Directory inside the container
# RUN go mod download

COPY ./ .

# Sample; this allows the image to be run and immediately execute SOMETHING
# rather than silently exiting. If this were production, this could be the
# server binary generated in a `GO BUILD` command.
CMD ["go", "run", "src/getting_started.go"]

################################################
## Sample of what a Dockerfile would look like if I was building a binary to
## run somewhere else, like on AWS Lambda
# FROM golang:1.22-alpine3.19 as builder
# WORKDIR /build
# COPY go.mod go.sum ./
# RUN go mod download
# COPY ./ .
# Compile the code
# RUN CGO_ENABLED=0 go build -o ./main
# CMD []
