"""
create a bank account class that stores an account holders name and balance 
add instance methods to deposit money, withdraw money and display
the balance 
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


name=input("enter account holder name: ")

balance=float(input("enter opening balance: "))

account=BankAccount(name,balance)

deposit_amount=float(input("enter amount to deposit: "))

account.deposit(deposit_amount)

withdraw_amount=float(input("enter amount to withdraw: "))

account.withdraw(withdraw_amount)

account.display()

