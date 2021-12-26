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

'''
def bfs(graph, start, goal):
    queue = list(start)
    visited = list()
    result = ['not reachable', list()]
    print('queue start with :', start)
    while len(queue) > 0:  # while len(queue) > 0 :  =  while queue :
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print('goal is found', node)
            result = ['reachable', visited]
            break
        print('goal is not found', node)
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
    return result


result = bfs(graph, 'A', 'D')
print(result[0], ' and the path is :', result[1])
'''

'''
def dfs(graph, start, goal):
    stack = list(start)
    visited = list()
    visited.append([start])
    result = ['not reachable', list()]
    print('stack start with :', start)
    while stack:
        print('stack', stack)
        print('visited', visited)
        node = stack.pop()
        path = visited.pop()
        print('visited after pop', visited)
        print('path', path)
        if node == goal:
            print('goal is found', path)
            result[0] = 'reachable'
            result[1].append(path)
        else:
            print('goal is not found', node)
            for child in graph[node]:
                if child not in path:
                    stack.append(child)
                    visited.append(path + [child])
        print('--------------------------')
    return result

result = dfs(graph, 'A', 'D')
print(result[0], 'and the path is :', result[1])
'''






