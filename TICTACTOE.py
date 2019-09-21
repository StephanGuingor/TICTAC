import random

board = [[1,2,3],[4,5,6],[7,8,9]]

def DisplayBoard(board):
    plus = "+"
    side= "-"
    up ="|"
    blank =" "
    
    for i in range(1,14):
        if i == 1 or i == 5 or i == 9 or i == 13:
            print((plus+(side*7))*3+plus)
     
        elif i == 3 or i == 7 or i == 11:
            if i == 3:
                print(up+(blank*3)+str(board[0][0])+(blank*3)+up+(blank*3)+str(board[0][1])+(blank*3)+up+(blank*3)+str(board[0][2])+(blank*3)+up)
            if i == 7:
                print(up+(blank*3)+str(board[1][0])+(blank*3)+up+(blank*3)+str(board[1][1])+(blank*3)+up+(blank*3)+str(board[1][2])+(blank*3)+up)   
            if i == 11:
                print(up+(blank*3)+str(board[2][0])+(blank*3)+up+(blank*3)+str(board[2][1])+(blank*3)+up+(blank*3)+str(board[2][2])+(blank*3)+up)   
        elif i%2==0:
            print((up+(blank*7))*3+up)


    
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def EnterMove():
    global board
    while True:
        answer = int(input("Enter your move: "))
        if answer >=1 and answer <= 9:
            if answer in MakeListOfFreeFields(board):
                if answer == 1 or answer ==2 or answer ==3:
                    board[0][answer-1]= "O"
                    break
                elif answer ==4 or answer ==5 or answer ==6:
                    answer = answer - 3
                    board[1][answer-1]="O"
                    break
                elif answer ==7 or answer ==8 or answer ==9:
                    answer = answer - 6
                    board[2][answer-1]="O"
                    break
        else:
            print("Enter valid input\n")
            
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    available = []
    for row in board:
        for square in row:
            if not square == "X":
                available.append(square)
    return available
            
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
    pass
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    
    pass
#
# the function draws the computer's move and updates the board
#

#Main Loop
print("Welcome to TIC-TAC-TOE")
DisplayBoard(board)
EnterMove()
print(board)