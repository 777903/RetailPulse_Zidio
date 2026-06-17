version: "3.9"

services:
  retailpulse:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: retailpulse_app
    ports:
      - "8501:8501"
    volumes:
      # Persist generated data and model artifacts across restarts
      - ./data:/app/data
      - ./models:/app/models
      - ./reports:/app/reports
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 90s
    restart: unless-stopped

  # Optional: MLflow tracking server
  mlflow:
    image: python:3.11-slim
    container_name: retailpulse_mlflow
    command: >
      sh -c "pip install mlflow && mlflow server
             --host 0.0.0.0
             --port 5000
             --backend-store-uri sqlite:///mlflow.db
             --default-artifact-root /mlruns"
    ports:
      - "5000:5000"
    volumes:
      - ./mlruns:/mlruns
      - mlflow_db:/mlflow.db
    restart: unless-stopped
    profiles:
      - mlops   # start with: docker-compose --profile mlops up

volumes:
  mlflow_db:
