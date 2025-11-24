from src.load_data import load_lung_data
from src.analysis.km import run_km

def main():
    df = load_lung_data()
    run_km(df)

if __name__ == "__main__":
    main()
