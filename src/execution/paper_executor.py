class PaperExecutor:
    def __init__(self):
        self.trades = []

    def place_order(self, symbol, side, qty, price):
        self.trades.append({
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price
        })
