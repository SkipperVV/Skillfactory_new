def create_matrix():
    matrix = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = '__ !'
    return matrix


def print_board(matrix):  # напечатать поле
    print("\033[0m")
    row = 0
    print(f'     {0}    {1}    {2}')
    for element in matrix:
        print(row, '!', *element, ' ')
        row += 1


def is_won(matrix, player):
    el = ' ' + player + ' !'
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
    print("\033[0m")
    again = input('Type "Y" if you want to play again:  ')
    if again == "Y" or again == "y":
        play = True
    else:
        play = False

    return play


def ask_input(matrix, player, color):
    while True:  # input и проверки ввода

        try:
            player_row, player_col = (
                input(f'{color}Enter position (row _ column) using "spase bar" for player "{player}": ').split())
            player_row, player_col = int(player_row), int(player_col)

            if player_row < 0 or player_row > 2 or player_col < 0 or player_col > 2:
                print("\033[31m{}".format('Out of range. Try other digits'))
                print("\033[0m{}".format(''))

            elif matrix[player_row][player_col] == '__ !':
                return player_row, player_col

            else:
                print('\033[31mThis position already occupied. Do again')
                print("\033[0m")

        except ValueError:
            print("\033[31m{}".format('Wrong input. '))
            print("\033[0mTry again")


def loop(matrix):
    cycle = 0
    while True:
        if bool(cycle % 2):  # чей ход
            player = 'Y'
            color = "\033[33m"

        else:
            player = 'X'
            color = "\033[36m"

        if cycle == 9:
            print("\033[35mDraw in the game. No winner.")  # проверить на ничью
            break
        cycle += 1
        row, column = ask_input(matrix, player, color)

        matrix[row][column] = ' ' + player + ' !'
        print('cycle:', cycle)
        print_board(matrix)
        if is_won(matrix, player):
            print(f"{color}Player {player} won the game!")
            break

def game():
    play = True
    while play:
        matrix = create_matrix()
        print_board(matrix)
        loop(matrix)
        play = is_again()


game()
print('Game over. See you next time, amigo! :)')
