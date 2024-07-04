from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [11, 22, 33]


def multiply(item):
    return item * 2


print(list(map(multiply, my_list)))


def is_odd(item):
    return item % 2 != 0


def acumulator(acc, item):
    return acc + item


print(list(filter(is_odd, my_list)))

print(list(zip(my_list, your_list, their_list)))

print(reduce(acumulator, my_list, 0))

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_words(word):
    return word.capitalize()


print(list(map(capitalize_words, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def score_filter(score):
    if score > 50:
        return True


print(list(filter(score_filter, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumultator_list(number, score):
    return number + score


print(reduce(accumultator_list, (my_numbers + scores)))
