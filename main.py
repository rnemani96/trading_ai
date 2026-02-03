from src.data.fetch import build_features
from src.agents.sector_agent import SectorAgent
from src.configs.sectors import SECTORS


def run_sector_agents():
    for sector, symbols in SECTORS.items():
        print(f"Training sector: {sector}")

        for symbol in symbols:
            df = build_features(symbol)
            agent = SectorAgent(sector, df)
            agent.train()
            agent.save(f"models/{sector}_{symbol}")


if __name__ == "__main__":
    run_sector_agents()
