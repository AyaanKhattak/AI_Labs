import heapq

graph = {
    '0': [('1', 2), ('2', 4)],
    '1': [('3', 7), ('4', 1)],
    '2': [('4', 3)],
    '3': [],
    '4': [('5', 1)],
    '5': []
}

def ucs(graph,start,goal):
    visited=set()

    queue=[(0,start,[start])]

    while queue:
        cost,node,path=heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node==goal:
            print("Path:","->".join(path))
            print("Total Cost: ",cost)
            return
        
        for neighbor,weight in graph.get(node,[]):
            if neighbor not in visited:
                heapq.heappush(queue,(cost+weight,neighbor,path+[neighbor]))

    print("No path found")

ucs(graph,'0','5')