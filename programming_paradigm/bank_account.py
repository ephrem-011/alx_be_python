class BankAccount:
    def __init__(self, account_balance):
        self.account_balance=account_balance
        self.initial_balance=0
    def deposit(self, amount):
        self.amount=amount
    def withdraw(self, amount):
        self.amount=amount
    def display_balance(self):
        print (f"Current Balance: ${self.account_balance:.2f}")

