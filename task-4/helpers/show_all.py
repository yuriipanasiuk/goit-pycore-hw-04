from helpers.logger import logger
from colorama import Fore

def show_all(contacts):
    if not contacts:
        return logger('info', 'Contacts list are empty')
    
    for name, phone in contacts.items():
        print(f"{Fore.CYAN}name:{Fore.RESET} {name}, {Fore.GREEN}phone_number:{Fore.RESET} {phone}")

