from collections import defaultdict
def kosaraju(V,g):
    def end_time(graph, u, stack, visited):
        visited.add(u)
        # print(graph[15])
        for v in g[u]:
            if v not in visited:
                end_time(graph, v, stack, visited)
        stack.append(u)

    def dfs_util(graph, u, visited):
        visited.add(u)
        print(graph)
        for v in g[u]:
            print(u, g[u])
            if v not in visited:
                dfs_util(graph, v, visited)
    
    
    def reverse_graph():
        g_prime = defaultdict(list)
        for u, v_s in g.items():
            for v in v_s:
                g_prime[v].append(u)
        return g_prime
    
    visited = set()
    stack = []
    l = list(g.keys()).copy()
    for item in l:
        # print(len(g))
        if item not in visited:
            end_time(g, item, stack, visited)
                
    g_prime = reverse_graph()
    visited = set()
    result = 0
    print(stack, g_prime)
    while stack:
        item = stack.pop()
        print(item, visited)
        if item not in visited:
            dfs_util(g_prime, item, visited)
            result += 1
    print ("here", result)
    return result
    
d = defaultdict(list)
d[0] = [-1]
d[1] = [0]
d[2] = [3]
d[-1] = [1,2]
kosaraju(5, d)