dev:
	poetry run uvicorn simple_proxy.main:app --reload

.PHONY: t test
t test:
	poetry run pytest -vv -s
