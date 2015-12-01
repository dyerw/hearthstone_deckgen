# NOTE: this is mostly in pseudo-code (for now)
def maxcost-n-kruskals(n, graph):

    edges = graph.edges()
    edgeWeights = graph.edges()
    edges.sort()    # sort the edges by weight
    numCards,cost = 0
    resultNodeSet = []
    resultEdgeSet = []

    while numNodes < n and not graph empty:
        edge = maxWeight(edges) # find the edge with the max weight
                                # will also remove it from the list
        weight = edge['weight'] # store its weight
        nodes = [edge[1],edge[2]] # store the nodes it is attached to
        graph.remove(edge)      # remove that edge from the graph
        resultEdgeSet.append(edge)  # add the edge to the result edge set
        cost += weight              # add the weight of this edge onto the cost
        for node in (range(0, len(nodes))):     # iterate over the nodes
            if not node in resultNodeSet:       # if we haven't already picked this node
                resultNodeSet.append(node)      # add it to the end of the result node list
                numCards += node['count']       # update the number of nodes with the number of cards in the node
    return [cost, constructGraph(resultEdgeSet,resultNodeSet)]  # return a tuple of the final weight and the new graph

# pop off the first itme of the list and return it
def maxWeight(edges):
    edge = edges.pop(0)
    return edge

def constructGraph(edges, nodes):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def generateGraph(..., ...):
    # something here for creating it from the scraped data

def __main__():
    OG = generateGraph(OG)  # create the graph from scraped data
    inverseKruskals = maxcost-n-kruskals(30, OG)    # run the modified kruskal's with a card number of 30
    print inverseKruskals[0]    # print out the total cost
    nx.draw(inverseKruskals[1]) # finally, the draw graph
