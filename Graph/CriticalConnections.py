from collections import defaultdict
def critical_connections(n, edges):
    g = defaultdict(list)
    time = 1
    for u,v in edges:
        g[u] += v,
        g[v] += u,

    def dfs(u, parent, low, disc, visited):
        # print(g)
        nonlocal time
        visited.add(u)
        disc[u] = time
        low[u] = time
        time += 1
        # print("time",u, time)
        for v in g[u]:
            if v not in visited:
                parent[v] = u
                dfs(v, parent, low, disc, visited)

                low[u] = min(low[u], low[v])

                # print(u,v, low, disc)
                if low[v] > disc[u]:
                    print(u,v)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    visited = set()
    parent = [-1]*(n+1)
    low = [float("inf")] * (n+1)
    disc = [float("inf")] * (n+1)

    for i in range(1,n+1):
        if i not in visited:
            dfs(i, parent, low, disc, visited)

# critical_connections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]])
critical_connections(6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]])
critical_connections(9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]])

