# we need the 3x3 grid
# we need to accept input from human player
# update the grid
# check if the human player won the game
# then computer player makes a move
# update the grid
# check if computer player won the game
# track wins/losses
# restart game once it is finished or quit at anytime
# have computer try to win

# import necessary
import random

# create a clean board to play
def print_board():
    stop_playing = False
    player_wins = 0
    computer_wins = 0
    turn = 0
    while stop_playing == False:
        board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # print the board
        for loc in range(9):
            print(board[loc], end='  ')
            if loc % 3 == 2:
                print()
        # this is a flag that is True if the human player indicated they want to quit by pressing q
        end_of_game = False
        # the main loop that controls that game
        while True:
            # this loop allows the user to select a new position if his first choice was invalid
            while True:
                # ask the use to make a selection
                x_location = input("Pick a position to play (0-8) or q to quit:")
                # if the human player wants to quit then the end_of_game
                # boolean variable updates to True
                if x_location == 'q':
                    end_of_game = True
                    stop_playing = True
                    break
                # convert his selection to an integer
                x_location = int(x_location)
                # if there is not X or O on the chosen location then add X and continue playing
                if board[x_location] != 'X' and board[x_location] != 'O':
                    # update the board to have the new X
                    board[x_location] = "X"
                    turn += 1
                    break
            # check if the person wanted to quit and break the game if yes
            if end_of_game == True:
                break
            # print the board
            board[x_location] = "X"
            for loc in range(9):
                print(board[loc], end='  ')
                if loc % 3 == 2:
                    print()
            # check for a draw
            if turn == 9:
                print("It's a draw")
                print("Your number of wins:", player_wins)
                print("Computer's number of wins:", computer_wins)
                print()
                break
            # check if the human player won the game
            if board[0] == board[1] == board[2] == 'X' or \
                board[3] == board[4] == board[5] == 'X' or \
                board[6] == board[7] == board[8] == 'X' or \
                board[0] == board[3] == board[6] == 'X' or \
                board[1] == board[4] == board[7] == 'X' or \
                board[2] == board[5] == board[8] == 'X' or \
                board[0] == board[4] == board[8] == 'X' or \
                board[2] == board[4] == board[6] == 'X':
                print("Congrats! You won")
                print()
                player_wins += 1
                print("Your number of wins:", player_wins)
                print("Computer's number of wins:", computer_wins)
                print()
                break
            # computer decision-making to win
            while True:
                if board[0] == board[1] == 'O' and board[2] != 'X': o_location = 2
                elif board[0] == board[3] == 'O' and board[6] != 'X': o_location = 6
                elif board[0] == board[4] == 'O' and board[8] != 'X': o_location = 8
                elif board[1] == board[2] == 'O' and board[0] != 'X': o_location = 0
                elif board[1] == board[4] == 'O' and board[0] != 'X': o_location = 7
                elif board[2] == board[4] == 'O' and board[6] != 'X': o_location = 6
                elif board[2] == board[5] == 'O' and board[8] != 'X': o_location = 8
                elif board[3] == board[6] == 'O' and board[0] != 'X': o_location = 0
                elif board[3] == board[4] == 'O' and board[5] != 'X': o_location = 5
                elif board[4] == board[5] == 'O' and board[3] != 'X': o_location = 3
                elif board[3] == board[4] == 'O' and board[5] != 'X': o_location = 5
                elif board[4] == board[5] == 'O' and board[3] != 'X': o_location = 3
                elif board[4] == board[8] == 'O' and board[0] != 'X': o_location = 0
                elif board[5] == board[8] == 'O' and board[2] != 'X': o_location = 2
                elif board[0] == board[2] == 'O' and board[1] != 'X': o_location = 1
                elif board[0] == board[6] == 'O' and board[3] != 'X': o_location = 3
                elif board[0] == board[8] == 'O' and board[4] != 'X': o_location = 4
                elif board[1] == board[7] == 'O' and board[4] != 'X': o_location = 4
                elif board[2] == board[6] == 'O' and board[4] != 'X': o_location = 4
                elif board[2] == board[8] == 'O' and board[5] != 'X': o_location = 5
                elif board[3] == board[5] == 'O' and board[4] != 'X': o_location = 4
                elif board[6] == board[8] == 'O' and board[7] != 'X': o_location = 7
                elif board[0] == board[1] == 'X' and board[2] != 'O': o_location = 2
                elif board[0] == board[3] == 'X' and board[6] != 'O': o_location = 6
                elif board[0] == board[4] == 'X' and board[8] != 'O': o_location = 8
                elif board[1] == board[2] == 'X' and board[0] != 'O': o_location = 0
                elif board[1] == board[4] == 'X' and board[7] != 'O': o_location = 7
                elif board[2] == board[4] == 'X' and board[6] != 'O': o_location = 6
                elif board[2] == board[5] == 'X' and board[8] != 'O': o_location = 8
                elif board[3] == board[6] == 'X' and board[0] != 'O': o_location = 0
                elif board[3] == board[4] == 'X' and board[5] != 'O': o_location = 5
                elif board[4] == board[5] == 'X' and board[3] != 'O': o_location = 3
                elif board[4] == board[6] == 'X' and board[2] != 'O': o_location = 2
                elif board[4] == board[7] == 'X' and board[1] != 'O': o_location = 1
                elif board[4] == board[8] == 'X' and board[0] != 'O': o_location = 0
                elif board[5] == board[8] == 'X' and board[2] != 'O': o_location = 2
                elif board[0] == board[2] == 'X' and board[1] != 'O': o_location = 1
                elif board[0] == board[6] == 'X' and board[3] != 'O': o_location = 3
                elif board[0] == board[8] == 'X' and board[4] != 'O': o_location = 4
                elif board[1] == board[7] == 'X' and board[4] != 'O': o_location = 4
                elif board[2] == board[6] == 'X' and board[4] != 'O': o_location = 4
                elif board[2] == board[8] == 'X' and board[5] != 'O': o_location = 5
                elif board[3] == board[5] == 'X' and board[4] != 'O': o_location = 4
                elif board[6] == board[8] == 'X' and board[7] != 'O': o_location = 7
                else:
                    # pick a random integer between 0 and 8
                    o_location = random.randint(0, 8)

                # if the position is not taken then place O on it and continue playing
                if board[o_location] != 'X' and board[o_location] != 'O':
                    board[o_location] = 'O'
                    turn += 1
                    break
            print()
            print("The computer chose position", o_location)
            print()
            # check if the computer player won the game
            if board[0] == board[1] == board[2] == 'O' or \
                board[3] == board[4] == board[5] == 'O' or \
                board[6] == board[7] == board[8] == 'O' or \
                board[0] == board[3] == board[6] == 'O' or \
                board[1] == board[4] == board[7] == 'O' or \
                board[2] == board[5] == board[8] == 'O' or \
                board[0] == board[4] == board[8] == 'O' or \
                board[2] == board[4] == board[6] == 'O':
                print("You lost the game!")
                print()
                computer_wins += 1
                print("Your number of wins:", player_wins)
                print("Computer's number of wins:", computer_wins)
                print()
                break
            # print the board
            for loc in range(9):
                print(board[loc], end='  ')
                if loc % 3 == 2:
                    print()
    if stop_playing == True:
        return

print_board()