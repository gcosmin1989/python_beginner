class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Misha', 2)
cat2 = Cat('Garfield', 4)
cat3 = Cat('Izy', 5)


# 2 Create a function that finds the oldest cat
def oldestCat(*cats):
    return max(cats)


# 3 Print out: "The oldest cat is x years old and her name is". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldestCat(cat1.age, cat2.age, cat3.age)} years old ')
