from src.data.feed import load_market_data
from src.data.features import build_features

from src.agents.sector_agent import SectorAgent
from src.agents.chief_agent import ChiefAgent
from src.agents.intraday_regime_agent import IntradayRegimeAgent

from src.envs.long_term_env import LongTermEnv
from src.execution.intraday_executor import execute_intraday_trade
from src.execution.openalgo_client import OpenAlgoClient


def run_long_term_pipeline():
    print("📊 Running Long-Term Investment Pipeline")

    # Load & prepare data
    df = load_market_data(mode="long_term")
    df = build_features(df)

    # Sector analysis
    sector_agent = SectorAgent()
    sector_reports = sector_agent.analyze(df)

    # Chief agent decides final stocks
    chief_agent = ChiefAgent()
    final_stocks = chief_agent.select_long_term_stocks(sector_reports)

    print("✅ Long-term selected stocks:", final_stocks)
    return final_stocks


def run_intraday_pipeline():
    print("⚡ Running Intraday Trading Pipeline")

    # Load & prepare intraday data
    df = load_market_data(mode="intraday")
    df = build_features(df)

    # Regime detection
    regime_agent = IntradayRegimeAgent()
    regime = regime_agent.classify(df)

    print(f"📈 Market Regime: {regime}")

    if regime == "TREND":
        strategy = "trend_following"
    elif regime == "RANGE":
        strategy = "mean_reversion"
    else:
        print("🛑 No-trade regime detected")
        return

    # Execute trade via OpenAlgo
    broker = OpenAlgoClient()
    execute_intraday_trade(df, strategy, broker)


def main():
    print("🚀 Trading AI System Started")

    # Long-term investment decision
    run_long_term_pipeline()

    # Intraday trading execution
    run_intraday_pipeline()

    print("🏁 Trading AI System Finished")


if MODE == "PAPER":
    executor = PaperExecutor()
else:
    executor = OpenAlgoExecutor()


if __name__ == "__main__":
    main()
