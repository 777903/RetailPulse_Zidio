"""
app.py  –  RetailPulse Navigation Shell
Uses st.navigation() so app.py itself is INVISIBLE in the sidebar.
Only the 6 declared pages appear in the navigation.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

# ── Cloud Initialization ──────────────────────────────────────────────────────
from src.config import SALES_CLEAN_FILE
if not SALES_CLEAN_FILE.exists():
    st.info("Initializing sample dataset for the first time... This will take a few moments.")
    with st.spinner("Generating synthetic data and training ML models..."):
        import main
        class Args:
            pass
        args = Args()
        args.generate_data = False
        args.preprocess = False
        args.feature_engineering = False
        args.train_segmentation = False
        args.train_forecasting = False
        args.train_churn = False
        args.inventory = False
        args.evaluate = False
        args.train_all = False
        args.all = True
        args.force_generate = False
        
        main.run_pipeline(args)
    st.success("Initialization complete!")
    st.rerun()

# ── Programmatic navigation: app.py is the shell, NOT a visible page ──────────
pages = [
    st.Page("pages/1_Sales_Analytics.py",        title="Sales Analytics",       icon="📈"),
    st.Page("pages/2_Demand_Forecasting.py",      title="Demand Forecasting",    icon="🔮"),
    st.Page("pages/3_Customer_Segmentation.py",   title="Customer Segmentation", icon="👥"),
    st.Page("pages/4_Churn_Prediction.py",        title="Churn Prediction",      icon="⚠️"),
    st.Page("pages/5_Inventory_Optimization.py",  title="Inventory Optimization",icon="📦"),
    st.Page("pages/6_Model_Performance.py",       title="Model Performance",     icon="🎯"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
