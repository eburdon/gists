FROM golang:1.22-alpine3.19 as builder

WORKDIR /build

# COPY go.mod go.sum ./
COPY go.mod ./
# RUN go mod download
# RUN CGO_ENABLED=0 go build -o ./main

COPY . .

CMD ["go", "run", "src/getting_started.go"]
