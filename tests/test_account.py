import pytest

from account import Account

@pytest.fixture
def account_created():
    account = Account("1", "Benjamin", "Berglund", "700109-2456")
    return account

def test_create_account(account_created):
    assert len(account_created.ssn) == 11 or len(account_created.ssn) == 13
    assert account_created.account_number is not None
    assert account_created.account_number != ""

def test_account_deposit(account_created):
    # testdata
    amount_to_deposit = 1000
    # setup
    print(account_created.balance) # 0
    account_created.deposit(amount_to_deposit)
    print(account_created.balance) # 1000
    assert account_created.balance >=  amount_to_deposit

def test_account_withdraw(account_created):
    # testdata
    amount_to_withdraw = 1100
    # setup
    print(account_created.balance)
    account_created.balance -= amount_to_withdraw
    print(account_created.balance)