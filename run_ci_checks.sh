#!/usr/bin/env bash
set -euo pipefail
black --check --diff src tests
isort --check-only --diff src tests
pylint src tests --fail-under=9.0
pytest --cov=src --cov-report=term-missing --cov-fail-under=100
