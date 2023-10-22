# # Define an empty graph as an adjacency list
# graph = {}

# # Add vertices (nodes) and edges
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'C', 'D']
# graph['C'] = ['A', 'B', 'D']
# graph['D'] = ['B', 'C']

# # To print the graph
# for vertex, neighbors in graph.items():
#     print(f"{vertex}: {neighbors}")

#Define an empty graph as an adjacency list
graph = {}

vertices = ['A','B','C','D']

#Adding vertices
for vertex in vertices:
    graph[vertex] = []

#Adding Edges
graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('A')
graph['B'].append('C')
graph['B'].append('D')
graph['C'].append('A')
graph['C'].append('B')
graph['C'].append('D')
graph['D'].append('B')
graph['D'].append('C')

# print("Graph Items")
# print(graph.items())

#To print the graph
for vertex, neighbours in graph.items():
    print(f"{vertex}:{neighbours}")