import random
import os  
from colorama import Fore, Style, init
from termcolor import colored

os.system("clear")

text = '''
 ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄    .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌
▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█ ▄█▀▄ ▀▄ █·██· ██   ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌
 ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌▐█▌.▐▌▐▀▀▄ ▐█▪ ▐█▌  ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪
▐█▪·•▐█▪ ▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██   ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.
.▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•    ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • 

'''

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

random_color = random.choice(colors)

colored_text = colored(text, random_color)
print(colored_text)

print(f'''
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.instagram.com/r94xs/        {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+
{Style.RESET_ALL}''')

lower = "abcdefghijklmnopwrstuvwxyz"
upper = "ABCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
simbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

all_chars = lower + upper + number + simbols 

def generate_password(length):
    password = "".join(random.choices(all_chars, k=length))
    return password

while True:
    try:
        length = int(input(f"{Fore.GREEN}[+] {Fore.BLUE}Enter how long you want the code {Fore.YELLOW}[5 - 25] :{Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Please enter the correct code.{Style.RESET_ALL}")
        continue

    if length < 5:
        print(f"{Fore.RED}[!] Please enter a number greater than {Fore.YELLOW}4{Fore.WHITE}.{Style.RESET_ALL}")
        continue

    password = generate_password(length)
    
    if length <= 25:
        print(Fore.GREEN + "[*] Password: " + password + Style.RESET_ALL)
    else:
        print(Fore.RED + "[*] Password: " + password + Style.RESET_ALL)

    response = input("[?] Do you want to try? (y/n): ")

    if response.lower() != "y":
        break
print(f"{Fore.BLUE}[+] {Fore.WHITE}Thank you")
