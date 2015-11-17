import urllib2

from bs4 import BeautifulSoup

PAGES_TO_SCRAPE = 10

# Get HTML for all deck listing pages
htmls = []
for x in range(PAGES_TO_SCRAPE):
    print "SCRAPING PAGE " + str(x + 1)
    response = urllib2.urlopen('http://hearthpwn.com/decks?filter-deck-tag=3&page=' + str(x + 1))
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

# Parse each decklist into python datastructures
def parse_cockatrice_export(decklist):
    lines = decklist.split('\n')

    deck = {}
    for line in lines:
        if line and line[0].isdigit():
            deck[line[2:-1]] = line[0]

    return deck

parsed_decks = map(parse_cockatrice_export, decklists)

with open('deckdata.csv', 'w') as f:
    for i, deck in enumerate(parsed_decks):
        for card, number in deck.iteritems():
            f.write(','.join([str(i), card, number]) + '\n')
