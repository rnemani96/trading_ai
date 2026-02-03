from src.data.fetch import load_market_data
from src.data.indicators import build_features
from src.agents.sector_agent import SectorAgent
from src.agents.chief_agent import ChiefAgent
from src.agents.intraday_regime_agent import IntradayRegimeAgent

def main():
    df = load_market_data()
    df = build_features(df)

    sector_agent = SectorAgent()
    sector_report = sector_agent.analyze(df)

    chief = ChiefAgent()
    long_term_stocks = chief.select(sector_report)

    regime_agent = IntradayRegimeAgent()
    regime = regime_agent.classify(df)

    print("Stocks:", long_term_stocks)
    print("Regime:", regime)

if __name__ == "__main__":
    main()
