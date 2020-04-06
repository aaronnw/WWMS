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

    while True:
        input_sentence = query_input()
        prediction = predictor.predict_output(input_sentence)
        output_quote = prediction[0]
        output_season = prediction[1]['season']
        output_episode = prediction[1]['episode']
        print("Michael says: \"{0}\" in season {1}, episode {2}".format(output_quote, output_season, output_episode))


if __name__ == '__main__':
    main()