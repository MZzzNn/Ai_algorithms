tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F': []
}


def dls(graph, start, goal, maxDepth):
    visited.append(start)
    print('check :', start)
    if start == goal:
        return True
    if maxDepth <= 0:
        return False
    for child in graph[start]:
        if dls(graph, child, goal, maxDepth - 1):
            return True
    return False


start = 'A'
goal = 'F'
max_depth = 3
visited = list()

result = dls(tree, start, goal, max_depth - 1)
if result:
    print('goal found and path is', visited)
else:
    print('goal NOT found')
