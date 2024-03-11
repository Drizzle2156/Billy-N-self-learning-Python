# this file is a module
class BalanceException(Exception):
    pass
# this class enables the ability to signal specific errors related to balances. however we do not do anything yet. note that Exception is a built in  base class in python. pass is an empty placeholder, has no methods or attributes defined.


class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
#  creates and prints the 2 bank accounts with initial balances

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
#  just repeats the balance of bank accounts

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()
# creates a function to add a sum to the balance and prints it out

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${
                    self.balance:.2f}"
            )
# viable transaction prevents withdrawals equal to or greater than self.balance

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
# withdraw function

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')
# transfer function


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        # dont forget the order of operations
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()
# our new class inherits all of the attributes of the BankAccount class


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
# new class inheriting interest class
