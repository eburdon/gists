FROM alpine as builder

# install the gcc compiler
RUN apk add --no-cache build-base

# Add Maintainer Info
LABEL maintainer="Erika Wiedemann"

# Set the working directory. Indicates where all further commands should be run
# Creates the directory.
WORKDIR /app

RUN mkdir src
COPY ./src ./src/

# Could put this into a /dist directory
RUN gcc -o getting_started src/getting_started.c
CMD ["./getting_started"]

# # use another container to run the program
# FROM alpine as distributor

# # copy binary executable to new container
# COPY --from=build-env /app/hello /app/hello
# WORKDIR /app

# CMD ["/app/hello"] 
