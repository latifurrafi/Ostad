print("Welcome to Calculator Project")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Divison")
print("5. Reminder")

while True:
    Option = int(input("Select an option for Basic Calculator Project : "))
    if Option == 1:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print("Addition :",num1+num2)
        print("\n")

    elif Option == 2:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print("Substraction :",num1-num2)
        print("\n")

    elif Option == 3:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print("Multipication :",num1*num2)
        print("\n")

    elif Option == 4:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : ")) 
        print("Divison :",num1/num2)
        print("\n")

    elif Option == 5:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print("Reminder :",num1%num2)
        print("\n")

    else:
        print("Invalid Choice,Please Choice Valid Option\n")
