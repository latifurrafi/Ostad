import re
from shared_files import contact_list, save_contacts_to_file

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def phone_duplicate(contact_book, phone):
    for new_contact in contact_book:
        if new_contact["phone"] == phone:
            return True
    return False

def add_contacts():
    while True:
        try:
            name = input("Enter Name: ")
            if not name.isalpha():
                raise ValueError("Name must contain only letters.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            phone = input("Enter Phone Number: ")
            if not phone.isdigit():
                raise ValueError("Phone number must be in Digit.")
            phone = int(phone)
            if phone_duplicate(contact_list, phone):
                raise ValueError("Phone Number Already Exists, Please Enter New Phone Number. ")
            break
        except ValueError as e:
            print(e)


    email = input("Enter Email : ")
    while not validate_email(email):
        print("Invalid Email. Please try agian.")
        email = input("Enter Email : ")

    address = input("Enter Address : ")
    if not address.strip():
        print("Address Cannot Be Empty.")

    new_contact = {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address" : address
    }
    contact_list.append(new_contact)
    save_contacts_to_file()
    print("\t\tContact Add Successfully.\n")