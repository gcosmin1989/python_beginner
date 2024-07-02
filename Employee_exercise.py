class Employee:
    raise_amt = 1.04

    def __init__(self, first, last,email, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developers(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, email, pay, prog_lang):
        super().__init__(first, last, email, pay)
        self.prog_lang = prog_lang


class Managers(Employee):

    def __init__(self, first, last, email, pay, employees=None):
        super().__init__(first, last, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developers('Tom', 'Joy', 'tom.joy@email.com', 5000, 'Python')
dev_2 = Developers('Michelle', 'Obama', 'm.obama@email.com', 75000, 'Java')

mgr_1 = Managers('Joe', 'Bidden', 'joe.b@usa.us', 10000, [dev_1])


mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# print(employ_1.fullName())
# print(Employee.fullName(employ_2))
#
# print(employ_1.pay)
# employ_1.apply_raise()
# print(employ_1.pay)

# print(dev_1.pay)
# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)
