
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player = [[0,1],["Player 1","Player 2",],["X","O"]]

turn = 0

def instructions():
    print("\n"
       "Top row = T \n"
       "Middle row = M \n" 
       "Bottom row = B \n \n" 
       "Left column = L \n"
       "Middle column = M \n"
       "Right column = R \n \n"
       "Column first, then row")
    print("an example entry is 'MR','TL','RM'")

#print board function
def printBoard():
    print()
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("--+---+--")

#input an entry and check to make sure it works
def inputEntry(x = "Please input a valid location for your piece "):
    global place
    row = ["T","M","B"]
    column = ["L","M","R"]
    
    entry = input("" + x) 
    while len(entry) != 2:
        entry = input("" + x) 
    entry = entry.upper()
    
    for i in range(3):
        for j in range (3):
            text = row[i] + column[j]
            if (text == entry):
                place = [i,j]         
                break
        if (text == entry):
            break
    
#place a vailid entry on the board
def placeEntry():
    while True:
        if board[place[0]][place[1]] == "X" or board[place[0]][place[1]] == "O":
            inputEntry("Please input an unused location ")
        else:
            board[place[0]][place[1]] = player[2][turn]
            printBoard()
            break
        
#return true if game is over false if not  
def gameOver():
    global full
    full = False
    
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
    # check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    # check if the board is full
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                full = False
                return False
            else: 
                full = True
            
    
    return True
    
     

instructions()

while not gameOver():
    print(f"\nIt's {player[1][turn]}'s turn\n")
    
    inputEntry()
    
    placeEntry()
    
    gameOver()
    
    if not gameOver():
        turn = 1 if turn == 0 else 0

if full == True:
    print("\nTie game!")
else:
    print(f"\n{player[1][turn]} wins!")
    
exit()
    





#make function for checking if valid entry
#make function check if win         
          
        
        
    


"""
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
"""