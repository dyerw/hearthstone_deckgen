import networkx

from algorithm import create_graph, load_csv_data

g = create_graph(load_csv_data())
networkx.write_graphml(g, 'hearthstone.graphml')
