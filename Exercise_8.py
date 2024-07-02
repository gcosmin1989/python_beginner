
# if (player_one == "Rock" and player_two == "Paper") or (player_one == "Paper" and player_two == "Scissors") or (
#         player_one == "Scissors" and player_two == "Rock"):
#     print("Player TWO wins")
# else:
#     print("Player ONE wins")


def game(one, two):
    if one == two:
        print('It\'s a tie')
    elif (one == "Rock" and two == "Paper") or (one == "Paper" and two == "Scissors") or (
            one == "Scissors" and two == "Rock"):
        print('Player Two wins')
    else:
        print('Player Two Wins')


while True:
    player_one = input('Player one:')
    player_two = input('Player two:')

    game(player_one, player_two)

    restart_game = input('Do you want to play again? Y/N ').upper()
    if restart_game == "N":
        print('Game End!')
        break
