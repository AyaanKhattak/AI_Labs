graph={
    's':['a','b'],
    'a':['c','d'],
    'b':['e','f','j'],
    'c':['k','g'],
    'd':['g','l'],
    'e':['m'],
    'f':[],
    'g':[],
    'k':[],
    'j':['m'],
    'l':['m']

}

h_values={
    's':12,'a':11,'b':9,'c':10,'d':9,'e':6,'f':5,'j':4,'k':6,'g':0,'l':3,'m':0
}

def hcs(graph,h_values,start,goals):
    curr=start
    path=[curr]

    while curr not in goals:
        neighbors = graph.get(curr,[])
        if not neighbors:
            return None
        
        nex_node=min(neighbors,key=lambda n:h_values[n])
        if h_values[nex_node]>=h_values[curr]:
            return None
        curr =nex_node
        path.append(curr)

    return path

start_node='s'
goal_nodes=['g','m']
result_path = hcs(graph, h_values, start_node, goal_nodes)
print("Hill Climbing Path:", result_path)