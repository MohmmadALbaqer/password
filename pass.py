import random
import os  
from colorama import Fore, Style, Back, init

init()

R = f"{Fore.RED}{Style.BRIGHT}"
G = f"{Fore.GREEN}{Style.BRIGHT}"
B = f"{Fore.BLUE}{Style.BRIGHT}"
Y = f"{Fore.YELLOW}{Style.BRIGHT}"
C = f"{Fore.CYAN}{Style.BRIGHT}"
M = f"{Fore.MAGENTA}{Style.BRIGHT}"
W = f"{Fore.WHITE}{Style.BRIGHT}"
D = f"{Fore.BLACK}{Style.BRIGHT}"
ERROR = f"{Y}[{R}!{Y}]{R}"

def clear_screen():
    operating_system = os.name
    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print(f"[!] System unknown!{Style.RESET_ALL}")
    except Exception as e:
        print(f"[ERROR]{W}: {e}")
clear_screen()

print(f"""
{Y}                                                                              
 _____                             _    _____                   ___    _       
|  _  |___ ___ ___ _ _ _ ___ ___ _| |  |   __|___ ___ _ _ ___  __H__ _| |_ _ _ 
|   __| .'|_ -|_ -| | | | . |  _| . |  |__   | -_|  _| | |  _|  [{Back.RED}{Y}P{Style.RESET_ALL}{Y}] |_   _| | |
|__|  |__,|___|___|_____|___|_| |___|  |_____|___|___|___|_|    [{Back.RED}{Y}+{Style.RESET_ALL}{Y}]   | | |_  |
                                                                [{Back.RED}{Y}S{Style.RESET_ALL}{Y}]   |_| |___|
                                                                 V    
{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}""")

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
        length = int(input(f"{B}[{G}+{B}] {G}Enter how long you want the code {Y}[5 - 25] : {B}"))
    except ValueError:
        print(f"{Y}[{R}!{Y}] {R}Please enter the correct code.{W}")
        continue

    if length < 5:
        print(f"{Y}[{R}!{Y}] {R}Please enter a number greater than {Y}4{W}.")
        continue

    password = generate_password(length)
    
    if length <= 25:
        print(f"{G}[{B}*{G}] {M}Password: {G}" + password + W)
    else:
        print(f"{Y}[{R}*{Y}] {M}Password: {R}" + password + W)

    response = input(f"{C}[{M}?{C}] {G}Do you want to try? (y/n): {W}")

    if response.lower() != "y":
        break
print(f"{G}[{B}*{G}] {W}Thank you")
