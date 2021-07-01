import bank_account as b

def displayMenu():
    print("MENU")
    print("1.  View Balances")
    print("2.  Deposit")
    print("3.  Withdraw")
    print("4.  Transfer")
    print("5.  Account Summary")
    print("6.  Exit")
    print()

def main():
    displayMenu()
    
    savings = b.Savings()
    checkings = b.Checkings()

    while True:
        option = int(input("Enter a menu option: "))
        print()

        if option == 1:
            print(f"{savings.name:*^30}\n")
            s_balance = savings.getBalance()
            print("Balance: $" + "{:.2f}".format(s_balance))
            print("\n")
            
            print(f"{checkings.name:*^30}\n")
            c_balance = checkings.getBalance()
            print("Balance: $" + "{:.2f}".format(c_balance))
            print("\n")  
            continue
                
        if option == 2:
            print("Please select an account to make a deposit.")
            account = input("('S' for Savings or 'C' for Checkings): ")
            amount = float(input("Enter an amount: "))
            print()

            if account.upper() == 'S':
                savings.deposit(amount, "Deposit")
                print("Amount Deposited: $" + "{:.2f}".format(amount))
                print()   
            elif account.upper() == 'C':
                checkings.deposit(amount, "Deposit")
                print("Amount Deposited: $" + "{:.2f}".format(amount))
                print()        
            else:
                account = input("Please select an account: ")
            continue

        if option == 3:
            print("Please select an account to make a withdrawal.")
            account = input("('S' for Savings or 'C' for Checkings): ")
            amount = float(input("Enter an amount: "))
            print()

            if account.upper() == 'S':
                savings.withdraw(amount, "Withdrawal")
                print("Amount Withdrawn: $" + "{:.2f}".format(amount))
                print()     
            elif account.upper() == 'C':
                checkings.withdraw(amount, "Withdrawal")
                print("Amount Withdrawn: $" + "{:.2f}".format(amount))
                print()            
            else:
                account = input("Please select an account: ")
            continue

        if option == 4:
            print("('S' for Savings or 'C' for Checkings)")
            account = input("Select the account you wish to transfer from: ")
            amount = float(input("Enter the amount you wish to transfer: "))
            print()

            if account.upper() == 'S':
                savings.transfer(amount, checkings)
                print()
            elif account.upper() == 'C':
                checkings.transfer(amount, savings)
                print()
            else:
                account = input("Please select an account: ")
            continue
                
        if option == 5:
            print(savings)
            print("\n")
            print(checkings)
            print("\n")

        if option == 6:
            print("Bye!")
            exit()

if __name__ == "__main__":
    main()
