number = int(input("Enter number: "))

divisors = []

for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

print(f"the divisor of {number} is {divisors}")