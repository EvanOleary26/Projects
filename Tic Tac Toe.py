
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player = [[0,1],["Player 1","Player 2",],["X","O"]]

turn = 0
entry = ""
place = [0,0]

row = ["L","M","B"]
column = ["L","M","R"]


#print board function
def printBoard():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("--+---+--")

#input an entry and check to make sure it works
def inputEntry():
    entry = input("Please input a location for your piece ") 
    while len(entry) != 2:
        entry = input("Please input a location for your piece ") 
    entry = entry.upper()
    
    for i in range(3):
        for j in range (3):
            text = column[j] + row[i]
            if (text == entry):
                place = [j,i]
                break
        if (text == entry):
            break
    #if (text != entry):
    #   inputEntry()
        
        
        
inputEntry()

def placeEntry():
    board[place[0]][place[1]] == player[2][turn]
    printBoard()

            
            
        
            


print("\n"
       "Top row = T \n"
       "Middle row = M \n" 
       "Bottom row = B \n \n" 
       "Left column = L \n"
       "Middle column = M \n"
       "Right column = R \n \n"
       "Column first, then row")
print("an example entry is 'MR','MM','BR' \n")


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