class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return (f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.1f}"
            return True
        else:
            return(f"Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")