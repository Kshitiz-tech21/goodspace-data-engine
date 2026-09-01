import pandas as pd
import numpy as np

class CohortEngine:
    @staticmethod
    def calculate_retention(df: pd.DataFrame):
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['cohort_month'] = df.groupby('user_id')['timestamp'].transform('min').dt.to_period('M')
        df['event_month'] = df['timestamp'].dt.to_period('M')
        
        cohorts = df.groupby(['cohort_month', 'event_month']).agg(n_customers=('user_id', 'nunique')).reset_index()
        cohorts['period_number'] = (cohorts.event_month - cohorts.cohort_month).apply(lambda x: x.n)
        
        pivot = cohorts.pivot(index='cohort_month', columns='period_number', values='n_customers')
        cohort_size = pivot.iloc[:, 0]
        retention = pivot.divide(cohort_size, axis=0)
        
        return retention
