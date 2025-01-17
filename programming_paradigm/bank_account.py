class BankAccount:
    def __init__(self, account_balance):
        self.account_balance=account_balance
        self.initial_balance=0
    def deposit(self, amount):
        self.amount=amount
        self.account_balance+=self.amount
    def withdraw(self, amount):
        self.amount=amount
        self.account_balance-=self.amount
        print (f"Withdrew: {self.amount}$")
    def display_balance(self):
        print (f"Current Balance: {self.account_balance}")