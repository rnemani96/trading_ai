from src.agents.intraday_regime_agent import IntradayRegimeAgent
from src.intraday.strategies import (
    trend_strategy,
    mean_reversion_strategy,
)
from src.execution.openalgo_executor import stay_flat


class IntradayController:
    def __init__(self):
        self.regime_agent = IntradayRegimeAgent()

    def run(self, df):
        """
        df = intraday OHLCV + indicators
        """

        regime = self.regime_agent.classify(df)

        if regime == "TREND":
            return trend_strategy(df)

        if regime == "RANGE":
            return mean_reversion_strategy(df)

        return stay_flat()
