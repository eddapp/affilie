.PHONY: all build push deploy run stop

all: build push deploy

build:
	docker build -t wukogan/affilie:latest -f config/myhome/Dockerfile .

push:
	docker push wukogan/affilie:latest

deploy:
	eb deploy

run:
	docker-compose up -d

stop:
	docker-compose down
