from collections import deque
# matrix = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
matrix = [['O', 'O', 'O', 'X'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O']]
 
m, n = len(matrix), len(matrix[0])
q = deque([(0,0,0)])
path, seen = [], {(0,0)}
while q:
    item = q.popleft()
    for di, dj in [(0,1), (1,0), (-1,0), (0, -1)]:
        i, j = item[0] + di, item[1] + dj
        if 0 <= i < m and 0 <= j < n and (i,j) not in seen:
            if matrix[i][j] == 'D': continue
            if matrix[i][j] == 'X':
                print(item[2]+1)
            q.append((i,j,item[2]+1)) 
            seen.add((i,j))
            