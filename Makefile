# Makefile for python code
# 
# > make help
#
# The following commands can be used.
#
# init:  sets up environment and installs requirements
# install:  Installs development requirments
# format:  Formats the code with autopep8
# lint:  Runs flake8 on src, exit if critical rules are broken
# clean:  Remove build and cache files
# env:  Source venv and environment files for testing
# leave:  Cleanup and deactivate venv
# test:  Run pytest
# run:  Executes the logic

VENV_PATH='env/bin/activate'
ENVIRONMENT_VARIABLE_FILE='.env'
DOCKER_NAME=osrs-bot
DOCKER_TAG=latest

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)


install: ## Installs development requirments
install:
	python -m pip install --upgrade pip
	# Used for packaging and publishing
	pip install setuptools wheel twine
	# Used for linting
	pip install flake8
	# Used for testing
	pip install pytest

lint: ## Runs flake8 on src, exit if critical rules are broken
lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics

clean: ## Remove build and cache files
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

test: ## Run pytest
test:
	pytest . -p no:logging -p no:warnings

build: ## Build docker image
build:
	docker build -t $(DOCKER_NAME):$(DOCKER_TAG) -f Dockerfile .

create: ## Create docker image
create: build
	docker create -it --name $(DOCKER_NAME) $(DOCKER_NAME):$(DOCKER_TAG)

start: ## Build and start docker image
start: build
	docker start $(DOCKER_NAME)

run: ## build, start and run docker image
run: start
	docker run -it $(DOCKER_NAME):$(DOCKER_TAG)

exec: ## build, start and exec into docker image
exec: start
	docker exec -it $(DOCKER_NAME) bash