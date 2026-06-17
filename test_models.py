# RetailPulse – Demo Video Script
## 6-Minute Professional Demo

**Author**: Satya Sourav Das  
**Platform**: RetailPulse – AI-Powered Customer Analytics & Demand Forecasting  
**For**: Zidio Development – Data Science & Analytics Domain  
**Duration**: ~6 minutes

---

## [0:00–0:30] Opening / Title Slide

**[Screen: Project title slide with RetailPulse logo]**

> "Hello everyone! My name is Satya Sourav Das, and I'm excited to present RetailPulse – an AI-powered customer analytics and demand forecasting platform that I built for Zidio Development's Data Science and Analytics domain.
>
> RetailPulse solves four real-world retail problems: demand uncertainty, customer churn, inventory inefficiency, and scattered analytics — all in one unified ML-powered platform."

---

## [0:30–1:00] Business Problem

**[Screen: Problem slide / executive summary KPI page]**

> "Let me quickly frame the business problem.
>
> Retail businesses lose millions annually from stockouts, overstock, and customer churn. Studies show that:
> - Stockouts cause up to 8% annual revenue loss
> - Acquiring a new customer costs 5× more than retaining an existing one
> - Overstock ties up working capital and leads to markdowns
>
> RetailPulse addresses all of these using machine learning, starting from raw transaction data all the way to automated recommendations — giving business teams answers in minutes, not days."

---

## [1:00–1:30] Dataset & Pipeline Overview

**[Screen: project folder structure + terminal running `python main.py`]**

> "The platform uses a synthetic retail dataset with over 12,000 transactions, 1,200 customers, and 120 products spanning 24 months — generated to simulate realistic retail seasonality, including a 40% Q4 sales boost.
>
> The full pipeline runs with a single command: `python main.py`.
>
> This triggers 8 automated steps:
> data generation → preprocessing → feature engineering → segmentation → forecasting → churn prediction → inventory optimization → model evaluation report.
>
> Everything saves automatically to structured folders — processed data, model artifacts, and metric reports."

---

## [1:30–2:15] Dashboard Walkthrough – Home Page

**[Screen: Streamlit dashboard home page]**

> "Here's the live RetailPulse dashboard running on Streamlit. Notice the clean dark theme with our brand purple and teal accent colors.
>
> The executive summary shows 8 KPI cards at a glance:
> - Total Revenue: ₹15.2M
> - 1,200+ active customers
> - 12,000+ orders
> - Average order value of ₹2,100
> - Churn rate of 31%
> - 18 SKUs flagged for immediate reorder
>
> Below, we have the monthly revenue trend — note the clear Q4 seasonality spike — and a revenue breakdown by product category."

---

## [2:15–3:00] Demand Forecasting

**[Screen: Demand Forecasting page, selecting 'Electronics' category]**

> "Let's jump into demand forecasting. I'll select the Electronics category.
>
> The chart shows 90 days of historical daily demand in purple, and the 30-day forecast in teal dashed line. The vertical red line marks where the forecast begins.
>
> The model used here is Prophet — Facebook's open-source time series library — which captures weekly and yearly seasonality automatically.
>
> Looking at the metrics panel: MAPE is 9.2%, MAE is 12.4 units, and RMSE is 18.7 — well within our target of MAPE ≤ 12%.
>
> The comparison chart on the right shows MAPE across all 10 product categories. The red dashed line marks our 12% target threshold."

---

## [3:00–3:45] Customer Segmentation

**[Screen: Customer Segmentation page]**

> "Now customer segmentation. Using RFM analysis combined with K-Means clustering, we've identified 7 distinct customer groups.
>
> The PCA scatter plot maps all 1,200 customers into 2-dimensional space — each colour is a different segment. You can clearly see the separation between Champion customers in green and Dormant customers in red.
>
> The donut chart shows the segment distribution — Champions represent 12% of customers but drive a disproportionate share of revenue.
>
> Scroll down and we see interpretation cards for each segment. For At-Risk customers, the platform recommends: 'Send personalised win-back campaigns.' For Champions: 'Reward them — they can become brand ambassadors.'
>
> Everything here is downloadable as a CSV for your CRM team."

---

## [3:45–4:30] Churn Prediction

**[Screen: Churn Prediction page]**

> "For churn prediction, the platform identifies customers who haven't purchased in 90+ days.
>
> We trained three models: Logistic Regression, Random Forest, and XGBoost. The best model — XGBoost — achieved an AUC-ROC of 0.91, exceeding our 0.88 target.
>
> The feature importance chart shows that recency_days is the single strongest churn predictor, followed by purchase_freq_per_month and CLV estimate.
>
> The risk distribution shows 320 customers flagged as High Risk — these are the customers your retention team should call first.
>
> The high-risk customer list at the bottom is filterable and downloadable — ready to plug directly into your CRM or email marketing system."

---

## [4:30–5:00] Inventory Optimization

**[Screen: Inventory Optimization page]**

> "Inventory optimization uses the demand forecast output to calculate:
> - Safety stock at 95% service level
> - Reorder point per SKU
> - EOQ-based reorder quantity
>
> The action pie chart summarises the current inventory health: 15 SKUs need immediate reorder, 8 need monitoring, 12 are overstocked, and the remainder are healthy.
>
> The bar chart compares current stock versus reorder point for the most critical products — you can instantly see which SKUs are dangerously below their threshold.
>
> The full recommendations table is sortable by urgency score and downloadable as CSV for your procurement team."

---

## [5:00–5:30] MLOps & Deployment

**[Screen: terminal running docker-compose, then MLflow UI]**

> "On the MLOps side, the platform is fully containerised with Docker. A single `docker-compose up` command starts the dashboard on port 8501.
>
> MLflow tracks every training run — parameters, metrics, and model artifacts — so you can compare experiments and roll back if needed.
>
> The GitHub Actions CI/CD pipeline automatically runs linting and unit tests on every push, and builds the Docker image on merges to main.
>
> For production scale, Kubernetes deployment YAML files are included for horizontal scaling with 2 replicas and a LoadBalancer service."

---

## [5:30–6:00] Summary & Closing

**[Screen: Model Performance page → business impact cards]**

> "Let me quickly summarise what RetailPulse delivers:
>
> - Demand Forecasting MAPE: ~8–12% ✅
> - Churn AUC-ROC: ~0.91 ✅
> - 6–8 interpretable customer segments ✅
> - 100% inventory coverage with action labels ✅
> - 7 interactive dashboard pages with download buttons ✅
>
> And projected business impact:
> - 30–50% stockout reduction
> - 15–25% revenue uplift through targeted marketing
> - 20–35% churn reduction
> - 25–40% inventory efficiency gain
>
> The entire project is open source, portfolio-ready, and deployable in under 5 minutes with Docker.
>
> Thank you for watching! The GitHub link and Streamlit demo are in the description. I'm Satya Sourav Das — this was RetailPulse for Zidio Development."

---

## Production Tips for Recording

1. **Resolution**: Record at 1920×1080 minimum
2. **Browser**: Chrome, zoom 80% for dashboard visibility
3. **Terminal font**: Size 16+ for readability
4. **Transitions**: Use OBS scene transitions between sections
5. **Background music**: Subtle lo-fi at 10% volume
6. **Captions**: Auto-generate with Descript or CapCut
7. **Thumbnail**: Dark background, RetailPulse logo, "AI Retail Analytics" text
