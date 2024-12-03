from shared_files import contact_list, save_contacts_to_file

def remove_contacts():
    try:
        phoneNum_to_remove = int(input("Enter Phone Number For Remove: "))
        phoneNum_found = False

        for contact in contact_list:
            if contact['phone'] == phoneNum_to_remove:
                phoneNum_found = True
                print("\nContact Details:")
                print(f"Name : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print(f"Address : {contact['address']}")
                contact_list.remove(contact)
                save_contacts_to_file()
                print(f"\t\tContact With Phone Number {phoneNum_to_remove} Removed Successfully.\n")
                break

        if not phoneNum_found:
            print("\t\tNo Contact Found With This Number.")
    except ValueError:
        print("\t\tInvalid Input! Please enter a valid phone number.")