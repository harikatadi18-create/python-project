import datetime
class ATM:
    def __init__(self):
        self.balance=10000
        self.pin="1234"
        self.attempts=0
        self.transaction_history=[]
    def authenticate(self):
        pin=input("enter your PIN: ")
        for attempt in range(3):
            pin=input(f"enter your PIn({3-attempt} attempts remaining):")
            if pin == self.pin:
                self.attempts=0
                return True
            else:
                print("Incorrect PIN.Try again")
        print("maximum attempts reached.card blocked!")
        return False
    def check_balance(self):
        print(f"your balance is {self.balance}")
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount!")
        elif amount>self.balance:
            print("Insuffient balance!")
        elif amount % 100 != 0:
            print("Invalid amount.please enter a multiple of 100")
        else:
            self.balance -= amount
            print(f"withdrawal successful. Remaining balance: {self.balance}")
            self.log_transaction("withdraw",amount)
    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount!")
        else:
            self.balance += amount
            print(f"Deposit successful. New balance:{self.balance}")
            self.log_transaction("Deposit",amount)
    def log_transaction(self,type,amount):
        transaction={
            "type":type,
            "amount":amount,
            "balance":self.balance,
            "datetime":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.transaction_history.append(transaction)
    def print_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet!")
        else:
            print("\n transaction History:")
            for i, transaction in enumerate(self.transaction_history,start=1):
                print(f"{i}. Type:{transaction['type']},Amount: {transaction['amount']},Balance:{transaction['balance']},Datetime:{transaction['datetime']}")
atm=ATM()
if atm.authenticate():
    while True:
        print("\n1.check balance")
        print("2.withdraw")
        print("3.Deposit")
        print("4.Transaction histroy")
        print("5.Exit")
        choice=int(input("enter your choice: "))
        if choice==1:
            atm.check_balance()
        elif choice==2:
            amount=int(input("enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice==3:
            amount=int(input("enter amount to deposit: "))
            atm.deposit(amount)
        elif choice==4:
            atm.print_transaction_history()
        elif choice==5:
            break
        else:
            print("Invalid choice.Try again1")
else:
    print("Account blocked")