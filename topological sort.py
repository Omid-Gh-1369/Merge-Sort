

#   4 --- 10
#   |   /    \
#   |  /      \
#    2         5
#     \       /
#      \     /
#         1

#----------------------

def topological_sort(start, visited, sort):
    current = start
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    sort.append(current)
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    return sort

#------------------------

edges = { 10: [4, 5, 2], 4: [2], 2: [1], 5: [1], 1 :[]}
vertices = [1,5,4,10,2]
sort = topological_sort(10, [], [])
print(sort)
