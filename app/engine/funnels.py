import pandas as pd

class FunnelEngine:
    @staticmethod
    def calculate_drop_offs(df: pd.DataFrame, steps: list):
        funnel_counts = {}
        for step in steps:
            count = df[df['event'] == step]['user_id'].nunique()
            funnel_counts[step] = count
            
        # Calculate drop-off percentages
        drop_offs = {}
        counts = list(funnel_counts.values())
        for i in range(len(counts) - 1):
            step_name = steps[i]
            drop_off = 1 - (counts[i+1] / counts[i]) if counts[i] > 0 else 1
            drop_offs[f"{step_name}_to_{steps[i+1]}"] = drop_off
            
        return {"counts": funnel_counts, "drop_offs": drop_offs}
