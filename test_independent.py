from bank import BankAccount

def test_deposit_independent():
    account = BankAccount(balance=100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_withdraw_independent():
    account = BankAccount(balance=100)
    new_balance = account.withdraw(30)
    assert new_balance == 70