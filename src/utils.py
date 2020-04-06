import os
import sys
import pickle
import tensorflow_hub as hub

resources_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources")

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"

quotes_filename = "michael_quotes.pickle"

quotes_file = os.path.join(resources_dir, quotes_filename)
encoder_folder = os.path.join(resources_dir, "encoder")


def save_pickle(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

# Load quotes if file exists, otherwise run the web scraper
def load_quotes():
    if os.path.exists(quotes_file) and os.path.isfile(quotes_file):
        with open(quotes_file, 'rb') as f:
            quotes = pickle.load(f)
            return quotes

# Load sentence encoder if file exists, otherwise pull from tf hub
def load_encoder():
    if os.path.exists(encoder_folder):
        print("Loading encoder from {0}".format(encoder_folder))
        model = hub.load(encoder_folder)
        return model
    else:
        sys.exit("No model could be loaded -- download from {0} and extract to {1}".format(module_url, encoder_folder))