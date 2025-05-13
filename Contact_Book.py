#Task-5 --> Contact Book

Contact_Book = {}

def add_contact():
    name = input("\nEnter name: ").strip()
    if name in Contact_Book:
        print("Contact already exists.")
        return
    
    phone = int(input("Enter phone number:"))
    email = input("Enter Email: ")
    address = input("Enter address: ")

    Contact_Book[name] = {
        "Phone" : phone,
        "Email" : email,
        "Address" : address
    }
    print("\nContact added successfully!")

def view_contacts():
    if not Contact_Book:
        print("\nNo contacts available")
        return
    print("\nContact List:")
    for name,details in Contact_Book.items():
        print(f"{name} - {details['Phone']}")

def search_contact():
    search = input("Who do you want: ")
    found = False

    for name,details in Contact_Book.items():
        if search.lower() in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
    
    if not found:
        print("\nNo contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()

    if name not in Contact_Book:
        print("Contact not found.")
        return
    print("Leave field blank to keep current value.")
    phone = int(input("Enter new phone number:")) or Contact_Book[name]['Phone']
    email = input("Enter new Email: ") or Contact_Book[name]['Email']
    address = input("Enter new address: ") or Contact_Book[name]['Address']

    Contact_Book[name] = {
        "Phone" : phone,
        "Email" : email,
        "Address" : address
    }    

    print("\nContact updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()

    if name in Contact_Book:
        del Contact_Book[name]
        print("\nContact deleted successfully.")
    else:
        print("\nContact not found")


def main():

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

    
