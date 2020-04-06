import requests
from bs4 import BeautifulSoup
import re
from src.utils import save_pickle
from src.utils import quotes_file


# Build a nested dictionary of episode -> season -> link
def build_episode_dict():
    base_url = "https://www.officequotes.net/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html5lib')

    episode_table = soup.find('div', attrs = {'id':'content'})
    episode_dict = {}

    for item in episode_table.find_all_next('a', attrs={'href': re.compile("/no+")}):
        link = item.get('href')

        season_episode = link.split('.')[0]
        season = season_episode.split('-')[0][3:]
        episode = season_episode.split('-')[1]
        episode = episode[1:] if episode[0] == '0' else episode
        full_link = base_url + link

        if season not in episode_dict.keys():
            episode_dict[season] = {}
        episode_dict[season][episode] = full_link
    return episode_dict


# Do whatever processing we need to clean up a quote
def process_quote(quote):
    # Remove strings in brackets (actions in the source)
    quote = re.sub(r'\[[^]]*\]', '', quote)
    # Remove any "\t" or "\n" characters and any extra whitespace on either side
    quote = quote.strip()
    return quote

# Build a quote dictionary of quote -> (season, episode)
def build_quote_dict(episode_dict):
    quote_dict = {}
    for season, episodes in episode_dict.items():
        for episode, link in episodes.items():
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html5lib')
            quote_section = soup.find('div', attrs = {'class':'quote'})
            if quote_section:
                annotations = quote_section.find_all_next('b', text="Michael:")
                for annotation in annotations:
                    quote = process_quote(annotation.next_sibling)
                    quote_dict[quote] = {"season": int(season), "episode": int(episode)}
    return quote_dict


def scrape():
    episode_dict = build_episode_dict()
    quote_dict = build_quote_dict(episode_dict)
    save_pickle(quote_dict, quotes_file)
    return quote_dict

if __name__ == '__main__':
    scrape()