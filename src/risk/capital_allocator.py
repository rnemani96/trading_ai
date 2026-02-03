class CapitalAllocator:
    def __init__(self, max_per_trade=0.02, sector_cap=0.25):
        self.max_per_trade = max_per_trade
        self.sector_cap = sector_cap

    def size_trade(self, portfolio, trade):
        capital = portfolio.capital
        trade["amount"] = capital * self.max_per_trade
        return trade
