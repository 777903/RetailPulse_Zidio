# RetailPulse – Exploratory Data Analysis
# Notebook: 01_eda.ipynb (placeholder)
# Run `jupyter notebook` and open this file, or convert to .ipynb with:
#   pip install jupytext && jupytext --to notebook 01_eda.py

# %% [markdown]
# # RetailPulse – Exploratory Data Analysis
# **Author**: Satya Sourav Das | **For**: Zidio Development
#
# ⚠️ *All data is synthetic*

# %%
import sys
sys.path.insert(0, '..')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from src.config import ensure_dirs, SALES_CLEAN_FILE, CUSTOMER_CLEAN_FILE, INVENTORY_CLEAN_FILE
from src.data_ingestion import load_or_generate_data, save_raw_data
from src.preprocessing import run_preprocessing

ensure_dirs()

# %% [markdown]
# ## 1. Load Data

# %%
sales_raw, customers_raw, inventory_raw = load_or_generate_data()
save_raw_data(sales_raw, customers_raw, inventory_raw)
sales, customers, inventory = run_preprocessing(sales_raw, customers_raw, inventory_raw, save=True)
print(f"Sales: {sales.shape}  |  Customers: {customers.shape}  |  Inventory: {inventory.shape}")

# %% [markdown]
# ## 2. Sales Overview

# %%
print(sales.describe())
print("\nDate range:", sales["invoice_date"].min(), "–", sales["invoice_date"].max())
print("Total revenue: ₹{:,.2f}".format(sales["total_amount"].sum()))

# %%
# Monthly revenue trend
monthly = sales.groupby(sales["invoice_date"].dt.to_period("M"))["total_amount"].sum()
monthly.plot(figsize=(14, 5), title="Monthly Revenue Trend", color="#6C63FF")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("../reports/figures/monthly_revenue.png", dpi=150)
plt.show()

# %%
# Category breakdown
cat_rev = sales.groupby("product_category")["total_amount"].sum().sort_values(ascending=True)
cat_rev.plot(kind="barh", figsize=(10, 6), title="Revenue by Category", color="#43D9B0")
plt.tight_layout()
plt.savefig("../reports/figures/category_revenue.png", dpi=150)
plt.show()

# %% [markdown]
# ## 3. Customer Overview

# %%
print(customers.describe(include="all"))
customers["age"].hist(bins=20, figsize=(8, 4), color="#6C63FF", edgecolor="white")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.savefig("../reports/figures/customer_age_dist.png", dpi=150)
plt.show()

# %% [markdown]
# ## 4. Inventory Overview

# %%
print(inventory.describe())
print("\nStock status:")
print((inventory["current_stock"] == 0).sum(), "products out of stock")
print((inventory["current_stock"] <= inventory["reorder_level"]).sum(), "products at/below reorder level")

# %% [markdown]
# ## 5. Summary Statistics

# %%
summary = {
    "Total Revenue": f"₹{sales['total_amount'].sum():,.0f}",
    "Total Transactions": f"{sales['invoice_id'].nunique():,}",
    "Unique Customers": f"{sales['customer_id'].nunique():,}",
    "Unique Products": f"{sales['product_id'].nunique():,}",
    "Avg Order Value": f"₹{sales['total_amount'].mean():,.2f}",
    "Date Range": f"{sales['invoice_date'].min().date()} → {sales['invoice_date'].max().date()}",
}
for k, v in summary.items():
    print(f"{k:25s}: {v}")
