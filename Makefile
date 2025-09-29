.PHONY: install lint test format check-format check-imports ci-check
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
lint:
	pylint src tests --fail-under=9.0
test:
	pytest --cov=src --cov-report=term-missing --cov-fail-under=100
format:
	black src tests
check-format:
	black --check --diff src tests
check-imports:
	isort --check-only --diff src tests
ci-check: check-format check-imports lint test
