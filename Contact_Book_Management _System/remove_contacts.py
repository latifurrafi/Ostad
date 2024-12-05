from shared_files import contact_list, save_contacts_to_file

def remove_contacts():
    try:
        phone_to_remove = int(input("Enter Phone Number to Remove: "))
        contact_found = False

        for contact in contact_list:
            if contact["phone"] == phone_to_remove:
                contact_list.remove(contact)
                save_contacts_to_file()
                contact_found = True
                print("\tContact removed successfully!\n")
                break

        if not contact_found:
            print("\tNo contact found with that phone number.\n")
    except ValueError:
        print("\tInvalid input! Please enter a valid phone number.\n")