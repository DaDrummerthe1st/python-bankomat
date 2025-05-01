from easygui import msgbox # for messaging the user


class Account:
    def __init__(self, account_number, first_name, last_name, ssn, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0

    def get_balance(self):
        return self.balance