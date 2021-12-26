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


def bfs(graph, start, goal):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print(visited)
        for child in graph[node]:
            if child not in visited:
                queue.append(child)


bfs(graph, 'A', 'F')