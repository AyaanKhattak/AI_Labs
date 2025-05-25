import heapq
graph = {
    'IN': [('A', 1)],
    'A': [('D', 1)],
    'D': [('I', 1)],
    'I': [('K', 1)],
    'K': [('M', 1)],
    'M': [('OUT', 1)]
}

def ucs(graph,start,goal):
    visited=set()
    queue=[(0,[start])]


    while queue:
        cost,path=heapq.heappop(queue)
        node=path[-1]


        if node==goal:
            return path,cost
        
        if node not in visited:
            visited.add(node)
            for neighbour,edge_cost in graph.get(node,[]):
                if neighbour not in visited:
                    heapq.heappush(queue,(cost+edge_cost,path+[neighbour]))
    return None,float('inf')

path, total_cost = ucs(graph, 'IN', 'OUT')
print("Correct UCS Path:", ' -> '.join(path))
print("Total Cost:", total_cost)                 