# use virtualenv or virtualenv-wrapper location based on availability
ifdef WORKON_HOME
	VIRTUALENV = $(WORKON_HOME)/mollie-api-python
endif
ifndef VIRTUALENV
	VIRTUALENV = $(PWD)/env
endif

PYTHON_VERSION = 3.9
PYTHON = $(VIRTUALENV)/bin/python


.PHONY: virtualenv
virtualenv: $(VIRTUALENV)  # alias
$(VIRTUALENV):
	$(shell which python$(PYTHON_VERSION)) -m venv $(VIRTUALENV)
	$(PYTHON) -m pip install --upgrade pip setuptools wheel


.PHONY: develop
develop: mollie_api_python.egg-info virtualenv # alias
mollie_api_python.egg-info:
	$(PYTHON) -m pip install -r test_requirements.txt
	$(PYTHON) -m pip install -e .


.PHONY: test
test: develop
	$(PYTHON) -m pytest --black
	$(PYTHON) -m safety check


.PHONY: clean
clean:
	rm -f -r build/ dist/ .eggs/ mollie_api_python.egg-info .pytest_cache


.PHONY: realclean
realclean: clean
	rm -f -r $(VIRTUALENV)
