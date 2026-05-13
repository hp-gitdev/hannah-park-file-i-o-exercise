# A simple contacts book using dictionaries

# Each contact is a dictionary; the whole book is dictionary of contacts
contacts = {
    "alice":   {
    "full_name": "Alice Johnson",
    "phone": "555-0101",
    "email": "alice@example.com",
    },
    "bob": {
        "full_name": "Bob Smith",
        "phone": "555-0202",
        "email": "bob@example.com"
    }
}

def display_contacts():
    """Print all contacts in a formatted way."""
    print("\n" + "=" * 40)
    print(" contact book")
    print("=" * 40)

    if not contacts:
        print("No contacts yet.")
        return
    
    for key, info in contacts.items():
        print(f"\n {info['full_name']}")
        print(f"    phone: {info['phone']}")
        print(f"    email: {info['email']}")

    print(f"\nTotal contacts: {len(contacts)}")
    print("=" * 40)

display_contacts()


#Look up a specific contact
search = input("\nLook up a contact (enter first name): ").lower()      # .lower() converts string to lowercase letters.

contact = contacts.get(search)      #.get() returns NONE if not found

if contact:
    print(f"\nFound: {contact['full_name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")

else:
    print(f"No contact found for '{search}.")


# Add a new contact
print("\n--Add New Contact--")
new_key = input("First name (for lookup): ").lower()
new_full = input("Full name: ")
new_phone = input("Phone: ")
new_email = input("Email: ")

contacts[new_key] = {
    "full_name": new_full,
    "phone": new_phone,
    "email": new_email
}

print(f"\n{new_full} added successfully!")
display_contacts()


#output
in both groups: {'bob','diana'}
in A but not B: {'alice', 'charlie'}
in either group: {'alice', 'bob', 'charlie', 'diana', 'eve', 'frank'}