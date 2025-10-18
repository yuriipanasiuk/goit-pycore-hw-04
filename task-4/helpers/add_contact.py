from helpers.logger import logger


def add_contact(args, contacts):
    if len(args) != 2:
        return logger('error', 'Please provide both name and phone number.')
    
    name, phone = args

    if contacts.get(name) != None:
        print(logger('warning', f"Contact '{name}' already exists with number {contacts[name]}."))
        confirm = input("Do you want to overwrite it? (y/n): ").strip().lower()

        if confirm == 'y':
            contacts[name] = phone
            return logger('success', f"Contact '{name}' updated.")
        else:
            return logger('info', "Contact not changed.")
        
    else:
        contacts[name] = phone

    return logger('success', "Contact added.")