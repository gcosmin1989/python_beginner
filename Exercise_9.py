import random

number = str(random.randint(1, 9))
count = 0
count_guess = 0
while True:
    user_number = input('Guess a number from 1 to 9 ')
    if user_number == 'Exit':
        print(f'You Exit the game with a guess of {count}')
        break
    count_guess = count_guess + 1

    if user_number == number:
        count = count + 1
        print(f'You guessed the number with {count_guess} tries ')
        number = str(random.randint(1, 9))

    elif user_number > number:
        print('Your number is Greater than the number generated!')

    else:
        print('Your number is Lower than the number generated')
