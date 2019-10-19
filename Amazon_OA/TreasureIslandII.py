from collections import deque
matrix = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

def get_closest(matrix):
    m, n = len(matrix), len(matrix[0])
    q = deque([ (i,j,0) for i,row in enumerate(matrix) for j, ch in enumerate(row) if ch == 'S'])
    dist = [[float("inf") for _ in range(m)] for _ in range(n)]
    seen = set(q)
    while q:
        item = q.popleft()
        for di, dj in ([(0, 1), (1, 0), (-1, 0), (0, -1)]):
            i, j, d = item[0]+di, item[1]+dj, item[2]+1
            if 0 <= i < m and 0 <= j < n and (i, j) not in seen and matrix[i][j] != 'D':
                if matrix[i][j] == 'X':
                    return d
                seen.add((i, j))
                q.append((i, j, d))

print(get_closest(matrix))
    
