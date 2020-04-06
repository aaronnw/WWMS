
class Encoder:
    """
    Encodes a piece of text using the given encoder
    """
    def __init__(self, encoder):
        self.encoder = encoder

    def compute_embedding(self, phrase):
        return self.encoder(phrase).numpy()
