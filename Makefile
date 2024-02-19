PYEXEC := python
BASH := bash
setup := setup.py
package := osrs_bot
package_dir := src/osrs_bot
tests_dir := tests
PYTEST_COMMAND := $(PYEXEC) -m pytest

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

.PHONY: test
test: ## run all tests.
test:
	$(PYTEST_COMMAND)

.PHONY: rebuild-docker
rebuild-docker: ## rebuilds docker file suing the lastest build image.
	docker-compose build --pull

.PHONY: clean-docker
clean-docker: ## cleans up docker volumes and rebuilds image from scratch.
	docker-compose down -v
	docker-compose build --pull

.PHONY: dev-shell
dev-shell: ## runs docker container
	docker-compose run --rm app