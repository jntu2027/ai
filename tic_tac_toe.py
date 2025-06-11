import math
def prints(board):
    for i in board:
        for j in i:
            print(j, end="\t")
        print()
        
def win_or_lose(a):
    if (a == "X"):
        print("Player X has Won")
    else:
        print("Player O has Won")
    exit()

def check(board):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            return win_or_lose(board[i][0])
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]):
            return win_or_lose(board[0][i])
    if (board[0][0] == board[1][1] == board[2][2]):
        return win_or_lose(board[1][1])
    if (board[0][2] == board[1][1] == board[2][0]):
        return win_or_lose(board[1][1])
    

def player(cur,board):
    print(f"Player {cur} Enter Your number:",end="\t")
    num = int(input())
    row = math.ceil(num/3) - 1
    col = num%3 - 1
    while(board[row][col] == "X" or board[row][col] == "O" ):
        num = int(input("Position already taken. enter another value : "))
        row = math.ceil(num/3) - 1
        col = num%3 - 1
    board[row][col] = cur
    return board    
    
def start():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    played = 0
    toggle = True
    prints(board)
    while(played < 9):
        if toggle:
            board = player("X",board)
            played += 1
            toggle = False
        else:
            toggle = True
            board = player("O",board)
            played += 1
        prints(board)
        check(board)
    print("Draw")

start()
