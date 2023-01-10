class account:
    def __init__(self, num, bal=100):
        self.acc_num = num
        self.balance = bal

    def withdraw(self, amount):
        if self.balance <= amount+100:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def display(self):
        print("\nThe account number is :", self.acc_num)
        print("The Account balance is :", self.balance)


acc_list = []


def new_account(num):
    for i in acc_list:
        if i.acc_num == num:
            print("Account already present")
            return
    acc_list.append(account(num))


def process(num, operation, amount):
    for i in acc_list:
        if i.acc_num == num:
            if operation == "withdraw":
                i.withdraw(amount)
            elif operation == "deposit":
                i.deposit(amount)
            elif operation == "display":
                i.display()
            return
    print("Error: Account", num, "not found")


def highest_balance():

    highest_balance = 0
    highest_acc = None

    for i in acc_list:
        if i.balance > highest_balance:
            highest_balance = i.balance
            highest_acc = i

    print("Account", highest_acc.acc_num,
          "has the highest balance of", highest_balance)


n = int(input("Enter number of accounts: "))
for i in range(n):
    acc_num = int(input("Enter the account number :"))
    new_account(acc_num)

while (1):
    print("\n1)DEPOSIT\n2)WITHDRAWL\n3)DISPLAY\n4)EXIT\n")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        acc_num = int(input("Enter the account number to be accessed:"))
        amt = int(input("Enter the amount to be deposited:"))
        process(acc_num, "deposit", amt)

    elif ch == 2:
        acc_num = int(input("Enter the account number to be accessed:"))
        amt = int(input("Enter the amount to be withdrawn:"))
        process(acc_num, "withdraw", amt)

    elif ch == 3:
        acc_num = int(input("Enter the account number to be accessed:"))
        process(acc_num, "display", 0)

    elif ch == 4:
        highest_balance()

    elif ch == 5:
        quit()

    else:
        print("Invalid choice")
