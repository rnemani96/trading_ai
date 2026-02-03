class Backtester:
    def __init__(self, env, agent):
        self.env = env
        self.agent = agent

    def run(self):
        obs = self.env.reset()
        done = False

        while not done:
            action = self.agent.act(obs)
            obs, reward, done, info = self.env.step(action)

        return self.env.performance()
