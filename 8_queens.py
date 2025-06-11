class chess:
    def __init__(self):
        self.board = [[" - " for i in range(8)] for j in range(8)]
        self.solution(0)
        
    def PrintBoard(self):
        for i in self.board:
            for j in i:
                print(j,end="")
            print()
                
                
                
    def check(self,r,c):
        for i in range(8):
            if (self.board[i][c] == " Q "):
                return False
        
        tr,tc = r,c
        while( (8 > tr >= 0) and (8 > tc >= 0)):
            if (self.board[tr][tc] == " Q "):
                return False
            tr -= 1
            tc -= 1
        tr,tc = r,c
        while( (8 > tr >= 0) and (8 > tc >= 0)):
            if (self.board[tr][tc] == " Q "):
                return False
            tr += 1
            tc += 1
        tr,tc = r,c
        while( (8 > tr >= 0) and (8 > tc >= 0)):
            if (self.board[tr][tc] == " Q "):
                return False
            tr -= 1
            tc += 1
        tr,tc = r,c
        while( (8 > tr >= 0) and (8 > tc >= 0)):
            if (self.board[tr][tc] == " Q "):
                return False
            tr += 1
            tc -= 1
        return True
    
    def solution(self,r):
        if (r == 8):
            self.PrintBoard()
            exit()
        for i in range(8):
            if (self.check(r,i)):
                self.board[r][i] = " Q "
                self.solution(r+1)
                self.board[r][i] = " - "
            
chess()