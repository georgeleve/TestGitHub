#George Leventopoulos TicTacToe

# Game Board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]



#Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a TicTacToe Game
def play_game():
    #Diplay initial board
    current_player = "X"
    display_board()

    #While the game is still going

    winner = check_if_game_over()
    while not(winner):

        #Handle a single turn of an arbitrary player
        handle_turn(current_player)

        #Flip to the enter player
        current_player = flip_player(current_player)

        winner = check_if_game_over()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " player won.")
    else:
        print("Tie.")






#Handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9\n")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input , please choose a position from 1 to 9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can not play in this position.Please try again")

    board[position] = player

    display_board()

def check_if_game_over():
     winner  = check_for_winner()
     if winner:
         return winner
     if check_if_tie():
        return "Tie"
     return False

def check_for_winner():
    #check rows
    row_winner = check_rows()
    #check colums
    colum_winner = check_colums()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #there is no win
        winner = False
    return winner

def check_rows():
    #Set up global variables
    #check if any rows have all the same values
    #and it is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if there is a row match , the game stop
    #Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return False

def check_colums():
    # Set up global variables
    # check if any colums have all the same values
    # and it is not empty
    colum_1 = board[0] == board[3] == board[6] != "-"
    colum_2 = board[1] == board[4] == board[7] != "-"
    colum_3 = board[2] == board[5] == board[8] != "-"
    # if there is a colum match , the game stop
    # Return the winner
    if colum_1:
        return board[0]
    elif colum_2:
        return board[1]
    elif colum_3:
        return board[2]
    return False

def check_diagonals():
    # Set up global variables
    # check if any rows have all the same values
    # and it is not empty
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    # if there is a row match , the game stop
    # Return the winner
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return False


def check_if_tie():
    if "-" not in board:
        return True
    return False

def flip_player(current_player):
    # If the current player is "X" , then changed it to "O"
    if current_player == "X":
        current_player = "O"
    # If the current player is "O" , then changed it to "X"
    elif current_player == "O":
        current_player = "X"
    return current_player


play_game()


# board
# display board
# play game
# handle turn
# check win
    #check rows
    # check colums
    # ckeck diagonals
# check tie
# flip player


