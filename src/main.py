from config.settings import MODE

from src.data.fetch import load_market_data
from src.data.indicators import add_indicators
from src.data.signals import add_signals

from src.agents.sector_agent import SectorAgent
from src.agents.chief_agent import ChiefAgent
from src.agents.intraday_regime_agent import IntradayRegimeAgent

from src.risk.risk_manager import RiskManager
from src.execution.paper_executor import PaperExecutor
from src.execution.openalgo_executor import OpenAlgoExecutor
from src.monitor.monitor import Monitor

from src.intraday.controller import execute_intraday_strategy


def main():
    print("🚀 Trading AI System Started")

    monitor = Monitor()
    risk_manager = RiskManager()
    executor = PaperExecutor() if MODE == "PAPER" else OpenAlgoExecutor()

    try:
        # -------- LONG TERM --------
        df_long = load_market_data(mode="long_term")
        df_long = add_indicators(df_long)
        df_long = add_signals(df_long)

        sector_agent = SectorAgent()
        sector_reports = sector_agent.analyze(df_long)

        chief_agent = ChiefAgent()
        long_term_trades = chief_agent.select_long_term_stocks(sector_reports)

        for trade in long_term_trades:
            if risk_manager.approve_trade(trade):
                executor.execute(trade)

        # -------- INTRADAY --------
        df_intra = load_market_data(mode="intraday")
        df_intra = add_indicators(df_intra)

        regime_agent = IntradayRegimeAgent()
        regime = regime_agent.classify(df_intra)

        if regime != "NO_TRADE":
            intraday_trades = execute_intraday_strategy(df_intra, regime)

            for trade in intraday_trades:
                if risk_manager.approve_trade(trade):
                    executor.execute(trade)

    except Exception as e:
        monitor.alert(f"SYSTEM HALTED: {e}")

    print("🏁 Trading AI System Finished")


if __name__ == "__main__":
    main()
