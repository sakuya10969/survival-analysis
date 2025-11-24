import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
import os

def plot_km(df, time_col, event_col, save_path=None):
    T = df[time_col]
    E = df[event_col]

    kmf = KaplanMeierFitter()
    kmf.fit(T, E)

    ax = kmf.plot_survival_function()
    plt.title("Kaplan-Meier Survival Curve")
    plt.xlabel("Time")
    plt.ylabel("Survival probability")
    plt.grid(True)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.close()
