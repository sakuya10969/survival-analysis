from src.plots.km_plot import plot_km
from src.config import FIGURES_DIR

def run_km(df):
    save_path = FIGURES_DIR / "km_lung.png"
    plot_km(df, "time", "event", save_path)
    print(f"[KM] Saved to {save_path}")
