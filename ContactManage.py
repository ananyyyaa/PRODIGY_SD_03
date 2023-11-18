import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = {"Phone Number": phone_number, "Email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}\nPhone Number: {info['Phone Number']}\nEmail: {info['Email']}\n")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print(f"Editing contact: {name}")
        phone_number = input(f"Enter new phone number for {name}: ")
        email = input(f"Enter new email address for {name}: ")

        contacts[name]["Phone Number"] = phone_number
        contacts[name]["Email"] = email

        save_contacts(contacts)
        print(f"Contact {name} edited successfully!")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")


   

if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("YOUR CONTACT LIST IS FORMED")
            break
        else:
            print("Invalid choice.")
