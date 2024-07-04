class Calculator:
    def add(self, x, y):
        return x + y

    def substraction(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            print("Cannot divide by zero")
        else:
            return x / y

    def power(self, x, y):
        return x**y


calc1 = Calculator()
print(calc1.add(2, 5))
print(calc1.div(1,2))
print(calc1.power(2,2))

