from helpers.logger import logger

def show_phone(args, contacts):
    if len(args) != 1:
        return logger('error', 'Please provide user name.')
    
    name = args[0]
    
    if contacts.get(name):
        return logger('success', f"{name}'s phone number is {contacts[name]}")
    else:
        return logger('error', f'Contact {name} not found in contacts list')