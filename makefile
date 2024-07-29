# Define variables
DOCKER_COMPOSE = docker compose
APP_NAME = app_api
build:
	$(DOCKER_COMPOSE) build
test:
	$(DOCKER_COMPOSE) run --rm $(APP_NAME) python ./app/test.py
run:
	$(DOCKER_COMPOSE) up -d
clean:
	$(DOCKER_COMPOSE) down
.PHONY: build test deploy clean