import numpy as np
import pandas as pd
from src.data.fetch import fetch_ohlcv



def build_stock_signal(df, symbol, allocation):
    """
    Converts raw df + RL action into Chief-Agent-ready signal
    """

    latest = df.iloc[-1]

    returns = df["Close"].pct_change().dropna()
    volatility = float(returns.std())

    return {
        "symbol": symbol,
        "allocation": float(allocation),
        "rsi": float(latest["rsi"]),
        "ema20": float(latest["ema20"]),
        "ema50": float(latest["ema50"]),
        "volatility": volatility,
    }
