import pytest
import pandas as pd
from app.pipeline.cleaner import DataCleaner
from app.pipeline.processor import DataProcessor

def test_cleaner_outliers():
    df = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'salary': [50000, 52000, 48000, 1000000, 51000] # 1,000,000 is an outlier
    })
    cleaner = DataCleaner(contamination=0.2)
    cleaned_df = cleaner.clean(df)
    assert len(cleaned_df) < 5

def test_processor_metrics():
    df = pd.DataFrame({
        'user_id': [1, 1, 2],
        'event': ['page_view', 'application_submitted', 'page_view'],
        'salary': [50000, 50000, 60000]
    })
    metrics = DataProcessor.aggregate_metrics(df)
    assert metrics['total_users'] == 2
    assert metrics['conversion_rate'] == 0.5
