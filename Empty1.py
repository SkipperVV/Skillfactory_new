import sys

matrix = [[0] * 3 for i in range(3)]
for i in range(3):
    for j in range(3):
        matrix[i][j] = '__ !'


play=True

def print_board(matrix):  # напечатать поле
    print("\033[0m")
    row = 0
    print(f'     {0}    {1}    {2}')
    for element in matrix:
        print(row, '!', *element, ' ')
        row += 1

def is_won(player):
    el=' ' + player + ' !'
    if matrix[0][0] == el and matrix[0][1] == el and matrix[0][2] == el or (
            matrix[1][0] == el and matrix[1][1] == el and matrix[1][2] == el or
            matrix[2][0] == el and matrix[2][1] == el and matrix[2][2] == el or
            matrix[0][0] == el and matrix[1][1] == el and matrix[2][2] == el or
            matrix[2][0] == el and matrix[1][1] == el and matrix[0][2] == el or
            matrix[0][0] == el and matrix[1][0] == el and matrix[2][0] == el or
            matrix[0][1] == el and matrix[1][1] == el and matrix[2][1] == el or
            matrix[0][2] == el and matrix[1][2] == el and matrix[2][2] == el

    ):
        return True
    else:
        return False

def is_again():
    again = input('Type "Y" if you want to play again:  ')
    if again == "Y" or again == "y":
        matrix = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                matrix[i][j] = '__ !'
        print_board(matrix)
        play=True
    else:
        sys.exit("Game over!")


    return play

def ask_input(player):  # input и проверки ввода

    try:
        player_row, player_col = (
            input(f'Enter position (row _ column) using "spase bar" for player "{player}": ').split())
        player_row, player_col = int(player_row), int(player_col)

        if player_row < 0 or player_row > 2 or player_col < 0 or player_col > 2:
            print("\033[31m{}".format('Out of range. Try other digits'))
            print("\033[0m{}".format(''))
            ask_input(player)

            # loop(matrix)
        elif matrix[player_row][player_col] == '__ !':
            return player_row, player_col

        # elif matrix[player_row][player_col] == '__ !':
        #     matrix[player_row][player_col] = ' ' + player + ' !'

        else:
            print('\033[31mThis position already occupied. Do again')
            print("\033[0m")
            ask_input(player)
    except ValueError:
        print("\033[31m{}".format('Wrong input. '))
        print("\033[0mTry again")
        ask_input(player)

def loop(matrix):
    cycle = 0
    while True:
        if bool(cycle % 2):  # чей ход
            player = 'Y'
            print("\033[33m")
        else:
            player = 'X'
            print("\033[36m")

        if cycle == 9:
            print("\033[35m{}".format('Draw in the game. No winner.'))  # проверить на ничью
            print("\033[0m{}".format(''))
        cycle += 1
        row, column = ask_input(player)

        matrix[row][column] = ' ' + player + ' !'
        print('cycle:', cycle)
        print_board(matrix)
        if is_won(player):
            print("\033[31m{}".format(f'Player "{player}" won the game!'))
            print("\033[0m")
            break


        # print("ask_input", row, column)



def game():
    print_board(matrix)
    loop(matrix)

while play:

    game()
    is_again()

