from stable_baselines3 import PPO


class SectorAgent:
    def __init__(self, sector_name):
        self.sector = sector_name
        self.model = None

    def train(self, env, timesteps=50_000):
        self.model = PPO(
            "MlpPolicy",
            env,
            verbose=0,
            n_steps=2048,
            batch_size=64,
            gamma=0.99
        )
        self.model.learn(total_timesteps=timesteps)

    def predict(self, obs):
        action, _ = self.model.predict(obs, deterministic=True)
        return action

    def save(self, path):
        self.model.save(path)

    def load(self, path, env):
        self.model = PPO.load(path, env=env)
