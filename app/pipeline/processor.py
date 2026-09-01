import pandas as pd
import numpy as np
from app.core.config import settings

class DataProcessor:
    @staticmethod
    def aggregate_metrics(df: pd.DataFrame):
        metrics = {
            "total_users": df['user_id'].nunique(),
            "avg_salary": df['salary'].mean() if 'salary' in df.columns else 0,
            "conversion_rate": (df['event'].value_counts().get('application_submitted', 0) / 
                                df['user_id'].nunique()) if not df.empty else 0
        }
        return metrics

    @staticmethod
    def process_clickstream(df: pd.DataFrame):
        return df.sort_values(by=['user_id', 'timestamp'])
