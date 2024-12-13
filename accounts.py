class BankAccount:
    #initializes the account with defual 0 balance
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    #adds given amount to the account
    def deposit(self, amount):
        if amount <= 0:
            return "Deposit must be positive"
        self.balance += amount
        return f"Deposited ${amount}"

    #subtracts amount from account
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}"

    #returns balance
    def check_balance(self):
        return self.check_balance

    #returns info about account
    def __str__(self):
        return f"Checking Account Balance: ${self.balance}"

class SavingsAccount(BankAccount):
    #initialize account
    def __init__(self, initial_balance=0, interest_rate=0.02):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    #deposits into account
    def deposit(self, amount):
        if amount <= 0:
            return "Deposit must be positive"
        self.balance += amount
        return f"Deposited ${amount}"

    #subtracts amount from account
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}"

    #returns balance
    def check_balance(self):
        return f"Balance: ${self.balance}"

    #increase balance by interest rate
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
        return f"Balance: ${self.balance}"

    #returns info about account
    def __str__(self):
        return f"Savings Account Balance: ${self.balance}, Interest Rate: {self.interest_rate}"
