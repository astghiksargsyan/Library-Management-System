class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner = owner
        self.__balance = initial_balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("enter a valid value")
        else:
            self.__balance +=amount 
            self.__transactions.append(amount)
    def withdraw(self, amount):
        if amount > self.__balance:
            print("enter a valid value")
        else:
            self.__balance -= amount
            self.__transactions.append(amount)
    def get_balance(self):
        return self.__balance
    def get_transactions(self):
        transaction_copy = self.__transactions.copy()
        return transaction_copy
    def __str__(self):
        return f"Amount {self.__owner} Balance {self.__balance }"
    
    def __add__(self, other):
        return BankAccount ("Test", self.__balance + other.__balance)
    @classmethod
    def from_transfer(cls, owner, source_account, amount):
        source_account.withdraw(amount)
        return cls(owner, amount)
    
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)
acc2.withdraw(100)
print(acc1) # Account: Alice, Balance: $1200
print(acc2) # Account: Bob, Balance: $400 
acc3 = acc1 + acc2
print(acc3.get_balance()) # 1600
print(acc1.get_transactions()) # ["+1000", "+200"
acc4 = BankAccount.from_transfer( "Karen", acc1, 300)
print(acc4.get_balance()) # 300
print(acc1.get_balance()) # 90
