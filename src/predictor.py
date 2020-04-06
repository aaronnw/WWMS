import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


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
        best_quote = None
        best_similarity = 0
        input_embedding = input_embedding.reshape(1,-1)
        for quote, details in self.quotes.items():
            quote_embedding = details['embedding']
            quote_embedding = quote_embedding.reshape(1,-1)
            similarity = cosine_similarity(quote_embedding, input_embedding)[0]
            if similarity > best_similarity:
                best_similarity = similarity
                best_quote = (quote, details)
        return best_quote

    def predict_output(self, input_sentence):
        input_embedding = self.encoder.compute_embedding([input_sentence])
        return self.find_best_embedding(input_embedding)