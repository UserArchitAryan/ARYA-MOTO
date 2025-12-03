import pyfiglet
import db_helper

# ----------- COLOR CODES -------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GREY = "\033[90m"
RESET = "\033[0m"
# ------------------------------------

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


def show_heading():
    print("\n" * 2)
    pyfiglet.print_figlet(text="Add Vehicle", colors="MAGENTA", width=100)
    print("\n" * 2)


def menu_box(text):
    styled_text = ""
    for ch in text:
        if ch in "12345":
            styled_text += RED + ch + RESET
        else:
            styled_text += ch
    return styled_text


def main():
    show_heading()
    db_helper.ensure_tables()
    print(style_line("#" * 100))
    print(f"{YELLOW}Add Vehicle Module{RESET}")
    print(style_line("#" * 100))

    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()
    user = db_helper.get_user_by_name_password(name, password)
    if not user:
        print(f"{RED}Authentication failed. Cannot add vehicle.{RESET}")
        return

    brand = input("Vehicle brand: ").strip()
    model = input("Vehicle model: ").strip()
    year = input("Vehicle year: ").strip()
    vid = db_helper.insert_vehicle(user.get('CUSTOMER_ID'), brand, model, year)
    if vid:
        print(f"{GREEN}Vehicle added successfully (ID: {vid}){RESET}")
    else:
        print(f"{RED}Failed to add vehicle.{RESET}")

    print("\n")
