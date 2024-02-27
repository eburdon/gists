# Requirements

nvm
* https://github.com/nvm-sh/nvm
* https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04#option-3-installing-node-using-the-node-version-manager

Docker

```
docker build -t mve-node .

docker run --rm -it --entrypoint /bin/sh mve-node:latest

-- run compiled TS
node build/getting_started.js

-- run original TS
node src/getting_started.ts

-- run plain JS
node src_js/hello_world.js
```

## Notes

(NODE vs JS): JavaScript is primarily used for client-side programming, while Node. js allows developers to build server-side applications using JavaScript.

(JS vs TS): TypeScript was created with the aim of expanding the technical abilities of JavaScript. It offers static typing and helps discover the problems with coding prior to their appearance in the runtime environment.

### Other

```
-- immediately run getting_started.ts
docker container run mve-node:latest
```
