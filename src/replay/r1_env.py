import gymnasium as gym

from gymnasium import spaces
import numpy as np
import pandas as pd

class TradingEnv(gym.Env):
    """Gym environment for single-stock trading using precomputed features."""
    
    metadata = {"render.modes": ["human"]}

    def __init__(self, feature_file, initial_cash=100000):
        super().__init__()
        self.df = pd.read_parquet(feature_file).reset_index()
        self.n_steps = len(self.df)
        self.initial_cash = initial_cash

        # Action space: 0 = Hold, 1 = Buy, 2 = Sell
        self.action_space = spaces.Discrete(3)

        # Observation: [Close, EMA20, EMA50, RSI, Position]
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(5,), dtype=np.float32
        )

        self.reset()

    def reset(self):
        self.i = 0
        self.position = 0  # 1 = long, -1 = short, 0 = flat
        self.cash = self.initial_cash
        self.entry_price = 0
        self.pnl = 0
        return self._get_obs()

    def _get_obs(self):
        row = self.df.iloc[self.i]
        return np.array([
            row.Close,
            row.ema20,
            row.ema50,
            row.rsi,
            self.position
        ], dtype=np.float32)

    def step(self, action):
        row = self.df.iloc[self.i]
        price = row.Close
        reward = 0.0

        # Execute action
        if action == 1 and self.position <= 0:  # Buy
            self.position = 1
            self.entry_price = price
        elif action == 2 and self.position >= 0:  # Sell
            self.position = -1
            self.entry_price = price

        # Calculate unrealized PnL
        if self.position == 1:
            self.pnl = self.cash * (price / self.entry_price - 1)
        elif self.position == -1:
            self.pnl = self.cash * (self.entry_price / price - 1)
        else:
            self.pnl = 0.0

        reward = self.pnl  # reward = current PnL
        self.i += 1
        done = self.i >= self.n_steps
        return self._get_obs(), reward, done, {}

    def render(self, mode="human"):
        row = self.df.iloc[self.i-1]
        print(f"{row.Date} | Price: {row.Close:.2f} | Pos: {self.position} | PnL: {self.pnl:.2f}")
