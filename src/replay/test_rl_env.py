from pathlib import Path
from src.replay.r1_env import TradingEnv

FEATURE_FILE = Path("D:/trading_ai/tmp/RELIANCE.NS_features.parquet")

env = TradingEnv(FEATURE_FILE)

obs = env.reset()
done = False

while not done:
    action = env.action_space.sample()  # random action
    obs, reward, done, _ = env.step(action)
    env.render()
