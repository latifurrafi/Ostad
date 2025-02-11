class Bank_System:
    def __init__(self, user_name, intial_balance):
        self.name = user_name
        self.balance = intial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount}$ add Succesfully.")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Amount {amount}$ Withdrawal Successfully.")
        else:
            return f"Insufficient Balance"
        
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    print("\t\tWelcome To Bank Management System.")
    bank_account = None
    while True:
        print("\t\t\t1. Deposite Balance")
        print("\t\t\t2. Withdraw Balance")
        print("\t\t\t3. Check Balance")
        print("\t\t\t4. Exit")

        try:
            option = int(input("Enter Your Choice : "))
        except ValueError:
            print("Invalid Input. Please Enter A Number.")
            continue

        if option == 1:
            if not bank_account:
                name = input("Enter Your Name : ")
                amount = int(input("Enter Initial Amount For Deposite : "))
                bank_account = Bank_System("name",amount)
                print(f"Account {name} Created And Amount {amount}$ Add Succesfully.")
            else:
                amount = int(input("Enter Amount For Deposite : "))
                bank_account.deposit(amount)
        
        elif option == 2:
            if not bank_account:
                print("No Account Exists.")
            else:
                amount = int(input("Enter Your Amount For Withdrawal : "))
                bank_account.withdraw(amount)

        elif option == 3:
            if not bank_account:
                print("No Account Exists.")
            else:
                print(f"Total Balance : {bank_account.get_balance()}$")

        elif option == 4:
            print("Thanks For Using The Bank System.")
            break

        else:
            print("Invalid Choice. Please Choose A Valid Option.")


print("Rafi")