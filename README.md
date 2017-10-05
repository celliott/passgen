# passgen
A docker container to run passgen.py

## Requirements
* [Docker for Mac](https://www.docker.com/docker-mac)
* Xcode command line tools to be installed `$ xcode-select --install`

## Usage
* Update AUTH_USER and AUTH_PASS in .env
* Build and run container

```
$ export AUTH_PASS=<auth_pass>
$ make build
$ make up
```

* Get password

#### plaintext

```
curl http://$AUTH_USER:$AUTH_PASS@127.0.0.1
```

#### json

```
curl http://$AUTH_USER:$AUTH_PASS@127.0.0.1/json
```
