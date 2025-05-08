from easygui import msgbox # for messaging the user
#from pydantic import BaseModel


class Account():
    """
    account: str
    first_name: str
    last_name: str
    ssn: str
    balance: float
    """
    def __init__(self, account_number, first_name, last_name, ssn, balance=0):
        self.account_number = account_number
        self._balance = balance
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return amount
        else:
            msgbox("Account balance too low", 'Transaction not possible')
            return 0

    def get_balance(self):
        return self._balance

"""
class ControlAccount:
    def __init__(self, account_number, first_name, last_name, ssn, balance):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self._balance = balance

class Balance(ControlAccount):
    def __init__(self, account_number, first_name, last_name, ssn, balance):
        # try:
        if self._balance < 0:
            return False
        # except

    def personal_information(self):
"""

