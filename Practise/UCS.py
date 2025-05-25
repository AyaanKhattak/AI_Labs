import heapq
graph={
    'S':[('C',2),('A',3),('D',2)],
    'C':[('F',1)],
    'D':[('B',3),('G',8)],
    'F':[('E',0),('G',4)],
    'B':[('E',2)],
    'A':[],
    'E':[('G',2)]
}

def ucs(graph,start,goal):
    queue=[(0,[start])]
    visited=set()

    while queue:
        cost,path=heapq.heappop(queue)
        node=path[-1]

        if node==goal:
            return path,cost
        
        if node not in visited:
            visited.add(node)
            for neighbour,edge_cost in graph.get(node,[]):
                if neighbour not in visited:
                    new_path=path+[neighbour]
                    heapq.heappush(queue,(cost+edge_cost,new_path))
    
    return None,float('inf')

path, total_cost = ucs(graph, 'S', 'G')
print("Path from S to G using UCS:", path)
print("Total cost:", total_cost)