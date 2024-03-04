

from handlers import add_contact, change_contact, parse_input, phone, print_contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
            print("How can I help you?")
        elif command == "change":
            print(change_contact(args, contacts))
            print("How can I help you?")
        elif command == "phone":
            print(phone(args, contacts))
            print("How can I help you?")
        elif command == "all":
            print_contacts(contacts)
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()