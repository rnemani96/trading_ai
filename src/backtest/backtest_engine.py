class BacktestEngine:
    def run(self, df, strategy):
        pnl = 0
        for _, row in df.iterrows():
            signal = strategy(row)
            pnl += signal * row["Close"]
        return pnl
