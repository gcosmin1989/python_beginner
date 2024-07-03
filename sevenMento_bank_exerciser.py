class Bank:
    initial_money = 0

    def __init__(self):
        self.customer = {}

    def create_account(self, acc_no):
        if acc_no not in self.customer:
            self.customer[acc_no] = self.initial_money
            print(f'The account {acc_no} has been created')
        else:
            print('Account already exists')

    def deposit_money(self, acc_no, value):
        if acc_no in self.customer:
            self.customer[acc_no] += value
        else:
            print(f'Account does not exist')

    def withdraw_money(self, acc_no, value):
        if acc_no in self.customer and self.customer[acc_no] >= 0:
            if self.customer[acc_no] - value < 0:
                print(f'Insufficient funds')
            else:
                self.customer[acc_no] -= value
        else:
            print(f'Account does not exist to withdraw')

    def check_balance(self, acc_no):
        if acc_no in self.customer:
            print(f'Your account balance is: {self.customer[acc_no]}')
        else:
            print(f'Account does not exist')


client1 = Bank()
client1.check_balance(1)
client1.create_account(1)
client1.check_balance(1)
client1.deposit_money(1, 100)
client1.check_balance(1)
client1.withdraw_money(1, 50)
client1.check_balance(1)
client1.withdraw_money(1, 75)
client1.check_balance(1)

