from stable_baselines3 import PPO
from src.envs.long_term_env import LongTermInvestEnv


class SectorAgent:
    def __init__(self, sector_name, df):
        self.sector = sector_name
        self.env = LongTermInvestEnv(df)

        self.model = PPO(
            "MlpPolicy",
            self.env,
            verbose=0,
            n_steps=2048,
            batch_size=64,
            gamma=0.99
        )

    def train(self, timesteps=50_000):
        self.model.learn(total_timesteps=timesteps)

    def predict(self, obs):
        action, _ = self.model.predict(obs, deterministic=True)
        return action

    def save(self, path):
        self.model.save(path)

    def load(self, path):
        self.model = PPO.load(path, env=self.env)
