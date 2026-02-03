import pandas as pd
import ta

def add_indicators(df):
    # Ensure 'Close' is 1D series
    close = df["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    df["ema20"] = ta.trend.ema_indicator(close, 20)
    df["ema50"] = ta.trend.ema_indicator(close, 50)
    df["rsi"] = ta.momentum.rsi(close, 14)

    return df.dropna()
