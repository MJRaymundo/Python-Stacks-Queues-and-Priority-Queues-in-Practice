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

#Testing breadth-first search and traversal implementations in action
#from graph import (
#    City,
#    load_graph,
#    breadth_first_traverse,
#    breadth_first_search as bfs,
#)

#def is_twentieth_century(city):
#    return city.year and 1901 <= city.year <= 2000

#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
#city.name
#'Lancaster'

#for city in breadth_first_traverse(graph, nodes["edinburgh"]):
#    print(city.name)

#Shortest Path Using Breadth-First Traversal
#import networkx as nx
#from graph import City, load_graph

#nodes, graph = load_graph("roadmap.dot", City.from_dict)

#city1 = nodes["aberdeen"]
#city2 = nodes["perth"]

#for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
#    print(f"{i}.", " → ".join(city.name for city in path))

#Testing Shortest Path
#from graph import shortest_path

#" → ".join(city.name for city in shortest_path(graph, city1, city2))

#def by_latitude(city):
#    return -city.latitude

#" → ".join(
#    city.name
#    for city in shortest_path(graph, city1, city2, by_latitude)
#)

#Checking the code for seeing if two roads remain connected
#from graph import connected
#connected(graph, nodes["belfast"], nodes["glasgow"])

#connected(graph, nodes["belfast"], nodes["derry"])

#Depth-First Search Using a LIFO Queue
#import networkx as nx
#from graph import City, load_graph

#def is_twentieth_century(year):
#    return year and 1901 <= year <= 2000

#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#for node in nx.dfs_tree(graph, nodes["edinburgh"]):
#    print("📍", node.name)
#    if is_twentieth_century(node.year):
#        print("Found:", node.name, node.year)
#        break
#else:
#    print("Not found")