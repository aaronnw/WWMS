import os
import pickle

resources_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources")
quotes_filename = "quotes.pickle"
quotes_file = os.path.join(resources_dir, quotes_filename)

def save_quotes(quote_dict, filename):
    with open(filename, 'wb') as f:
        pickle.dump(quote_dict, f)