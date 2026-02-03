import gymnasium as gym

from stable_baselines3 import PPO
from pathlib import Path
from src.replay.r1_env import TradingEnv

# Path to your features
FEATURE_FILE = Path("D:/trading_ai/tmp/RELIANCE.NS_features.parquet")

# Create environment
env = TradingEnv(FEATURE_FILE)

# Create PPO agent
model = PPO("MlpPolicy", env, verbose=1)

# Train the agent
model.learn(total_timesteps=5000)

# Save model
model.save("ppo_trading_agent")
print("Model trained and saved as ppo_trading_agent.zip")

# Test the trained agent
obs = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    env.render()
