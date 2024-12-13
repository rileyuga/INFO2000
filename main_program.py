from bankutils import BankAccount, SavingsAccount

def main():
    #BankAccount Test
    print("BankAccount Tests:")


    account = BankAccount(-100) # expected error message
    account = BankAccount(100)
    account.deposit(50)
    print(account)# Expected balance: $150
    account.withdraw(200) # Expected: "Insufficient balance"
    account.withdraw(100)
    print(account) # Expected balance: $50

    #SavingsAccount Test
    print("\nSavingsAccount Tests:")

    savings = SavingsAccount(200, 0.05) # 5% interest rate
    savings.deposit(100) # Expected balance: $300
    savings.apply_interest() # Expected balance after interest: $315
    print(savings) # Expected output: $315

main()
