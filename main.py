from src.data.fetch import build_features
from src.data.feeds.long_term_feed import build_stock_signal
from src.agents.sector_agent import SectorAgent
from src.agents.chief_agent import ChiefAgent
from src.configs.sectors import SECTORS
import os


MODELS_DIR = "models"


def ensure_dirs():
    os.makedirs(MODELS_DIR, exist_ok=True)


def run_long_term_pipeline():
    ensure_dirs()

    all_sector_outputs = []

    for sector, symbols in SECTORS.items():
        print(f"\n=== SECTOR: {sector} ===")

        for symbol in symbols:
            print(f"Processing {symbol}")

            # 1. Build features
            df = build_features(symbol)

            # 2. Init sector agent
            agent = SectorAgent(sector, df)

            model_path = f"{MODELS_DIR}/{sector}_{symbol}"

            # 3. Train or load model
            if os.path.exists(model_path + ".zip"):
                agent.load(model_path)
            else:
                agent.train(timesteps=30_000)
                agent.save(model_path)

            # 4. Get latest observation
            obs, _ = agent.env.reset()
            action = agent.predict(obs)

            # 5. Build signal for Chief Agent
            signal = build_stock_signal(
                df=df,
                symbol=symbol,
                allocation=action[0],
            )

            all_sector_outputs.append(signal)

    # 6. Chief Agent decision
    chief = ChiefAgent(max_stocks=5)
    final_portfolio = chief.select_portfolio(all_sector_outputs)

    print("\n🔥 FINAL LONG-TERM PORTFOLIO 🔥")
    for stock in final_portfolio:
        print(
            stock["symbol"],
            "weight:",
            round(stock["weight"], 3),
            "score:",
            round(stock["score"], 2),
        )


if __name__ == "__main__":
    run_long_term_pipeline()
