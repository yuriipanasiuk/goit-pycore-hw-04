from helpers.logger import logger

def change_contact(args, contacts):
    if len(args) != 2:
        return logger('error', 'Please provide both name and phone number.')
    
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        
        return logger('success', "Contact updated.")
    else:
        return logger('error', f'Contact {name} not found in contacts list')