tree = {}

vertices = ['A','B','C','D','F','E']

# tree['A'] = ['B','C']
# tree['B'] = ['D','F']
# tree['C'] = ['E']

tree['A'].append('B')
tree['A'].append('C')
tree['B'].append('D')
tree['B'].append('F')
tree['C'].append('E')

for vertex, edges in tree.items():
    print(f"{vertex}:{edges}")