import socket
import board
from tkinter import *
import tkinter.messagebox


class Menu():
  
    def __init__(self,master):
        self.master = master
        self.master.title("Tic Tac Toe 2")
        self.master.geometry('400x400')
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master,bg = 'powder blue')
        self.frame.pack()
        #======login/username info===========================================
        self.Username = StringVar()
        self.Username.set(" ")
        self.port = IntVar()
        self.addy = StringVar()   
        #================================================================================================================
        self.lblTitle = Label(self.frame, text = 'Please Enter Address and Port and Hit Enter First, then Enter Username', font=('arial',8,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)


        self.UserFrame = LabelFrame(self.frame, width = 20,height=20,font=('arial',5,'bold'),relief = 'ridge',bg = 'gray',bd=10)
        self.UserFrame.grid(row=3, column = 0)
        self.UsernameEntry = Entry(self.UserFrame,font=('arial',15,'bold'),textvariable=self.Username)
        self.UsernameEntry.grid(row=1,column=1)
        self.AddyFrame = LabelFrame(self.frame, width = 20,height=20,font=('arial',10,'bold'),relief = 'ridge',bg = 'gray',bd=10)
        self.AddyFrame.grid(row=1, column = 0)
        self.AddyEntry = Entry(self.AddyFrame,font=('arial',15,'bold'),textvariable=self.addy)
        self.AddyEntry.grid(row=1,column=1)
        self.PortEntry = Entry(self.AddyFrame,font=('arial',10,'bold'),textvariable=self.port)
        self.PortEntry.grid(row=4,column=1)

        
        self.lblTitleUser = Label(self.UserFrame, text = 'Enter Username', font=('arial',10,'bold'), bg='powder blue', fg='black')
        self.lblTitleUser.grid(row = 0, column = 0, columnspan = 2, pady = 10)

        
        self.lblTitlePort = Label(self.AddyFrame, text = 'Enter Port', font=('arial',10,'bold'), bg='powder blue', fg='black')
        self.lblTitlePort.grid(row = 2, column = 0, columnspan = 2, pady = 10)
        self.lblTitleAddy = Label(self.AddyFrame, text = 'Enter Server Address', font=('arial',10,'bold'), bg='powder blue', fg='black')
        self.lblTitleAddy.grid(row = 0, column = 0, columnspan = 2, pady = 10)


        #================================================================================================================
        self.userbtn1 = Button(self.UserFrame, text = 'Enter', command = self.sendUser)
        self.userbtn1.grid(row = 1, column = 0)
        self.userbtn2 = Button(self.AddyFrame, text = 'Enter', command = self.connectUser)
        self.userbtn2.grid(row = 4, column = 0)

    def connectUser(self):
        port = self.port.get()
        addy = self.addy.get()
        connectionSocket.connect((addy,port))
    
    def sendUser(self):
        gameBoard.username1 = self.Username.get()
        data = (gameBoard.username1).encode()
        connectionSocket.send(data)
        tkinter.messagebox.showinfo(gameBoard.username1 + ' Waiting', "Please wait for Player 1 to send Username")
        data2 = connectionSocket.recv(1024).decode('ascii')
        gameBoard.username2 = data2

        self.master.destroy()
        self.master = Tk()
        self.game = ticTac(self.master)


class ticTac():
    def __init__(self,master):
        gameBoard.recordGamePlayed()
        self.master = master
        self.master.title("Tic Tac Toe " + gameBoard.username1)
        self.master.geometry('400x400')
        self.master.config(bg = 'powder blue')
        #===========Variable Init ======================
        self.var1 = StringVar()
        self.var1.set("-")
        self.var2 = StringVar()
        self.var2.set("-")
        self.var3= StringVar()
        self.var3.set("-")
        self.var4 = StringVar()
        self.var4.set("-")
        self.var5 = StringVar()
        self.var5.set("-")
        self.var6 = StringVar()
        self.var6.set("-")
        self.var7 = StringVar()
        self.var7.set("-")
        self.var8 = StringVar()
        self.var8.set("-")
        self.var9 = StringVar()
        self.var9.set("-")
        
        #==============Create Frame and Container=====
        self.frame = Frame(self.master,bg = 'powder blue')
        self.frame.pack()
        self.canvas = Canvas(self.frame,width = 600,height = 600)
        self.canvas.grid()
        #============Board init==============
        self.Frame1 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame1.grid(row=0, column = 0)
        self.Frame2 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame2.grid(row=0, column = 1)
        self.Frame3 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame3.grid(row=0, column = 2)
        self.Frame4 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame4.grid(row=1, column = 0)
        self.Frame5 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame5.grid(row=1, column = 1)
        self.Frame6 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame6.grid(row=1, column = 2)
        self.Frame7 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame7.grid(row=2, column = 0)
        self.Frame8 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame8.grid(row=2, column = 1)
        self.Frame9 = LabelFrame(self.canvas, width = 40,height=40,font=('arial',1,'bold'),relief = 'ridge',bg = 'black',bd=2)
        self.Frame9.grid(row=2, column = 2)
        
        self.btn1 = Button(self.Frame1,text = '-',height = 2, width = 2, command = self.choose1)
        self.btn2 = Button(self.Frame2,text = '-',height = 2, width = 2, command = self.choose2)
        self.btn3 = Button(self.Frame3,text = '-',height = 2, width = 2, command = self.choose3)
        self.btn4 = Button(self.Frame4,text = '-',height = 2, width = 2, command = self.choose4)
        self.btn5 = Button(self.Frame5,text = '-',height = 2, width = 2, command = self.choose5)
        self.btn6 = Button(self.Frame6,text = '-',height = 2, width = 2, command = self.choose6)
        self.btn7 = Button(self.Frame7,text = '-',height = 2, width = 2, command = self.choose7)
        self.btn8 = Button(self.Frame8,text = '-',height = 2, width = 2, command = self.choose8)
        self.btn9 = Button(self.Frame9,text = '-',height = 2, width = 2, command = self.choose9)

        self.btn1.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn2.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn3.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn4.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn5.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn6.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn7.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn8.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
        self.btn9.grid(row = 0, column = 0, sticky = "ewns", padx =1, pady =1)
       
     #=============Create Buttons Functions========
    
    def choose1(self):
        gameChar = self.btn1['text']
        if gameChar == '-':
            data = '1'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose2(self):
        gameChar =  self.btn2['text'] 
        if gameChar == '-':
            data = '2'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose3(self):
        gameChar =  self.btn3['text'] 
        if gameChar == '-':
            data = '3'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose4(self):
        gameChar =  self.btn4['text'] 
        if gameChar == '-':
            data = '4'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose5(self):
        gameChar =  self.btn5['text'] 
        if gameChar == '-':
            data = '5'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose6(self):
        gameChar =  self.btn6['text'] 
        if gameChar == '-':
            data = '6'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose7(self):
        gameChar =  self.btn7['text'] 
        if gameChar == '-':
            data = '7'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose8(self):
        gameChar =  self.btn8['text'] 
        if gameChar == '-':
            data = '8'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")
    def choose9(self):
        gameChar =  self.btn9['text'] 
        if gameChar == '-':
            data = '9'
            self.sendMove(data)
            if_win = self.check_win()
            if not if_win:  
                self.recieveMove()
        else:
            tkinter.messagebox.showinfo("Error: Invalid Move", "Invalid move! Please try again!")

    #=======Button Methods ============================

    def sendMove(self,data):
        move_flag = 2
        data1 = data.encode()
        connectionSocket.send(data1)
        gameBoard.lastuser = gameBoard.username1
        self.setMove(data,move_flag)
        
    #====================Set Move==============================
    def setMove(self,data,move_flag):
        if data == '1':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[0]= 2
                self.btn1['text'] = 'X' 
            else:
                board[0] = 1
                self.btn1['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '2':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[1]= 2
                self.btn2['text'] = 'X'
            else:
                board[1] = 1
                self.btn2['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
          
        if data == '3':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[2]= 2
                self.btn3['text'] = 'X'
            else:
                board[2] = 1
                self.btn3['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
           
        if data == '4':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[3]= 2
                self.btn4['text'] = 'X'
            else:
                board[3] = 1
                self.btn4['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '5':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[4]= 2
                self.btn5['text'] = 'X'
            else:
                board[4] = 1
                self.btn5['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '6':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[5]= 2
                self.btn6['text'] = 'X'
            else:
                board[5] = 1
                self.btn6['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '7':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[6]= 2
                self.btn7['text'] = 'X'
            else:
                board[6] = 1
                self.btn7['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '8':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[7]= 2
                self.btn8['text'] = 'X'
            else:
                board[7] = 1
                self.btn8['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        if data == '9':
            board = gameBoard.returnBoard()
            if move_flag == 2:
                board[8]= 2
                self.btn9['text'] = 'X'
            else:
                board[8] = 1
                self.btn9['text'] = 'O'
            gameBoard.playMoveOnBoard(board)
            
        
     #===============End of Set Move===============   
            
    def recieveMove(self):
        tkinter.messagebox.showinfo('Player 1s Turn', "Please wait for Player 1 to make a move")
        move_flag = 1
        data = connectionSocket.recv(1024).decode('ascii')
        gameBoard.lastuser = gameBoard.username2
        self.setMove(data,move_flag)
        a = self.check_win()
        
        
    def check_win(self):
        win_flag = gameBoard.isGameFinished()
        if ((win_flag == 1) or (win_flag == 2)):
             self.gameEnd(win_flag)
        return win_flag
         

            
    def gameEnd(self,win_flag):
        winner = ''
        if win_flag == 1:
            winner = str(gameBoard.lastuser) +' Won!'
        else:
            winner = 'Game is Tie!'
        data = tkinter.messagebox.askyesno((winner), "Would You Like to Play Again?")
        data = str(data)
        data1 = data.encode()
        connectionSocket.send(data1)
        if data == 'True':
            self.restartGame()
        else:
            self.showStats()

        connectionSocket.send(data1)
        

    def restartGame(self):
        gameBoard.resetGameBoard()
        gameBoard.recordGamePlayed()
        self.btn1['text'] = '-'
        self.btn2['text'] = '-'
        self.btn3['text'] = '-'
        self.btn4['text'] = '-'
        self.btn5['text'] = '-'
        self.btn6['text'] = '-'
        self.btn7['text'] = '-'
        self.btn8['text'] = '-'
        self.btn9['text'] = '-'
        #tkinter.messagebox.showinfo('Next Game Staring', gameBoard.username2+ ' Chose to restart the game')
    
    def showStats(self):
        player2,player1,winner,gamenum, wins, losses, ties = gameBoard.computeStats()
        tkinter.messagebox.showinfo('Game Over: '+player2+' Match Stats - Press OK to Close Game','Player 1 user: Player 1'+'\n' + 'Player 2 user: '+str(player2)+'\n'
                                    +'Last User to Make a Move: '+str(winner)+'\n'
                                    +'Total Games Played: '+str(gamenum)+'\n'
                                    +'Total wins for ' +str(player2)+': '+str(wins)+'\n'
                                    +'Total losses for ' +str(player2)+': '+str(losses)+ '\n'
                                    +'Total ties: '+str(ties)+'\n')
        self.master.destroy()
        

#=============Main Prog Run =====================       
if __name__ == '__main__':
    gameBoard = board.Board()
#create socket object
    global connectionSocket
    connectionSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind host with port number
    root = Tk()
    game = Menu(root)
    root.mainloop()
 
