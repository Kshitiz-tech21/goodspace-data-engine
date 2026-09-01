import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from app.core.config import settings

def generate_mock_data(n_users=1000, n_events=5000):
    users = [f"user_{i}" for i in range(n_users)]
    events_types = ['page_view', 'job_search', 'application_started', 'application_submitted']
    channels = ['google', 'linkedin', 'direct', 'referral']
    
    data = []
    for _ in range(n_events):
        user_id = random.choice(users)
        event = random.choice(events_types)
        # Simulate a funnel: only some who view page search, etc.
        # This is simplified mock logic
        
        timestamp = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
        salary = random.randint(40000, 200000) if random.random() > 0.1 else np.nan
        channel = random.choice(channels)
        
        data.append([user_id, event, timestamp, salary, channel])
        
    df = pd.DataFrame(data, columns=['user_id', 'event', 'timestamp', 'salary', 'channel'])
    df.to_csv(settings.DATA_RAW_PATH, index=False)
    print(f"Successfully generated mock data at {settings.DATA_RAW_PATH}")

if __name__ == "__main__":
    generate_mock_data()
