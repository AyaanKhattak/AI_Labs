graph={
    '0':['1','2','3'],
    '1':[],
    '2':['4'],
    '3':[],
    '4':[]
}

def bfs(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print(" -> ".join(visited))


print("BFS")
bfs(graph,'0')