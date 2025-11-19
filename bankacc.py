class BankAccount:
    def __init__(self,acc_no,name,acc_type,balance=0):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"${amount} deposited successfully\n")
        else:
            print(f"Deposit amount cannot be negative")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        elif amount<0:
            print("Withdrawal amount cannot be negative")
        else:
            self.balance-=amount
            print(f"{amount} withdrawn successfully")

    def display(self):
        print("\n---Account Details---\n")
        print(f"Account Number:{self.acc_no}")
        print(f"Name:{self.name}")
        print(f"Account Type:{self.acc_type}")
        print(f"Balance:{self.balance}")

acc1=BankAccount(123456,"Lakshmi","Savings",5000)
acc1.display()

acc1.deposit(1500)
acc1.withdraw(2000)
acc1.withdraw(6000)

acc1.display()




        