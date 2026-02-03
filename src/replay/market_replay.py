import pandas as pd

class MarketReplay:
    def __init__(self, feature_file):
        self.df = pd.read_parquet(feature_file).reset_index()
        self.i = 0
        self.position = 0
        self.cash = 100000
        self.entry_price = 0
        self.pnl = 0

    def reset(self):
        self.i = 0
        self.position = 0
        self.cash = 100000
        self.entry_price = 0
        self.pnl = 0

    def step(self):
        if self.i >= len(self.df):
            return None

        row = self.df.iloc[self.i]
        sig = row.signal
        price = row.Close

        if sig == 1 and self.position <= 0:  # Buy
            self.position = 1
            self.entry_price = price
            print(f"{row.Date} BUY at {price:.2f}")
        elif sig == -1 and self.position >= 0:  # Sell
            self.position = -1
            self.entry_price = price
            print(f"{row.Date} SELL at {price:.2f}")

        # Simple unrealized PnL
        if self.position == 1:
            self.pnl = self.cash * (price / self.entry_price - 1)
        elif self.position == -1:
            self.pnl = self.cash * (self.entry_price / price - 1)

        self.i += 1
        return row
