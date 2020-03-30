from src.utils import load_quotes, load_encoder
from src.predictor import Predictor
from src.encoder import Encoder
from src.scraper import scrape



def query_input():
    return input("Enter a sentence or phrase to translate:")

def main():
    # Load a dictionary of Michael's quotes to their season and episode
    quotes = load_quotes()
    if quotes is None:
        quotes = scrape()
    sentence_encoder = load_encoder()

    input_sentence = query_input()

    encoder = Encoder(sentence_encoder)
    predictor = Predictor(encoder, quotes)

    output_sentence = predictor.predict_output(input_sentence)
    print(output_sentence)


if __name__ == '__main__':
    main()