class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance<0:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        else:
            print("no yield due to negitive account balance")
        return self
#################################################################
class User ():
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self 

    def display_user_balance(self):
        print(self.account.balance)
        return self

    def transfer_money(user1, user2, amount):
        user1.account.balance -= amount
        user2.account.balance += amount
 
        print(f"{user1.name} transferred {amount} to {user2.name}")

Chelsea = User("Chelsea")
Weston = User("Weston")
Colby = User("Colby")

Colby.make_withdrawl(500).make_withdrawl(750).make_withdrawl(300).make_deposit(500000).display_user_balance()
Colby.make_deposit(700).display_user_balance()
Colby.account.yield_interest()