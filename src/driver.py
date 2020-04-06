from src.utils import load_quotes, load_encoder
from src.predictor import Predictor
from src.encoder import Encoder
from src.scraper import scrape



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


def main():
    # Load a dictionary of Michael's quotes to their season and episode
    quotes = load_quotes()
    if quotes is None:
        quotes = scrape()

    quotes = filter_quotes(quotes, 1, 1)
    sentence_encoder = load_encoder()

    encoder = Encoder(sentence_encoder)
    predictor = Predictor(encoder, quotes)

    input_sentence = query_input()

    output_sentence = predictor.predict_output(input_sentence)
    print(output_sentence)


if __name__ == '__main__':
    main()