import re
from shared_files import contact_list, save_contacts_to_file

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def phone_duplicate(phone):
    return any(contact['phone'] == phone for contact in contact_list)

def add_contacts():
    while True:
        try:
            name = input("Enter Name: ").strip()
            if not name.isalpha():
                raise ValueError("\tName must contain only letters.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            phone = input("Enter Phone Number: ").strip()
            if not phone.isdigit():
                raise ValueError("\tPhone number must be an integer.")
            phone = int(phone)
            if phone_duplicate(phone):
                raise ValueError("\tPhone number already exists. Please enter a new phone number.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            email = input("Enter Email: ").strip()
            if not validate_email(email):
                raise ValueError("\tInvalid email format. Please enter a valid email address.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        address = input("Enter Address: ").strip()
        if address:
            break
        print("\tAddress cannot be empty. Please enter a valid address.")

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contact_list.append(contact)
    save_contacts_to_file()
    print("\tContact added successfully!\n")