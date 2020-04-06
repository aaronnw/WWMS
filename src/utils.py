import os
import pickle

resources_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources")

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"

quotes_filename = "michael_quotes.pickle"
embeddings_filename = "quote_embeddings.pickle"

quotes_file = os.path.join(resources_dir, quotes_filename)
embeddings_file = os.path.join(resources_dir, embeddings_filename)
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

# Load quotes embeddings if file exists, otherwise run the web scraper
def load_quote_embeddings():
    if os.path.exists(embeddings_file) and os.path.isfile(embeddings_file):
        with open(embeddings_file, 'rb') as f:
            embeddings = pickle.load(f)
            return embeddings
