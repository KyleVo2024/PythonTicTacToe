done = True
size = 3
board = []
for _ in range(size):
    temp = [0 for _ in range(3)];
    board.append(temp)
while done:
    rowMove = int(input("X Move put row:"))
    if rowMove>0 and rowMove<4:
        colMove = int(input("X Move put col:"))
        if colMove>0 and colMove<4:
            board[rowMove-1][colMove-1] = "X"
    print(board)
    

    