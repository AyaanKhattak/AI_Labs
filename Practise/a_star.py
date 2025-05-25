import heapq

# Initial and goal states
start = ((2, 1, 3),
         (4, 7, 6),
         (5, 8, 0))  # 0 represents the blank

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Possible move directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan Distance Heuristic
def manhattan(state, goal):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:  # Don't compute for blank
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            dist += abs(i - x) + abs(j - y)
    return dist

# Get blank tile (0) position
def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate valid successors by moving the blank tile
def successors(state):
    i, j = get_blank(state)
    result = []
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            # Create a deep copy
            new_state = [list(row) for row in state]
            # Swap blank with adjacent tile
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            result.append(tuple(tuple(row) for row in new_state))
    return result

# A* Search
def a_star(start, goal):
    visited = set()
    queue = [(manhattan(start, goal), 0, start, [])]  # (f, g, state, path)

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for succ in successors(state):
            if succ not in visited:
                new_g = g + 1
                h = manhattan(succ, goal)
                heapq.heappush(queue, (new_g + h, new_g, succ, path + [state]))

    return None

solution = a_star(start, goal)

for step, state in enumerate(solution):
    print(f"Step {step}:")
    for row in state:
        print(row)
    print()
