num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]


def is_prime(n):
    if num > 1 or num == 1:
        if len(a) == 0:
            print('PRIME')
        else:
            print('NOT PRIME')
    else:
        print('NOT PRIME')


is_prime(num)