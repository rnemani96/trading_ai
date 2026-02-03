import numpy as np


class ChiefAgent:
    def __init__(self, max_stocks=5):
        self.max_stocks = max_stocks

    def score_stock(self, stock_signal):
        """
        stock_signal = {
            'symbol': str,
            'allocation': float,
            'rsi': float,
            'ema20': float,
            'ema50': float,
            'volatility': float
        }
        """

        score = 0.0

        # RL confidence
        score += stock_signal["allocation"] * 2.0

        # Trend
        if stock_signal["ema20"] > stock_signal["ema50"]:
            score += 1.0

        # RSI health
        if 35 < stock_signal["rsi"] < 60:
            score += 1.0
        elif stock_signal["rsi"] > 70:
            score -= 1.0

        # Volatility penalty
        score -= stock_signal["volatility"] * 0.5

        return score

    def select_portfolio(self, stock_signals):
        """
        stock_signals = list of dicts
        """

        scored = []
        for s in stock_signals:
            s["score"] = self.score_stock(s)
            scored.append(s)

        scored.sort(key=lambda x: x["score"], reverse=True)

        selected = scored[: self.max_stocks]

        total_score = sum(max(s["score"], 0.01) for s in selected)

        for s in selected:
            s["weight"] = max(s["score"], 0.01) / total_score

        return selected
