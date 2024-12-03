import os

contact_list = []

def load_contacts_from_file():
    if os.path.exists("contact_file.csv"):
        with open("contact_file.csv", "r") as file:
            for line in file:
                if "Name" in line and "Address" in line:
                    continue
                name, phone, email, address = line.strip().split(" || ")
                contact = {
                    "name": name.title(),
                    "phone": int(phone),
                    "email": email,
                    "address": address.title(),
                }
                contact_list.append(contact)

def save_contacts_to_file():
    file_exists = os.path.exists("contact_file.csv")

    with open("contact_file.csv", "a" if file_exists else "w") as file:  # Append if file exists
        if not file_exists:
            # Write the header only if the file does not exist
            file.write("Name || Phone || Email || Address\n")
        
        # Save only the most recently added contact
        for contact in contact_list[-1:]:
            content = f"{contact['name'].title()} || {contact['phone']} || {contact['email']} || {contact['address'].title()}\n"
            file.write(content)

