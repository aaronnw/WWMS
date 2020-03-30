import os
import sys
import pickle
import tensorflow_hub as hub
import tensorflow as tf

resources_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources")

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"

quotes_filename = "michael_quotes.pickle"
encoder_filename = "google_sentence_encoder"

quotes_file = os.path.join(resources_dir, quotes_filename)
encoder_folder = os.path.join(resources_dir, encoder_filename)


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
        model = tf.keras.models.load_model(encoder_folder)
        return model
    else:
        try:
            model = hub.load(module_url)
        except Exception as e:
            sys.exit("No model could be loaded from {0} \n Error: {1}".format(module_url, repr(e)))
        if model:
            #TODO: Figure out how to save this model for future loading
            model.save(encoder_folder)
    return model