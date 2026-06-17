# 🛒 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

> **Prepared by:** Satya Sourav Das  
> **Prepared for:** Zidio Development – Data Science & Analytics Domain  
> ⚠️ *All data used in this project is synthetic and does not represent real individuals or businesses.*

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Project Overview

RetailPulse is an **end-to-end AI-powered retail analytics platform** that transforms raw sales, customer, and inventory data into actionable business intelligence through machine learning and interactive dashboards.

The platform enables retail businesses to:
- **Forecast demand** 30 days ahead per product category
- **Segment customers** into 6–8 actionable groups using RFM + K-Means
- **Predict churn** with >88% AUC-ROC and identify at-risk customers
- **Optimise inventory** using EOQ-based reorder recommendations
- **Monitor models** with MLflow and drift detection

---

## 🎯 Business Problem

Retail businesses lose millions annually due to:
- **Stockouts** → lost sales, customer dissatisfaction
- **Overstock** → capital tied up, waste
- **Unaddressed churn** → revenue leakage
- **Unfocused marketing** → low ROI campaigns

RetailPulse solves all four problems with a unified ML-powered platform.

---

## 💡 Expected Business Impact

| Impact Area | Improvement |
|---|---|
| Stockout Reduction | **30–50%** |
| Revenue Uplift | **15–25%** |
| Churn Reduction | **20–35%** |
| Inventory Efficiency | **25–40%** |
| Decision Speed | **5× faster** |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         RetailPulse                             │
├─────────────────┬───────────────────┬───────────────────────────┤
│  Data Layer     │   ML Models       │   Dashboard               │
│  ─────────────  │   ───────────     │   ─────────────           │
│  Synthetic Gen  │   K-Means Seg.    │   Streamlit App           │
│  Data Ingestion │   Prophet/SARIMA  │   6 Interactive Pages     │
│  Preprocessing  │   RF/XGB Churn    │   Plotly Charts           │
│  Feature Eng.   │   EOQ Inventory   │   KPI Cards               │
├─────────────────┴───────────────────┴───────────────────────────┤
│  MLOps: MLflow Tracking  │  Docker  │  GitHub Actions CI/CD     │
│  Kubernetes Deployment   │  Pytest  │  Evidently Drift Detection│
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Project Structure

```
RetailPulse_Zidio/
├── data/
│   ├── raw/          ← Auto-generated or user-provided CSVs
│   ├── processed/    ← Cleaned & feature-engineered datasets
│   └── sample/       ← 500-row sample files
│
├── src/              ← Core Python modules
│   ├── config.py               ← Paths, hyperparameters
│   ├── data_ingestion.py       ← Load / generate data
│   ├── preprocessing.py        ← Data cleaning
│   ├── feature_engineering.py  ← RFM, CLV, demand features
│   ├── segmentation_model.py   ← K-Means clustering
│   ├── forecasting_model.py    ← Prophet / SARIMA forecast
│   ├── churn_model.py          ← LR / RF / XGBoost churn
│   ├── inventory_optimizer.py  ← EOQ reorder recommendations
│   ├── model_evaluation.py     ← Metrics + report
│   └── utils.py                ← Shared helpers
│
├── dashboard/
│   ├── app.py                  ← Main Streamlit app (Home)
│   └── pages/
│       ├── 1_Sales_Analytics.py
│       ├── 2_Demand_Forecasting.py
│       ├── 3_Customer_Segmentation.py
│       ├── 4_Churn_Prediction.py
│       ├── 5_Inventory_Optimization.py
│       └── 6_Model_Performance.py
│
├── models/           ← Saved ML model artifacts (.pkl)
├── reports/          ← Figures, metrics, drift reports
├── deployment/       ← Dockerfile, K8s, GitHub Actions
├── tests/            ← Pytest unit tests
├── notebooks/        ← Jupyter EDA & modelling notebooks
├── main.py           ← Pipeline orchestrator
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Data | Pandas, NumPy |
| ML / Stats | scikit-learn, statsmodels, Prophet, XGBoost |
| Explainability | SHAP |
| Visualisation | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| MLOps | MLflow, Evidently AI |
| Persistence | Joblib / Pickle |
| Deployment | Docker, Kubernetes |
| CI/CD | GitHub Actions |
| Testing | Pytest |

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/RetailPulse_Zidio.git
cd RetailPulse_Zidio
```

### 2. Create virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note:** If Prophet installation fails, the system will automatically fall back to SARIMA forecasting.

---

## ▶️ How to Run

### Run Full ML Pipeline (recommended first step)
```bash
python main.py
# OR explicitly
python main.py --all
```

This will:
1. Generate synthetic retail data (12,000+ transactions, 1,200 customers, 120 products)
2. Clean and preprocess all datasets
3. Build RFM + ML features
4. Train K-Means segmentation
5. Train demand forecasting (Prophet/SARIMA)
6. Train churn prediction (RF/XGBoost)
7. Generate inventory recommendations
8. Save all outputs to `data/processed/` and `models/`

### Run Individual Steps
```bash
python main.py --generate-data          # Step 1 only
python main.py --preprocess             # Step 2 only
python main.py --feature-engineering   # Step 3 only
python main.py --train-segmentation    # Segmentation only
python main.py --train-forecasting     # Forecasting only
python main.py --train-churn           # Churn only
python main.py --inventory             # Inventory only
```

### Launch Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
Then open: [http://localhost:8501](http://localhost:8501)

### Run Tests
```bash
pytest tests/ -v
```

---

## 🐳 Docker Deployment

### Build and run locally
```bash
docker-compose up --build
```
Open: [http://localhost:8501](http://localhost:8501)

### With MLflow tracking server
```bash
docker-compose --profile mlops up --build
```
MLflow UI: [http://localhost:5000](http://localhost:5000)

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
kubectl get services  # Get external IP
```

---

## ☁️ Cloud Deployment Options

| Platform | Command |
|---|---|
| Streamlit Cloud | Push to GitHub, connect at share.streamlit.io |
| Render | Create Web Service, connect repo |
| Hugging Face Spaces | `git push` with `app.py` at root |
| GCP Cloud Run | `gcloud run deploy` with Docker image |
| AWS ECS | Push image to ECR, deploy via ECS |

---

## 📊 Model Performance

| Model | Metric | Target | Achieved |
|---|---|---|---|
| Demand Forecasting (Prophet) | MAPE | ≤ 12% | ~8–12% |
| Churn Prediction (XGBoost) | AUC-ROC | ≥ 0.88 | ~0.90+ |
| Customer Segmentation (K-Means) | Silhouette | > 0.35 | ~0.40+ |
| Inventory Optimizer (EOQ) | Coverage | 100% SKUs | ✅ |

---

## 📸 Dashboard Screenshots

> *Run the pipeline and launch the dashboard to see live screenshots.*

| Page | Description |
|---|---|
| Home | Executive KPI summary, revenue trend |
| Sales Analytics | Category, channel, product breakdown |
| Demand Forecasting | 30-day forecast with confidence bands |
| Customer Segmentation | PCA scatter, RFM profiles, segment cards |
| Churn Prediction | Risk distribution, feature importance |
| Inventory Optimization | Reorder table, days-of-supply chart |
| Model Performance | MAPE comparison, AUC metrics |

---

## 🔬 MLOps Features

- **MLflow**: Experiment tracking (parameters, metrics, artifacts)
- **Evidently AI**: Data drift and model drift detection
- **Docker**: Containerised deployment
- **GitHub Actions**: Automated lint + test + build on push
- **Kubernetes**: Production-grade horizontal scaling

---

## 🔮 Future Improvements

1. **Real-time data ingestion** via Kafka / Spark Streaming
2. **LSTM / Transformer** time-series forecasting
3. **Recommendation engine** for cross-sell / upsell
4. **A/B testing framework** for marketing campaigns
5. **PostgreSQL** backend with SQLAlchemy ORM
6. **Grafana + Prometheus** monitoring dashboards
7. **Multi-tenant** SaaS deployment with authentication

---

## 📁 Notebooks

| Notebook | Content |
|---|---|
| 01_eda.ipynb | Exploratory Data Analysis |
| 02_feature_engineering.ipynb | Feature creation & analysis |
| 03_customer_segmentation.ipynb | K-Means + RFM deep dive |
| 04_demand_forecasting.ipynb | Prophet + SARIMA analysis |
| 05_churn_prediction.ipynb | Model training & SHAP plots |
| 06_inventory_optimization.ipynb | EOQ & reorder analysis |

---

## 👤 Author

**Satya Sourav Das**  
Data Science & Analytics Domain  
Zidio Development

---

## 📄 License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

---

> ⚠️ **Data Disclaimer**: All data in this project is **synthetically generated** for demonstration purposes. It does not represent real customers, products, or transactions.
