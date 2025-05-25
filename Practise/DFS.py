graph={
    '0':['1','2','3'],
    '1':['4','5'],
    '2':['6'],
    '3':['7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
    
}

def dfs(graph,node,visited=None):
    if visited is None:
        visited=[]

    visited.append(node)
    print(node,end="->")

    for neighbour in graph.get(node,[]):
        if neighbour not in visited:
            dfs(graph,neighbour,visited)


print("DFS Traversal:")
dfs(graph, '0')