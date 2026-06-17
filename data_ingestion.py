name: RetailPulse CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    name: Lint & Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          # Install lightweight deps for testing (skip heavy ML libs)
          pip install pandas numpy scikit-learn streamlit joblib scipy statsmodels
          pip install pytest flake8 black

      - name: Lint with flake8
        run: |
          flake8 src/ main.py --max-line-length=120 --ignore=E501,W503 \
            --exclude=__pycache__,.git,venv

      - name: Check formatting with black
        run: |
          black --check src/ main.py --line-length=120

      - name: Run unit tests
        run: |
          pytest tests/ -v --tb=short

  docker-build:
    name: Docker Build Check
    runs-on: ubuntu-latest
    needs: lint-and-test
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image (no push)
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: retailpulse:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
