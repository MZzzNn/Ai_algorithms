graph = {
    1: [(7, 2), (9, 3), (14, 6)],
    2: [(7, 1), (10, 3), (15, 4)],
    3: [(9, 1), (10, 2), (11, 4), (2, 6)],
    4: [(15, 2), (11, 3), (6, 5)],
    5: [(6, 4), (9, 6)],
    6: [(14, 1), (2, 3), (9, 5)]
}


def ucs(graph, start, goal):
    queue = []
    paths = []
    visited = []
    queue.append((0, start))
    paths.append((0, [start]))

    while queue:
        queue.sort()
        paths.sort()

        cost, node = queue.pop(0)
        item = paths.pop(0)
        path = item[1]

        if node == goal:
            print(cost)
            print(path)
            break
        for child in graph[node]:
            if child[1] not in visited:
                totalcost = cost + child[0]
                queue.append((totalcost, child[1]))
            if child[1] not in path:
                paths.append((totalcost, path + [child[1]]))


ucs(graph, 1, 5)