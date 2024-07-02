
# if (player_one == "Rock" and player_two == "Paper") or (player_one == "Paper" and player_two == "Scissors") or (
#         player_one == "Scissors" and player_two == "Rock"):
#     print("Player TWO wins")
# else:
#     print("Player ONE wins")

player_one_name = input('PLayer One Name: ')
player_two_name = input('PLayer two Name: ')
def game(one, two):
    if one == two:
        print('It\'s a tie')
    elif (one == "Rock" and two == "Paper") or (one == "Paper" and two == "Scissors") or (
            one == "Scissors" and two == "Rock"):
        print(f'Player {player_two_name} wins')
    else:
        print(f'Player {player_one_name} Wins')


while True:
    player_one = input('Player one:').capitalize()
    player_two = input('Player two:').capitalize()

    game(player_one, player_two)

    restart_game = input('Do you want to play again? Y/N ').upper()
    if restart_game == "N":
        print('Game End!')
        break
