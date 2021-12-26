graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C', 'H'],
    'H': ['F', 'G']
}


def dfs(graph, start, goal):
    stack = [start]
    visited = [[start]]
    while stack:
        node = stack.pop()
        path = visited.pop()
        if node == goal:
            print(path)
        for child in graph[node]:
            if child not in path:
                stack.append(child)
                visited.append(path + [child])


dfs(graph, 'A', 'F')