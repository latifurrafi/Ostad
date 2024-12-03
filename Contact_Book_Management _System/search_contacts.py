from shared_files import contact_list

def search_contacts():
    try:
        phoneNum_to_search = int(input("Enter Phone Number For Search : "))
        phoneNum_found = False

        for contact in contact_list:
            if contact['phone'] == phoneNum_to_search:
                phoneNum_found = True
                print("\nContact Details:")
                print(f"Name : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print(f"Address : {contact['address']}")
                print(f"\t\tContact With Phone Number {phoneNum_to_search} Founded Successfully.\n")
                break
        
        if not phoneNum_found:
            print("\t\tNo Contact Found With This Number.")
    except ValueError:
        print("\t\tInvalid Input, Please Enter a Valid Phone Number.")
