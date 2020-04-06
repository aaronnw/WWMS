from src.utils import load_quotes, load_quote_embeddings, save_pickle, embeddings_file
from src.predictor import Predictor
from src.encoder import Encoder
from src.scraper import scrape

import numpy as np


def query_input():
    return input("Enter a sentence or phrase to translate:")

def filter_quotes(quotes, season=None, episode=None):
    filtered_quotes = {}
    for quote, details in quotes.items():
        if episode and details['episode'] != episode:
            continue
        if season and details['season'] != season:
            continue
        filtered_quotes[quote] = details
    return filtered_quotes

def generate_quote_embeddings(encoder, quotes):
    # Add an embedding field to each item in quote dict
    raw_quotes = np.asarray(list(quotes.keys()))
    embeddings = encoder.compute_embedding(raw_quotes)
    for index, key in enumerate(quotes.keys()):
        quotes[key]['embedding'] = embeddings[index]
    return quotes

def main():
    # Load a dictionary of Michael's quotes to their season and episode
    print("Attempting to load quotes from file")
    quotes = load_quotes()
    if quotes is None:
        print("Scraping the web for new quotes")
        quotes = scrape()

    print("Creating sentence encoder")
    encoder = Encoder()

    print("Attempting to load quote embeddings from file")
    quote_embeddings = load_quote_embeddings()
    if quote_embeddings is None:
        print("Generating new quote embeddings")
        quote_embeddings = generate_quote_embeddings(encoder, quotes)
        print("Saving new quote embeddings to {0}".format(embeddings_file))
        save_pickle(quote_embeddings, embeddings_file)

    print("Creating predictor")
    predictor = Predictor(encoder, quote_embeddings)

    while True:
        input_sentence = query_input()
        prediction = predictor.predict_output(input_sentence)
        output_quote = prediction[0]
        output_season = prediction[1]['season']
        output_episode = prediction[1]['episode']
        print("Michael says: \"{0}\" in season {1}, episode {2}".format(output_quote, output_season, output_episode))


if __name__ == '__main__':
    main()