import streamlit as st
import pandas as pd
import plotly.express as px
from app.core.config import settings
from app.pipeline.processor import DataProcessor
from app.engine.cohorts import CohortEngine
from app.engine.funnels import FunnelEngine

st.set_page_config(page_title="GoodSpace AI Autonomous Dashboard", layout="wide")

st.title("🚀 GoodSpace AI Data Engine")
st.sidebar.header("Controls")

try:
    df = pd.read_csv(settings.DATA_RAW_PATH)
    
    st.subheader("Key Performance Indicators")
    metrics = DataProcessor.aggregate_metrics(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Users", metrics['total_users'])
    col2.metric("Avg Salary", f"${metrics['avg_salary']:,.2f}")
    col3.metric("Conv Rate", f"{metrics['conversion_rate']:.2%}")

    st.subheader("User Retention Cohorts")
    retention = CohortEngine.calculate_retention(df)
    st.dataframe(retention)
    
    st.subheader("Job-Matching Funnel")
    steps = ['page_view', 'job_search', 'application_started', 'application_submitted']
    funnel_data = FunnelEngine.calculate_drop_offs(df, steps)
    
    fig = px.bar(
        x=list(funnel_data['counts'].keys()), 
        y=list(funnel_data['counts'].values()), 
        labels={'x': 'Step', 'y': 'Users'},
        title="Funnel Conversion"
    )
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error(f"Raw data file not found at {settings.DATA_RAW_PATH}. Please run mock_generator.py first.")
