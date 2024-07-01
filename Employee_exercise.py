class Employee:
    raise_amount = 1.04

    def __init__(self, name, last, email, pay):
        self.name = name
        self.last = last
        self.email = email
        self.pay = pay

    def fullName(self):
        return f'The full name of the employee is {self.name}  {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


employ_1 = Employee('Tom', 'Joy', 'tom.joy@email.com', 5000)
employ_2 = Employee('Michelle', 'Obama', 'm.obama@email.com', 75000)

print(employ_1.fullName())
print(Employee.fullName(employ_2))

print(employ_1.pay)
employ_1.apply_raise()
print(employ_1.pay)
