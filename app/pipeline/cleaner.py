import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from app.core.config import settings

class DataCleaner:
    def __init__(self, contamination=0.05):
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # Numerical columns for outlier detection
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if not num_cols:
            return df

        # Outlier detection
        df['outlier'] = self.model.fit_predict(df[num_cols].fillna(df[num_cols].median()))
        df = df[df['outlier'] == 1].drop(columns=['outlier'])

        # Imputation for missing salary/revenue
        for col in num_cols:
            if df[col].isnull().any():
                df[col] = df[col].fillna(df[col].median())

        return df
