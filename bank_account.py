class Account:
    def __init__(self):
        self.name = ""

    def deposit(self, amount, description = ""):
        """
        A deposit method that accepts an amount and a description.
        The amount is stored in the ledger list.
        """
        
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        """
        A withdraw method that is similar to the deposit method, but the amount
        is stored in the ledger as a negative number. If there are not enough
        funds, nothing is withdrawn nor added to the ledger.
        """
        
        if (self.getBalance() >= amount):
            self.ledger.append({"amount": -amount, "description": description})
        else:
            print("Insufficient Balance")

    def transfer(self, amount, account):
        """
        A transfer method that accepts an amount and another account as arguments.
        The method adds a withdrawal with the amount and the description,
        "Transfer to [Destination Account Name]". The method then adds a deposit
        to the other account with the amount and description, "Transfer from
        [Source Account Name]". If there are not enough funds, nothing is added to
        either ledgers.
        """
  
        if ((self.getBalance()) >= amount):
            self.withdraw(amount, "Transfer to " + account.name)
            account.deposit(amount, "Transfer from " + self.name)

            print("Transferred $" + "{:.2f}".format(amount) + " from " + self.name + " to " + account.name)

        else:
            print("Insufficient Balance")
     
    def getBalance(self):
        """
        A getBalance method that returns the current balance of the account based
        on the deposits, withdrawals, and transfers that have occured.
        """

        balance = 0
        for item in self.ledger:
            balance += item["amount"]

        return balance

class Savings(Account):
    def __init__(self):
        Account.__init__(self)
        self.name = "Savings"
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        balance = 0

        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

            balance += item['amount']

        output = title + items + "\nTotal Balance: $" + "{:.2f}".format(balance)
        return output
                               
class Checkings(Account):
    def __init__(self):
        Account.__init__(self)
        self.name = "Checkings"
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        balance = 0

        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

            balance += item['amount']

        output = title + items + "\nTotal Balance: $" + "{:.2f}".format(balance)
        return output
