import numpy as np

class Encoder:
    """
    Encodes a piece of text using the given encoder
    """
    def __init__(self, encoder):
        self.encoder = encoder

    def compute_quote_embeddings(self, quotes):
        message_embeddings = self.encoder(np.fromiter(quotes.keys(), dtype=str))
        return message_embeddings

    def compute_input_embedding(self, input_words):
        message_embeddings = self.encoder(input_words)
        return message_embeddings