import os

HERE = os.path.dirname(os.path.abspath(__file__))

PAGES_TO_SCRAPE = 10
HEARTHPWN_URL = 'http://hearthpwn.com/decks?filter-deck-tag=3&page='
SAVE_LOCATION = os.path.join(HERE, '..', 'data', 'decks.csv')
DECKSIZE = 30
