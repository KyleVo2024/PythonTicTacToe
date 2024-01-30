done = True
xMove = True
oMove= False
size = 3
board = []
rowMove = 0
colMove = 0
score =0
for _ in range(size):
    temp = [0 for _ in range(3)];
    board.append(temp)
def legalMove(rowMove, colMove):
    if rowMove>0 and rowMove<4 and colMove>0 and colMove<4 and board[rowMove-1][colMove-1] == 0:
        return True
    else:
        return False
def printBoard():
    for row in board:
        print(row)
def isWinner():
    #check col
    for col in range(size):
        score = 0
        temp = board [0][col]
        for row in range(size):
            if board[row][col] == temp and temp!=0:
                score +=1
            else:
                break
        if score==3:
            return True
        
    #check row
    for row in range(size):
        score = 0
        temp = board [row][0]
        for col in range(size):
            if board[row][col] == temp and temp!=0:
                score +=1
            else:
                break
        if score==3:
            return True
    #check diagnoal LR
    temp = board [0][0]
    score = 0
    if board[1][1] == temp and board[2][2]==temp and temp!=0:
        return True

    #check diagnoal RL
    temp = board [0][2]
    score = 0
    if board[1][1] == temp and board[2][0] ==temp and temp!=0:
        return True
    return False    
    
                   
while done:
    printBoard()
    while xMove:
        try:
            rowMove = int(input("X Move put row:"))
            colMove = int(input("X Move put col:"))
            if legalMove(rowMove, colMove):
                board[rowMove-1][colMove-1] = "X"
                xMove = False
                oMove = True
                if isWinner():
                    print("X is the Winner")
                    xMove = False
                    oMove = False
                    done = False
                
            
            else:
                print("Illegal Move!!!")
        except:
            print("Illegal Move!!!")
    printBoard()
    while oMove:
        try:
            rowMove = int(input("O Move put row:"))
            colMove = int(input("O Move put col:"))
            if legalMove(rowMove, colMove):
                board[rowMove-1][colMove-1] = "O"
                xMove = True
                oMove = False
                if isWinner():
                    print("O is the Winner")
                    xMove = False
                    oMove = False
                    done = False
            else:
                print("Illegal Move!!!")
        except:
            print("Illegal Move!!!")
        
    
    

    

    

    