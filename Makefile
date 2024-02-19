PYEXEC := python
BASH := bash
setup := setup.py
package := osrs_bot
package_dir := src/osrs_bot
tests_dir := tests
PYTEST_COMMAND := $(PYEXEC) -m pytest --cov=. --cov-fail-under=90 --import-mode=importlib --cov-config=pyproject.toml --cov-report=xml:coverage.xml --cov-report=term-missing --cov-branch $(package_dir) $(tests_dir)

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

# .PHONY: all
# all: ## Run lint checks and tests.
# all: fix-lint lint test

# .PHONY: format
# format:
# 	$(PYEXEC) -m ruff format --check $(package_dir)
# 	$(PYEXEC) -m ruff format --check $(tests_dir)

# .PHONY: ruff-fix
# ruff-fix: ## Fix code formatting using Ruff
# ruff-fix: 
# 	$(PYEXEC) -m ruff check --fix-only -e $(package_dir)
# 	$(PYEXEC) -m ruff check --fix-only -e $(tests_dir)

# .PHONY: format-fix
# format-fix: ## Format the source code with Black
# format-fix: 
# 	$(PYEXEC) -m ruff format -q $(package_dir)
# 	$(PYEXEC) -m ruff format -q $(tests_dir)

# .PHONY: blocklint
# blocklint: 
# 	$(PYEXEC) -m mypy --config-file pyproject.toml $(package_dir)

# .PHONY: mypy
# mypy: 
# 	$(PYEXEC) -m blocklint --max-issue-threshold 1 $(package_dir)

# .PHONY: ruff
# ruff: 
# 	$(PYEXEC) -m ruff check $(package_dir)
# 	$(PYEXEC) -m ruff check $(tests_dir)

# .PHONY: lint
# lint: ## Run lint checks.
# lint: ruff mypy format blocklint

# .PHONY: fix-lint
# fix-lint:  ## Fix any lint errors that can be fixed automatically.
# fix-lint: ruff-fix format-fix

# .PHONY: test
# test: ## run all tests.
# test:
# 	$(PYTEST_COMMAND)

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