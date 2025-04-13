COMPOSE = docker-compose
DOCKER = docker
CONTAINER_NAME = golden-raspberry-api

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

restart:
	@$(COMPOSE) restart

build:
	@$(COMPOSE) up -d --build

ps:
	@$(DOCKER) ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"

bash:
	@$(DOCKER) exec -it $(CONTAINER_NAME) bash

logs:
	@$(DOCKER) logs -f $(CONTAINER_NAME)

test:
	@$(DOCKER) exec $(CONTAINER_NAME) env PYTHONPATH=. pytest

%:
	@:  # for commands dosen't exists
