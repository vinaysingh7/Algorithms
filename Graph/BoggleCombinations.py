board = [[0 for i in range (3)] for i in range(3)]
M = len(board)
total = M * M
curr = 1
order = set()


def generateRandomOrder(board, row, col, curr):
    if board[row][col] != 0:
        return
    board[row][col] = curr
    if curr == 9:
        order.add(' '.join(str(row-1) for item in board for row in item))
    curr +=1
    for i in range (row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < M and j >= 0 and j < M:
                generateRandomOrder(board, i, j, curr)
    
    board[row][col] = 0
    curr -= 1


for i in range(M):
    for j in range (M):
        generateRandomOrder(board, i, j, curr)

print(order)

print(len(order))

with open('/media/vinay/New_Ubuntu/MSCS-Assignments/CS5520_MAD/vinaysingh-5520/NUMAD19SUVinaySingh/app/src/main/assets/possible_arrangements.txt', 'w+') as writer:
    for item in order:
        writer.write(item + '\n')