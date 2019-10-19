from collections import defaultdict, deque
import heapq
# edges = [[1, 2, 1], [2, 3, 1], [3, 5, 1], [1, 4, 1], [4, 5, 2], [3, 4, 2], [2, 4, 4]]
edges = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 1, 3], [1, 3, 2], [5, 3, 1]]
ans = [False] * len(edges)
g = defaultdict(list)
g_node = 5
for edge in edges:
    g[edge[0]] += [edge[2], edge[1]],
    g[edge[1]] += [edge[2], edge[0]],

dist = [[float("inf"), []]] * (len(g)+1)
dist[1] = [0, set()]
heap = []
heapq.heappush(heap,(0,1))
seen = set()
while heap:
    d, u = heapq.heappop(heap)
    seen.add(u)
    for d_v, v in g[u]:
        if v not in seen:
            if v == 5: print(u, dist[v][0] , dist[u][0]+d_v)
            if dist[u][0]+d_v == dist[v][0]:
                dist[v][1].add(u)
            elif dist[v][0] > dist[u][0]+d_v:
                 dist[v] = [dist[u][0]+d_v, set([u])]
            heapq.heappush(heap, (dist[v][0], v))
print(dist)
q = deque()
for v in dist[g_node][1]:
    q.append((g_node, v))
used_edges = set()
seen = set()
while q:
    parent, node = q.popleft()
    used_edges.add((parent, node))
    used_edges.add((node, parent))
    seen.add(node)
    # if node == 1: continue
    for neighbor in dist[node][1]:
        q.append((node, neighbor))
print(used_edges)

for i,edge in enumerate(edges):
    if (edge[0], edge[1]) in used_edges:
        ans[i] = True
print(ans)


