edges = [[1, 4], [4, 5], [2, 3]]
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
newEdges = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
n = 6
n = 5
newEdges.sort(key=lambda x: x[2])
def calculate_min_cost():
    s = [-1] * (n+1)
    
    def find(node):
        while s[node] >= 0:
            node = s[node]
        return node
    
    def union(node1, node2):
        parent1 = find(node1)
        parent2 = find(node2)
        if parent1 == parent2: return False
        rank1 = abs(s[parent1])
        rank2 = abs(s[parent2])

        if rank1 > rank2:
            s[parent2] = parent1
            s[parent1] = -(rank1+ rank2)
        else:
            s[parent1] = parent2
            s[parent2] = -(rank1+ rank2)
        return True        
    # For Min Cost to Repair Edges
    # broken = set()
    # for item in newEdges:
    #     broken.add((item[0], item[1]))
    # for u,v in edges:
    #     if (u,v) not in broken:
    #         union(u, v)    
    for u,v in edges:
        union(u, v)
             

    disconnected = 0
    for parent in s[1:]:
        if parent < 0: disconnected += 1
    cost = 0
    print(s)
    for edge in newEdges:
        if union(edge[0], edge[1]):
            disconnected -= 1
            cost += edge[2]
            if disconnected == 1: return cost
    
    return -1

print(calculate_min_cost())

