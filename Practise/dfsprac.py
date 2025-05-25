graph={
    '0':['1','2','3'],
    '1':[],
    '2':['4'],
    '3':[],
    '4':[]
}

def dfs(graph,node,visited=None):
    if visited is None:
        visited=set()
    
    print(node,end="->")
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    
print("DFS: ")
dfs(graph,'0')