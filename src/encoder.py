import os
import sys
import tensorflow_hub as hub
from src.utils import encoder_folder, module_url

class Encoder:
    """
    Loads a sentence encoder model and encodes a piece of text
    """
    def __init__(self):
        self.encoder = self.load_encoder()

    # Load sentence encoder if file exists, otherwise pull from tf hub
    def load_encoder(self):
        if os.path.exists(encoder_folder):
            print("Loading encoder from {0}".format(encoder_folder))
            model = hub.load(encoder_folder)
            return model
        else:
            sys.exit(
                "No model could be loaded -- download from {0} and extract to {1}".format(module_url, encoder_folder))

    def compute_embedding(self, phrase):
        return self.encoder(phrase).numpy()

