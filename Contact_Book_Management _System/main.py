from shared_files import load_contacts_from_file
from add_contacts import add_contacts
from remove_contacts import remove_contacts
from view_contacts import view_contacts
from search_contacts import search_contacts

def main():
    load_contacts_from_file()
    while True:
        print("\t\tWelcome to the Contact Book Management System")
        print("\t\t\t1. Add Contact")
        print("\t\t\t2. Remove Contact")
        print("\t\t\t3. View All Contacts")
        print("\t\t\t4. Search Contact")
        print("\t\t\t5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_contacts()
            elif choice == 2:
                remove_contacts()
            elif choice == 3:
                view_contacts()
            elif choice == 4:
                search_contacts()
            elif choice == 5:
                print("\tThanks for using Contact Book. Goodbye!")
                break
            else:
                print("\tInvalid choice. Please select a valid option.\n")
        except ValueError:
            print("\tInvalid input! Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()