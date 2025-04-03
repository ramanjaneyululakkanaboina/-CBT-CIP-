class ContactMaster:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact's name: ")
        phone = input("Enter contact's phone number: ")
        email = input("Enter contact's email: ")
        address = input("Enter contact's address: ")
        self.contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        print(f"Contact for {name} added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}\n")
        print("End of contact list.\n")

    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ")
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['Phone']:
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}\n")
                found = True
        if not found:
            print("No contact found with that name or phone number.\n")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name not in self.contacts:
            print(f"No contact found for {name}.")
            return
        print("Updating contact details for", name)
        phone = input(f"Enter new phone number (current: {self.contacts[name]['Phone']}): ")
        email = input(f"Enter new email (current: {self.contacts[name]['Email']}): ")
        address = input(f"Enter new address (current: {self.contacts[name]['Address']}): ")
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact for {name} updated successfully!\n")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully!\n")
        else:
            print(f"No contact found for {name}.\n")

    def show_menu(self):
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-6): ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting the contact book. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    contact_book = ContactMaster()
    contact_book.run()
