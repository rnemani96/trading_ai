from config.settings import MODE

# ===== Data =====
from src.data.fetch import load_market_data
from src.data.indicators import add_indicators
from src.data.signals import add_signals

# ===== Agents =====
from src.agents.sector_agent import SectorAgent
from src.agents.chief_agent import ChiefAgent
from src.agents.intraday_regime_agent import IntradayRegimeAgent

# ===== Risk & Execution =====
from src.risk.risk_manager import RiskManager
from src.execution.paper_executor import PaperExecutor
from src.execution.openalgo_executor import OpenAlgoExecutor

# ===== Intraday =====
from src.intraday.controller import execute_intraday_strategy


# --------------------------------------------------
# LONG-TERM PIPELINE
# --------------------------------------------------
def run_long_term_pipeline():
    print("📊 Running Long-Term Investment Pipeline")

    df = load_market_data(mode="long_term")
    df = add_indicators(df)
    df = add_signals(df)

    sector_agent = SectorAgent()
    sector_reports = sector_agent.analyze(df)

    chief_agent = ChiefAgent()
    long_term_trades = chief_agent.select_long_term_stocks(sector_reports)

    print("✅ Long-term decisions:", long_term_trades)
    return long_term_trades, chief_agent


# --------------------------------------------------
# INTRADAY PIPELINE
# --------------------------------------------------
def run_intraday_pipeline(executor, risk_manager):
    print("⚡ Running Intraday Trading Pipeline")

    df = load_market_data(mode="intraday")
    df = add_indicators(df)

    regime_agent = IntradayRegimeAgent()
    regime = regime_agent.classify(df)

    print(f"📈 Market Regime: {regime}")

    if regime == "NO_TRADE":
        print("🛑 No-trade regime detected")
        return

    trades = execute_intraday_strategy(df, regime)

    for trade in trades:
        if risk_manager.approve_trade(trade):
            executor.execute(trade)
        else:
            print("🚨 Trade blocked by RiskManager")


# --------------------------------------------------
# MAIN
# --------------------------------------------------
def main():
    print("🚀 Trading AI System Started")

    executor = PaperExecutor() if MODE == "PAPER" else OpenAlgoExecutor()
    risk_manager = RiskManager()

    # Long-term
    _, chief_agent = run_long_term_pipeline()

    # Intraday
    run_intraday_pipeline(executor, risk_manager)

    print("🏁 Trading AI System Finished")


if __name__ == "__main__":
    main()
