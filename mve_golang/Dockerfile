FROM golang:1.22-alpine3.19 as builder

WORKDIR /build

# COPY go.mod go.sum ./
COPY go.mod ./
# RUN go mod download

COPY . .

CMD ["go", "run", "src/getting_started.go"]
