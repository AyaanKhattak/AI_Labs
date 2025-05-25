from collections import deque
graph={
    '0':['1','2','3'],
    '1':['4','5'],
    '2':['6'],
    '3':['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

def bfs(graph,start):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)

    while queue:
        m=queue.pop(0)
        print(m,end="->")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS: ")
bfs(graph,'0')