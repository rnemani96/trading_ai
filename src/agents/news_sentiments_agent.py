from transformers import pipeline

class NewsSentimentAgent:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def score(self, headlines):
        scores = [self.model(h)[0]["score"] for h in headlines]
        return sum(scores) / len(scores)
