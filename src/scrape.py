# This file contains the functionality necessary to gather information
# about Hearthstone decks necessary to run our algorithm
import urllib2

from bs4 import BeautifulSoup

from constants import PAGES_TO_SCRAPE, HEARTHPWN_URL, SAVE_LOCATION

def parse_cockatrice_export(decklist):
    """
    We are given a deck list in "Cockatrice" format
    and this function splits it into a list of dictionaries
    where the key is the name of the card and the vaue is
    the number of that card in the deck
    e.g.
    {'Card1': 2, 'Card2': 1, 'Card3': 2, ...}
    """
    lines = decklist.split('\n')

    deck = {}
    for line in lines:
        if line and line[0].isdigit():
            deck[line[2:-1]] = line[0]

    return deck


def save_data_to_csv(data, save_location):
    """
    Because scraping the website can take a while or because
    we are not online or want to run against static data for tests
    we can save the results of our scrape to CSV
    data :list: the list of decks to save
    save_location :string: the filepath to where the CSV will be saved
    """
    with open(save_location, 'w') as f:
        for i, deck in enumerate(parsed_decks):
            for card, number in deck.iteritems():
                f.write(','.join([str(i), card, number]) + '\n')


def get_scraped_content(save=True):
    """
    Scrapes the HTML content of Hearthpwn.com's decklists
    to gather data about decklists. Contains logic very specific
    to the layout of Hearthpwn.com
    save :bool: if true will save the content to disk as a CSV
    returns the decklist data
    """
    # Get HTML for all deck listing pages
    htmls = []
    for x in range(PAGES_TO_SCRAPE):
        print "SCRAPING PAGE " + str(x + 1)
        response = urllib2.urlopen(HEARTHPWN_URL + str(x + 1))
        html = response.read()
        htmls += [html]

    # Parse all pages for links to each deck
    links = []
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        deck_table = soup.find(attrs={'class' :'listing-decks'})
        rows = deck_table.tbody.find_all('tr')

        for row in rows:
            data = row.find_all('td')
            for link in data[0].find_all('a'):
                if '/decks/' in link['href']:
                    links += [link['href']]

    # Grab the decklists from each deck link
    decklists = []
    for link in links:
        endpoint = link.split('/')[2]
        deck_id = endpoint.split('-')[0]
        print deck_id
        response = urllib2.urlopen('http://hearthpwn.com/decks/' + deck_id + '/export/1')

        deck_list = response.read()
        decklists += [deck_list]

    parsed_decks = map(parse_cockatrice_export, decklists)
    if save:
        save_data_to_csv(parsed_decks, SAVE_LOCATION)

    return parsed_decks
