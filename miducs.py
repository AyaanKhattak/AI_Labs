import heapq

graph = {
    'S': [('A', 22), ('B', 23), ('C', 26)],
    'A': [('E', 16), ('D', 15)],
    'B': [('D', 21)],
    'C': [('F', 19)],
    'D': [('E', 12), ('R', 12)],
    'E': [('P', 24), ('R', 10)],
    'F': [('M', 12)],
    'P': [('R', 14)],
    'R': [('G', 17)],
    'M': [('T', 18)],
    'T': [('G', 11)],
    'G': []
}

goal_nodes=['L','G','H','M']

def ucs(graph,start,goals):
    queue=[]
    heapq.heappush(queue,(0,start,[start]))
    visited=set()

    while queue:
        cost,node,path=heapq.heappop(queue)
        if node in goals:
            return path,cost
        if node not in visited:
            visited.add(node)
            for neighbor,edge_cost in graph.get(node,[]):
                if neighbor not in visited:
                    heapq.heappush(queue,(cost+edge_cost,neighbor,path+[neighbor]))
    return None,None

start_node = 'S'
path, total_cost = ucs(graph, start_node, goal_nodes)
print("UCS Path:", path)
print("Total Cost:", total_cost)