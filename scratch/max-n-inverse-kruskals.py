# NOTE: this is mostly in pseudo-code (for now)

def sort_edges(edges):
    return

def maxcost_kruskals(graph):

    edges = graph.edges()
    sort_edges(edges)    # sort the edges by weight
    num_cards, cost = 0
    result_node_set = []
    result_edge_set = []

    while num_cards <= DECKSIZE and graph.number_of_edges() > 0:
        edge = edges.pop(0)     # find the edge with the max weight
                                # will also remove it from the list
        weight = edge['weight']   # store its weight
        nodes = [edge[1], edge[2]] # store the nodes it is attached to
        graph.remove(edge)      # remove that edge from the graph
        result_edge_set.append(edge)  # add the edge to the result edge set
        cost += weight              # add the weight of this edge onto the cost
        for node in (range(0, len(nodes))):     # iterate over the nodes
            if not node in result_node_set:       # if we haven't already picked this node
                result_node_set.append(node)      # add it to the end of the result node list
                num_cards += node['count']       # update the number of nodes with the number of cards in the node
    return [cost, construct_graph(result_edge_set, result_node_set)]  # return a tuple of the final weight and the new graph

def construct_graph(edges, nodes):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def generateGraph(..., ...):
    # something here for creating it from the scraped data

def __main__():
    OG = generateGraph(OG)  # create the graph from scraped data
    inverse_kruskals = maxcost_kruskals(30, OG)    # run the modified kruskal's with a card number of 30
    print inverse_kruskals[0]    # print out the total cost
    nx.draw(inverse_kruskals[1]) # finally, the draw graph
