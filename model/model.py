from transformers import pipeline


model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

class GetSentimentModel:
    def __init__(self): 
        self.model = pipeline("sentiment-analysis", model_name)

    def predict_sentiment(self, text):
        sentiment = self.model(text)
        return sentiment[0]["label"]
