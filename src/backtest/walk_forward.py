class WalkForwardValidator:
    def __init__(self, env, agent, windows):
        self.env = env
        self.agent = agent
        self.windows = windows

    def run(self):
        results = []
        for train_end, test_end in self.windows:
            self.agent.train(self.env, train_end)
            result = self.agent.evaluate(self.env, test_end)
            results.append(result)
        return results
