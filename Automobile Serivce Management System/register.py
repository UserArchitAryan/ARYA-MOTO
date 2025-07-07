import pyfiglet


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def style_line(text):
    styled = ""
    for ch in text:
        if ch == "#":
            styled += MAGENTA + ch
        elif ch == "-":
            styled += GREEN + ch
        else:
            styled += YELLOW + ch
        styled += RESET
        return styled


def main():
    print("\n" * 2)
    text = pyfiglet.print_figlet(text = "Registration", colors = "YELLOW", width = 100)
    print("\n" * 2)
D = main()
def display_registration():
    print("\n" * 2)
    print("Welocme and Thank you for registering with ARYA-MOTO!")
    print(style_line("#" * 100))
    print(f"{YELLOW}Name: {NAME}")
    print(f"Age: {AGE}")
    print(f"Email: {EMAIL}")
    print(f"Phone: {PHONE}")
    print(f"Address: {ADDRESS}{RESET}")
    print(style_line("#" * 100))
    print("\n" * 2)

NAME = input("Enter your name:")
AGE = input("Enter your age: ")
EMAIL = input("Enter your email: ")
PHONE = input("Enter your phone number: ")
ADDRESS = input("Enter your address: ")

A = display_registration()