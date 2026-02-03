from src.agents.intraday_regime_agent import IntradayRegimeAgent
from src.intraday.trading_agent import IntradayTradingAgent
from src.intraday.strategies import trend_strategy, mean_reversion_strategy


class IntradayController:
    def __init__(self):
        self.regime_agent = IntradayRegimeAgent()
        self.trader = IntradayTradingAgent()

    def run(self, df, symbol):
        regime = self.regime_agent.classify(df)

        if regime == "TREND":
            signal = trend_strategy(df, symbol)

        elif regime == "RANGE":
            signal = mean_reversion_strategy(df, symbol)

        else:
            signal = {"action": "NO_TRADE"}

        return self.trader.execute(signal)
