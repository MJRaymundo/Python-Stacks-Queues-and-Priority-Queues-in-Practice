# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Tests for graph.py
# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python

#Object Representation of the Cities and Roads
#import networkx as nx
#graph = nx.nx_agraph.read_dot("roadmap.dot")
#print(graph.nodes["london"])

#Testing load_graph
#from graph import City, load_graph

#nodes, graph = load_graph("roadmap.dot", City.from_dict)

#nodes["london"]

#print(graph)


#Looking for neighbors
#for neighbor in graph.neighbors(nodes["london"]):
#    print(neighbor.name)

#Neighbors with weights
#for neighbor, weights in graph[nodes["london"]].items():
#     print(weights["distance"], neighbor.name)

#Sorting neighbors
#def sort_by(neighbors, strategy):
#    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

#def by_distance(weights):
#    return float(weights["distance"])

#for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
#    print(f"{weights['distance']:>3} miles, {neighbor.name}")

#Breadth-First Search Using a FIFO Queue
#import networkx as nx
#from graph import City, load_graph

#def is_twentieth_century(year):
#    return year and 1901 <= year <= 2000
#
#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#for node in nx.bfs_tree(graph, nodes["edinburgh"]):
#    print("📍", node.name)
#    if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break
#else:
#    print("Not found")

#Visiting cities with higher latitude first
#def order(neighbors):
#    def by_latitude(city):
#        return city.latitude
#    return iter(sorted(neighbors, key=by_latitude, reverse=True))

#for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
#    print("📍", node.name)
#    if is_twentieth_century(node.year):
#        print("Found:", node.name, node.year)
#        break
#else:
#    print("Not found")