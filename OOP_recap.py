# class Computer:
#
#     def __init__(self, cpu, ram, hdd):
#         self.cpu = cpu
#         self.ram = ram
#         self.hdd = hdd
#
#     def config(self):
#         print(f'The computer has {self.cpu}, {self.ram} RAM, {self.hdd} TB')
#
#
# com1 = Computer('i7', 16, 1)
# com1.config()
# com2 = Computer('Ryzen 5', 32, 2)
# com2.config()

########################################################################

# class Car:
#     wheels = 4
#
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BMW'
#
#
# car1 = Car()
# car2 = Car()
#
# car1.mil = 20
# car2.com = 'Ford'
#
# print(car1.com, car1.mil, car1.wheels)
# print(car2.com, car2.mil, car2.wheels)

########################################################################

# class Student:
#     university = 'UPB'
#
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()
#
#     def show(self):
#         print(self.name, self.rollno)
#
#     class Laptop:
#
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(self.brand, self.cpu, self.ram)
#
#
# s1 = Student('Henry', 1)
# s2 = Student('John', 3)
#
# s1.show()
# s1.lap.show()

########################################################################

# class A:
#
#     def feature1(self):
#         print('Feature 1 working')
#
#     def feature2(self):
#         print('Feature 2 working')
#
#
# a1 = A()
#
# a1.feature1()
# a1.feature2()
#
#
# class B():
#
#     def feature3(self):
#         print('Feature 3 working')
#
#     def feature4(self):
#         print('Feature 4 working')
#
#
# class C(A, B):
#
#     def feature5(self):
#         print('Feature 5 working')
#
#
# b1 = B()
# b1.feature4()
#
# c1 = C()
# c1.feature1()
# c1.feature3()
# c1.feature5()

########################################################################

# class A:
#
#     def __init__(self):
#         print('In A init')
#
#     def feature1(self):
#         print('Feature 1 working')
#
#     def feature2(self):
#         print('Feature 2 working')
#
#
# class B(A):
#
#     def __init__(self):
#         super().__init__()
#         print('In B init')
#
#     def feature3(self):
#         print('Feature 3 working')
#
#     def feature4(self):
#         print('Feature 4 working')
#
#
# b1 = B()

########################################################################


class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Conventional Check")
        print("Compiling MyEditor")
        print("Running MyEditor")
class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
