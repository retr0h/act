#!/usr/bin/env make

.PHONY: dep
dep:
	pip install poetry
	poetry install

.PHONY: test
test: lint format-check unit cov

.PHONY: unit
unit:
	poetry run py.test -vv --junitxml=xunit-reports/xunit-result-act.xml

.PHONY: cov
cov:
	poetry run py.test --cov act --cov-report term-missing --cov-report xml:coverage-reports/coverage-act.xml --showlocals

.PHONY: lint
lint:
	poetry run flake8

.PHONY: format
format:
	poetry run black .
	poetry run isort .

.PHONY: format-check
format-check:
	poetry run black --diff --check .
	poetry run isort --check-only --diff .

.PHONY: build-dist
build-dist:
	poetry build
