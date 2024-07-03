class User:

    def sign_in(self):
        print('Logged In')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows left {self.num_arrows}')

    def arrow_remaining(self):
        print(f'Arrows remaining {self.num_arrows}')
    def runFast(self):
        print('Run really fast')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hybrid1 = Hybrid('HybridBorg', 65, 76)
hybrid1.runFast()
hybrid1.arrow_remaining()




