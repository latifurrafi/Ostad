from shared_files import contact_list

def view_contacts():
    if contact_list:
        print("\nAll Contacts:")
        for contact in contact_list:
            print(f"Name: {contact['name']} || Phone: {contact['phone']} || Email: {contact['email']} || Address: {contact['address']}")
        print()
    else:
        print("\tNo contacts found.\n")