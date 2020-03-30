class Predictor:
    def __init__(self, encoder, quotes):
        self.encoder = encoder
        self.quote_embeddings = self.generate_quote_embeddings(quotes)

    def generate_quote_embeddings(self, quotes):
        return self.encoder.compute_quote_embeddings(quotes)

    def find_best_embedding(self, input_embedding):
        pass

    def predict_output(self, input_sentence):
        input_embedding = self.encoder.compute_input_embedding(input_sentence)
        return self.find_best_embedding(input_embedding)