import sys

arr = [[0] * 3 for i in range(3)]
for i in range(3):
    for j in range(3):
        arr[i][j] = '__ !'


def print_matrix():
    print("\033[0m")
    row = 0
    print(f'     {0}    {1}    {2}')
    for s in arr:
        print(row, '!', *s, ' ')
        row += 1

print_matrix()

def again():
    again = input('Type "Y" if you want to play again:  ')
    if again == "Y" or again == "y":
        for i in range(3):
            for j in range(3):
                arr[i][j] = '__ !'
        print_matrix()
        Game()
    else:
        print('Goodby, my friend :)')
        sys.exit('Game over')

def Game():
    cycle = 0

    while True:
        if bool(cycle % 2):
            X_O = 'Y'
            print("\033[33m")
        else:
            X_O = 'X'
            print("\033[36m")

        if cycle == 9:
            print("\033[35m{}".format('Draw in the game. No winner.'))
            print("\033[0m{}".format(''))
            again()

        try:
            player_row, player_col = (
                input(f'Enter position (row _ column) using "spase bar" for player "{X_O}": ').split())
            player_row, player_col = int(player_row), int(player_col)
            if player_row < 0 or player_row > 2 or player_col < 0 or player_col > 2:
                print("\033[31m{}".format('Out of range. Try other digits'))
                print("\033[0m{}".format(''))
                # player(X_O)
            elif arr[player_row][player_col] == '__ !':
                arr[player_row][player_col] = ' ' + X_O + ' !'
                cycle += 1
                print('cycle:', cycle)
                print_matrix()
                el = arr[player_row][player_col]
                if arr[0][0] == el and arr[0][1] == el and arr[0][2] == el or (
                        arr[1][0] == el and arr[1][1] == el and arr[1][2] == el or
                        arr[2][0] == el and arr[2][1] == el and arr[2][2] == el or
                        arr[0][0] == el and arr[1][1] == el and arr[2][2] == el or
                        arr[2][0] == el and arr[1][1] == el and arr[0][2] == el or
                        arr[0][0] == el and arr[1][0] == el and arr[2][0] == el or
                        arr[0][1] == el and arr[1][1] == el and arr[2][1] == el or
                        arr[0][2] == el and arr[1][2] == el and arr[2][2] == el

                ):
                    print("\033[31m{}".format(f'Player "{X_O}" won the game!'))
                    print("\033[0m{}".format(''))
                    again()

            else:
                print('\033[31mThis position already occupied. Do again')
                print("\033[0m")

                # player(X_O)
        except ValueError:
            print("\033[31m{}".format('Wrong input. '))
            print("\033[0mTry again")

Game()
