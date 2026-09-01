import pandas as pd
import json
from app.core.config import settings

class FeatureStore:
    @staticmethod
    def export_to_parquet(df: pd.DataFrame):
        df.to_parquet(settings.DATA_PROCESSED_PATH, index=False)
        return settings.DATA_PROCESSED_PATH

    @staticmethod
    def export_to_json(df: pd.DataFrame):
        result = df.to_dict(orient='records')
        path = settings.DATA_PROCESSED_PATH.replace('.parquet', '.json')
        with open(path, 'w') as f:
            json.dump(result, f, indent=4)
        return path
