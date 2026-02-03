import time
from src.execution.openalgo_executor import place_order, stay_flat


class IntradayTradingAgent:
    def __init__(self, cooldown=300):
        self.last_trade_time = 0
        self.cooldown = cooldown  # seconds

    def execute(self, signal: dict):
        """
        signal = {
            "action": BUY / SELL / NO_TRADE,
            "symbol": "SBIN",
            "qty": 1
        }
        """

        if signal["action"] == "NO_TRADE":
            return stay_flat()

        if time.time() - self.last_trade_time < self.cooldown:
            return stay_flat()

        self.last_trade_time = time.time()

        return place_order(
            symbol=signal["symbol"],
            side=signal["action"],
            quantity=signal["qty"]
        )
