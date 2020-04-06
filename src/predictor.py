import numpy as np

class Predictor:
    def __init__(self, encoder, quotes):
        self.encoder = encoder
        self.quotes = self.generate_quote_embeddings(quotes)

    def generate_quote_embeddings(self, quotes):
        # Add an embedding field to each item in quote dict
        raw_quotes = np.asarray(list(quotes.keys()))
        embeddings = self.encoder.compute_embedding(raw_quotes)
        for index, key in enumerate(quotes.keys()):
            quotes[key]['embedding'] = embeddings[index]
        return quotes

    def find_best_embedding(self, input_embedding):
        pass

    def predict_output(self, input_sentence):
        input_embedding = self.encoder.compute_embedding([input_sentence])
        return self.find_best_embedding(input_embedding)