class Board:
    def __init__(self):
        self.CurrentBoard = [0,0,0,0,0,0,0,0,0]
        self.username1 = ''
        self.username2 = ''
        self.lastuser = ''
        self.totalgamesplayed = 0
        self.totalwins = 0
        self.totalties = 0
        self.totallosses = 0
        
    def recordGamePlayed(self):
        self.totalgamesplayed += 1

    def resetGameBoard(self):
        self.CurrentBoard = [0,0,0,0,0,0,0,0,0]

    def returnBoard(self):
        return self.CurrentBoard

    def playMoveOnBoard(self,board):
        self.CurrentBoard = board

    def isBoardFull(self):
        board = self.CurrentBoard
        if 0 in board:
            return 0
        else:
            return 1

    def isGameFinished(self):
        Board = self.CurrentBoard
        if ((Board[0]==Board[1]==Board[2] != 0) or (Board[3]==Board[4]==Board[5] != 0) or (Board[6]==Board[7]==Board[8] != 0) or
            (Board[0]==Board[3]==Board[6] != 0) or (Board[1]==Board[4]==Board[7] != 0) or (Board[2]==Board[5]==Board[8] != 0) or
            (Board[0]==Board[4]==Board[8] != 0) or (Board[2]==Board[4]==Board[6] != 0)):
            if self.username1 == self.lastuser:
                self.totalwins += 1
            else:
                self.totallosses +=1
            return 1
        
        else:
            if self.isBoardFull() == 1:
                self.totalties +=1
                return 2
            return 0 
                
    def computeStats(self):
      return self.username1,self.username2,self.lastuser,self.totalgamesplayed,self.totalwins,self.totallosses,self.totalties



        
        
