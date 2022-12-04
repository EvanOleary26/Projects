# Tic Tac Toe game in Python

# define the board
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# function to print the board


def print_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-+-+-")

# function to check if the game is over


def game_over():
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
                return False
    return True

# main game loop


def game():
    # print the initial board
    print_board()

    # player 1 plays first
    player = "X"

    while not game_over():
        # get input from player
        print("Player", player, "turn:")
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        # make the move
        board[row-1][col-1] = player

        # print the updated board
        print_board()

        # switch players
        if player == "X":
            player = "O"
        else:
            player = "X"

    # print the result
    if game_over() == True:
        if player == "X":
            print("Player O wins!")
        else:
            print("Player X wins!")
    else:
        print("It's a tie!")

# start the game
game()