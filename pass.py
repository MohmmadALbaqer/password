import random
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def generate_colored_header(text):
    text_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    colored_header = ""
    for char in text:
        text_color = random.choice(text_colors)
        colored_header += text_color + char
    colored_header += Style.RESET_ALL  
    return colored_header

header_text = "R 9 4 X S"
lo = generate_colored_header(pyfiglet.figlet_format(header_text))
print(lo)

insta_text = (
    "--------------------------------------------------\n"
    f"|{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   |\n"
    "--------------------------------------------------"
)
print(insta_text)

print("أروح فدوة لشعر خشمك دروح تابعني على الأنستكرام\n")

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
        length = int(input("العزيز شكد تريد طول الرمز؟ :"))
    except ValueError:
        print("أثول دخل الرمز صحيح.")
        continue

    if length < 1:
        print("مطي دخل رقم أكبر من 0 .")
        continue

    password = generate_password(length)
    
    if length <= 25:
        print(Fore.GREEN + " Password==>: " + password + Style.RESET_ALL)
    else:
        print(Fore.RED + "Password==>: " + password + Style.RESET_ALL)

    response = input(" تريد تعيد بعد تسوي رمز ؟ (y/n): ")

    if response.lower() != "y":
        break
print("يلة أدعبل منا")
