PYEXEC := python
setup := setup.py
package := osrs_bot
package_dir := src/osrs_bot
tests_dir := tests
PYTEST_COMMAND := $(PYEXEC) -m pytest

.PHONY: test
test: ## Run all tests.
	$(PYTEST_COMMAND)

.PHONY: create-venv
create-venv: ## Creating virtual enviornment.
	python -m venv venv

.PHONY: venv
venv: ## Sourcing virtual environment on Windows.
	.\venv\Scripts\activate

.PHONY: format
format: ## Formatting code with auto linters
	$(PYEXEC) -m black src/ tests/