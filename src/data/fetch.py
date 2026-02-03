import sys
import yfinance as yf
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))  # adds C:\trading_ai to sys.path

from src.data.indicators import add_indicators
from src.data.signals import signal
from config.settings import FEATURE_DIR




def get_data(symbol, start="2023-01-01"):
    df = yf.download(symbol, start=start, progress=False)
    df.dropna(inplace=True)
    return df

def build_features(symbol):
    df = get_data(symbol)
    df = add_indicators(df)
    df["signal"] = df.apply(signal, axis=1)
    return df

if __name__ == "__main__":
    symbol = "RELIANCE.NS"
    df = build_features(symbol)
    print(df.tail())
    df.to_parquet(FEATURE_DIR / f"{symbol}_features.parquet")
    print(f"Saved features to {FEATURE_DIR}")
