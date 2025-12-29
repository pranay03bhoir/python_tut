class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}')
            print(f'New balance is: {self.balance}')
        else:
            print(f'{amount} is an invalid amount.')

    def withdraw(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal: {amount}')
            print(f'New Balance: {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount.')
            else:
                print('Insufficient funds.')
                print(f'Current balance is {self.balance}')