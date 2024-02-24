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