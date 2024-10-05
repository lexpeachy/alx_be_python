#Define a class named BankAccount.
#Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
class Backaccount():
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.
    def deposit_amount(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print(f"You can't deposite a negative amount")
    def withdraw_amount(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print(f"Insufficient funds.")
            return False
    def display_balance(self):
        print(f"Your current account balance is {self.account_balance}")
