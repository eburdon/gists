FROM node:lts-alpine as builder

# Create app directory for the docker image
WORKDIR /usr/src/app

# Install app dependencies from package.json. If modules are not included in the package.json file enter a RUN command. E.g. RUN npm install <module-name>
COPY ./package.json ./package-lock.json ./
RUN npm ci

COPY . .

FROM builder as production

ENV NODE_PATH=./build

RUN npm run build

CMD ["node", "build/getting_started.js"]
