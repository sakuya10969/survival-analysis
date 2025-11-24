import pandas as pd
from lifelines.datasets import load_lung

def load_lung_data():
    df = load_lung()

    # status: 1=死亡, 2=打ち切り → event: 1=死亡, 0=打ち切り
    df["event"] = df["status"].apply(lambda x: 1 if x == 1 else 0)
    return df
