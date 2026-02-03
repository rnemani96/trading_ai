class RiskManager:
    def __init__(self, capital, max_risk=0.02):
        self.capital = capital
        self.max_risk = max_risk

    def approve_trade(self, price, stop_loss, qty):
        risk = abs(price - stop_loss) * qty
        return risk <= self.capital * self.max_risk
