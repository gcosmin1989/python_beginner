number = int(input('Enter a number: '))

if number % 2 == 0:
    if number % 4 == 0:
        print('The number is even and a multiple of 4')
    else:
        print('The number is even')
else:
    print('The number is odd')

num = int(input('Enter a number to check: '))
check = int(input('Enter a number to divide by: '))

if num % check == 0:
    print(f'{check} divides evenly into {num}')
else:
    print(f'{check} does not divide evenly into {num}')