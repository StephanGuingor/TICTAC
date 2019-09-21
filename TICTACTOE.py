from random import randrange
from random import choice


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
    if VictoryFor(board,"X") and VictoryFor(board,"O"):
        while True:
            answer = int(input("Enter your move: "))
            if answer >=1 and answer <= 9:
                if answer in MakeListOfFreeFields(board):
                    if answer == 1 or answer ==2 or answer ==3:
                        board[0][answer-1]= "O"
                        DisplayBoard(board)
                        break
                    elif answer ==4 or answer ==5 or answer ==6:
                        answer = answer - 3
                        board[1][answer-1]="O"
                        DisplayBoard(board)
                        break
                    elif answer ==7 or answer ==8 or answer ==9:
                        answer = answer - 6
                        board[2][answer-1]="O"
                        DisplayBoard(board)
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
            if not square == "X" and square != "O" :
                available.append(square)
    return available
            
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
 
def VictoryFor(board, sign):
    for i in range(3):
        if sign == board[i][0] and sign == board[i][1] and sign ==board[i][2]:
            print(sign + "s"+" wins!")
            return False
        if sign == board[0][2] and sign ==board[1][2] and sign==board[2][2]:
            print(sign + "s"+" wins!")
            return False
        if sign == board[0][1] and sign ==board[1][1] and sign==board[2][1]:
            print(sign + "s"+" wins!")
            return False
        if sign == board[0][0] and sign ==board[1][0] and sign==board[2][0]:
            print(sign + "s"+" wins!")
            return False

        if sign == board[0][0] and sign ==board[1][1] and sign==board[2][2]:
            print(sign + "s"+" wins!")
            return False
        if sign == board[0][2] and sign ==board[1][1] and sign==board[2][0]:
            print(sign + "s"+" wins!")
            return False

        elif not (1 in MakeListOfFreeFields(board) and 2 in MakeListOfFreeFields(board) or 3 in MakeListOfFreeFields(board) or 4 in MakeListOfFreeFields(board)\
            or 5 in MakeListOfFreeFields(board) or 6 in MakeListOfFreeFields(board) or 7 in MakeListOfFreeFields(board) \
            or 8 in MakeListOfFreeFields(board) or 9 in MakeListOfFreeFields(board)):
            print("Tie")
            return False
        else:
            return True
   
    
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove():
    if VictoryFor(board,"X") and VictoryFor(board,"O"):
        answer = choice(MakeListOfFreeFields(board))
        while True:
            if answer >=1 and answer <= 9:
                if answer in MakeListOfFreeFields(board):
                    if answer == 1 or answer ==2 or answer ==3:
                        board[0][answer-1]= "X"
                        DisplayBoard(board)
                        break
                    elif answer ==4 or answer ==5 or answer ==6:
                        answer = answer - 3
                        board[1][answer-1]="X"
                        DisplayBoard(board)
                        break
                    elif answer ==7 or answer ==8 or answer ==9:
                        answer = answer - 6
                        board[2][answer-1]="X"
                        DisplayBoard(board)
                        break
            else:
                listx = MakeListOfFreeFields(board)
                print(listx)
                answer = randrange(9)
                if answer in MakeListOfFreeFields(board):
                    continue
                else:
                    answer = randrange(9)
                    if answer in MakeListOfFreeFields(board):
                        continue
    
  

# the function draws the computer's move and updates the board
#
def MainLoop(board,sign1,sign2):
    print("Welcome to TIC-TAC-TOE")
    while True:
        DisplayBoard(board)    
        EnterMove()
        if not (VictoryFor(board, sign1) and VictoryFor(board, sign2)):
            break
        DrawMove()
        if not (VictoryFor(board, sign1) and VictoryFor(board, sign2)):
            break
#Calling the GAME
board = [[1,2,3],[4,5,6],[7,8,9]]
MainLoop(board,"X","O")

