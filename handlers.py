def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Please add name and phone to add the contact"
    name, phone = args
    contacts[name] = phone
    return "Contact is added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        return f"Contact {name} doesn't exist. Please add contact first"
    contacts[name] = phone
    return "Contact is changed."

def phone(args, contacts):
    name = args[0]
    if name not in contacts.keys():
        return f"Contact {name} doesn't exist. Please add contact first"
    return f"Contact's {name} phone is {contacts[name]}."

def print_contacts(contacts):
    if len(contacts) > 0:
        print(f'|{'Name':^15}|{'Phone':^15}|')
    for name, phone in contacts.items():
        print(f'|{name:^15}|{phone:^15}|')