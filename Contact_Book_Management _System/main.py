lst = []

print("Welcome To Contacts Management System")
print("1. Add Contacts.")
print("2. Remove Contacts.")
print("3. Search Contacts.")
print("4. View Contacts.")
print("5. Exit")

option = int(input("Enter Your Choice : "))
while True:
    if option == 1:
        add_contacts()

    elif option == 2:
        remove_contacts()

    elif option == 3:
        search_contacts()

    elif option == 4:
        view_contacts()

    elif option == 5:
        print("Thanks For Using Contacts Book.")
        break
