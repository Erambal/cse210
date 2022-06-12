# Tic Tac Toe
# Author Kendrikc Rambal

gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in gameBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def main():

    turn = 'X'
    count = 0

    i = 0
    while i <= 9:
        printBoard(gameBoard)
        print("It's your turn, " + turn + ". Choose a spot.")

        move = input()

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That spot is already filled.\nChoose another spot.")
            continue

        if count >= 5:
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':  # across the top
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':  # across the middle
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':  # across the bottom
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':  # down the left side
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':  # down the middle
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':  # down the right side
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ':  # diagonal
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':  # diagonal
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            gameBoard[key] = " "

        main()


if __name__ == "__main__":
    main()
