def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "exit" or user_input == "close":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        else:
            command, *args = parse_input(user_input)
            if command == "add":
                message = add_contact(contacts, *args)
                print(message)
            elif command == "change":
                message = change_contact(contacts, *args)
                print(message)
            elif command == "phone":
                message = show_phone(contacts, *args)
                print(message)
            elif command == "all":
                message = show_all(contacts)
                print(message)
            else:
                print("Invalid command. Please try again.")

def parse_input(user_input):
    return user_input.split()

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts saved."

if __name__ == "__main__":
    main()
