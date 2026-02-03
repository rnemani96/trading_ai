import numpy as np


class IntradayRegimeAgent:
    """
    Rule-based (fast & reliable)
    Can be upgraded to RL later
    """

    def __init__(self):
        pass

    def classify(self, df):
        """
        df must contain:
        Close, ema20, ema50, rsi
        """

        latest = df.iloc[-1]
        prev = df.iloc[-2]

        # Trend strength
        trend_strength = abs(latest["ema20"] - latest["ema50"]) / latest["Close"]

        # Volatility (last 20 candles)
        returns = df["Close"].pct_change().dropna()
        volatility = returns[-20:].std()

        # RSI movement
        rsi_change = abs(latest["rsi"] - prev["rsi"])

        # ---- Regime rules ----
        if volatility > 0.02:
            return "VOLATILE"

        if trend_strength > 0.005 and 40 < latest["rsi"] < 70:
            return "TREND"

        return "RANGE"
