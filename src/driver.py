import os
import pickle

from src.scraper import scrape
from src.utils import quotes_file

# Load quotes if file exists, otherwise run the web scraper
def load_quotes():
    if os.path.exists(quotes_file) and os.path.isfile(quotes_file):
        with open(quotes_file, 'rb') as f:
            quotes = pickle.load(f)
            return quotes
    else:
        quotes = scrape()
        return quotes


def main():
    # Load a dictionary of Michael's quotes to their season and episode
    quotes = load_quotes()
    print(quotes)


if __name__ == '__main__':
    main()