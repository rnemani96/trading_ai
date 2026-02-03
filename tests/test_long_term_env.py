import pandas as pd
from src.envs.long_term_env import LongTermInvestEnv

def test_env_step():
    df = pd.DataFrame({
        "Close": [100, 102, 101],
        "rsi": [40, 45, 50],
        "ema20": [99, 100, 101],
        "ema50": [98, 99, 100],
    })

    env = LongTermInvestEnv(df)
    obs, info = env.reset()
    obs, reward, terminated, truncated, _ = env.step([0.5])

    
    assert len(obs) == 4
    assert isinstance(reward, float)
