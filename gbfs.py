graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F', 'J'],
    'C': ['K', 'G'],
    'D': ['L'],
    'E': ['M'],
    'F': [],
    'J': ['M'],
    'K': [],
    'L': [],
    'G': [],
    'M': []
}

# Heuristic values for each node (estimated cost to goal 'G')
h_values = {
    'S': 12, 'A': 11, 'B': 9, 'C': 10, 'D': 9, 'E': 6, 'F': 5, 'J': 4,
    'K': 6, 'G': 0, 'L': 3, 'M': 0
}

def greedy_best_first_search(graph, h_values, start, goal):
    open_list = [start]       # Nodes to explore
    closed_set = set()        # Explored nodes
    path = []                 # To record the traversal path

    while open_list:
        # Pick the node with the lowest heuristic value
        current = min(open_list, key=lambda n: h_values[n])
        open_list.remove(current)
        path.append(current)

        if current == goal:
            return path  # Goal found, return path

        closed_set.add(current)

        # Add neighbors to open_list if not explored
        for neighbor in graph.get(current, []):
            if neighbor not in closed_set and neighbor not in open_list:
                open_list.append(neighbor)

    return None  # Goal not found

start_node = 'S'
goal_node = 'G'

result_path = greedy_best_first_search(graph, h_values, start_node, goal_node)
print("Greedy Best First Search Path:", result_path)
