tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F': []
}

visited = list()


def dfs(graph, start, goal, maxDepth, depth):
    visited[depth].append(start)
    print('check :', start)
    if start == goal:
        print('goal found and path is', visited[-1])
        return True
    if maxDepth <= 0:
        return False
    for child in graph[start]:
        if dfs(graph, child, goal, maxDepth - 1, depth):
            return True
    return False


def ids(graph, start, goal, maxDepth):
    for depth in range(maxDepth):
        visited.append([])
        print('----- depth =', depth, '-----')
        if dfs(graph, start, goal, depth, depth):
            return True
    return print('goal NOT found')


ids(tree, 'A', 'F', 4)
print('visited', visited)
