install:
	poetry install
lint:
	poetry run flake8 src
test:
	poetry run pytest --cov=src --cov-report xml tests/