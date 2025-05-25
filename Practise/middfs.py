graph = {
    'h': ['a'],
    'a': ['b', 'd'],
    'b': ['c', 'f'],
    'c': ['h', 'e'],
    'd': ['f'],
    'e': ['f', 'b'],
    'f': ['a'],
    'g': ['h', 'e']
}

goal = ['e', 'f']

def dfs(graph, start, goals, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start in goals:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goals, visited, path)
            if result is not None:  # If path found, return it immediately
                return result

    path.pop()  # Backtrack
    return None

start_node = 'h'
result_path = dfs(graph, start_node, goal)
print("DFS:", result_path)
