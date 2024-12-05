import os

contact_list = []

def load_contacts_from_file():
    if os.path.exists("contact_file.csv"):
        with open("contact_file.csv", "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                if line.strip(): 
                    name, phone, email, address = line.strip().split(" || ")
                    contact = {
                        "name": name.strip(),
                        "phone": int(phone.strip()),
                        "email": email.strip(),
                        "address": address.strip(),
                    }
                    contact_list.append(contact)

def save_contacts_to_file():
    with open("contact_file.csv", "w") as file:
        file.write("Name || Phone || Email || Address\n")
        for contact in contact_list:
            file.write(f"{contact['name']} || {contact['phone']} || {contact['email']} || {contact['address']}\n")