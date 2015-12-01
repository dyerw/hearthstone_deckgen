import networkx as nx

from constants import SAVE_LOCATION

# If necessary, can be used to load saved data from CSV
def load_csv_data():
    with open(SAVE_LOCATION, "r") as f:
        data = f.read()
    return data

def create_graph(data):
    cardlist = []
    lines = data.split("\n")
    for line in lines:
        if line:
            cardlist += [line.split(",")]

    # Create a node for each deck choice (one or two copies for each card)
    cardnames = set([x[1] for x in cardlist])
    cardnames = [[x, x + "_two"] for x in cardnames]
    cardnames = reduce(lambda x, y: x + y, cardnames)

    G = nx.Graph()
    G.add_nodes_from(cardnames)

    # Get a list of lists for each deck
    decks = [[]]
    curr = 0
    for card in cardlist:
        cardname = card[1] if card[2] == '1' else card[1] + '_two'
        if int(card[0]) == curr:
            decks[curr] += [cardname]
        else:
            curr += 1
            decks += [[cardname]]

    for deck in decks:
        for i, card in enumerate(deck):
            for other_card in deck[(i + 1):]:
                G.add_edge(card, other_card)
                print G[card][other_card]
                if 'weight' in G[card][other_card]:
                    prev_weight = G[card][other_card]['weight']
                    G[card][other_card]['weight'] = prev_weight + 1
                else:
                    G[card][other_card]['weight'] = 1


    for edge in G.edges_iter(data='weight', default=0):
        print edge
