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


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Hawk Eye', 100)
wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()


def player_attack(character):
    character.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()