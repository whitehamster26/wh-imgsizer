install:
	poetry install
lint:
	poetry run flake8 src
test:
	poetry run pytest --cov=wh-imgsizer --cov-report xml tests/