from pathlib import Path
from src.replay.market_replay import MarketReplay

FEATURE_FILE = Path("D:/trading_ai/tmp/RELIANCE.NS_features.parquet")

engine = MarketReplay(FEATURE_FILE)

while True:
    candle = engine.step()
    if candle is None:
        break

print(f"Final PnL: {engine.pnl:.2f}")
