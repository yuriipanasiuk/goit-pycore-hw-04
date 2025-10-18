from typing import Literal
from colorama import Fore, init
init(autoreset=True)

Status = Literal['info', 'success', 'warning', 'error']

def logger(status: Status, message: str):
    match status:
        case 'info':
            return f"{Fore.CYAN}[INFO]{Fore.RESET} {message}"
        case 'success':
            return f"{Fore.GREEN}[SUCCESS]{Fore.RESET} {message}"
        case 'warning':
            return f"{Fore.YELLOW}[WARNING]{Fore.RESET} {message}"
        case 'error':
            return f"{Fore.RED}[ERROR]{Fore.RESET} {message}"
        case _:
            return(f'{Fore.LIGHTMAGENTA_EX}{message}')

