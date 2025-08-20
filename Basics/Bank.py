class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance
    

    def deposit(self,amount):
        self.balance += amount
        print("New Balance:", self.balance)
    

    def withdraw(self, amount):
        self.balance-= amount 
        print("New Balance:", self.balance)
    

    def Details(self):
        print("Owner:", self.owner , "Balance: " ,self.balance)


acc1 = BankAccount("Arvin",5000)

acc1.Details()
acc1.withdraw(1000)
# acc2 = BankAccount("Arv")
# acc2.Details()