from shared_files import load_contacts_from_file, save_contacts_to_file
from add_contacts import add_contacts
from view_contacts import view_contacts
from remove_contacts import remove_contacts
from search_contacts import search_contacts

def main():
    load_contacts_from_file()

while True:
    print("\t\tWelcome To Contacts Books System")
    print("\t\t\t1. Add Contacts.")
    print("\t\t\t2. Remove Contacts.")
    print("\t\t\t3. Search Contacts.")
    print("\t\t\t4. View All Contacts.")
    print("\t\t\t5. Exit")

    try:
        option = int(input("Enter Your Choice : "))
    except ValueError:
        print("Invalid Input, Please Enter a Number Between 1 to 5")
        continue

    if option == 1:
        add_contacts()

    elif option == 2:
        remove_contacts()

    elif option == 3:
        search_contacts()

    elif option == 4:
        view_contacts()

    elif option == 5:
        print("\t\tThanks For Using Contacts Book.")
        break

    else:
        print("Invalid Choice. Please Try Again")
    

if __name__ == "__main__":
    main()