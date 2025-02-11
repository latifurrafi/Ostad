from shared_files import contact_list

def search_contacts():
    search_term = input("Enter Name, Phone, or Email to Search: ").strip().lower()
    results = [contact for contact in contact_list if search_term in str(contact.values()).lower()]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']} || Phone: {contact['phone']} || Email: {contact['email']} || Address: {contact['address']}")
        print()
    else:
        print("\tNo contacts found matching the search term.\n")