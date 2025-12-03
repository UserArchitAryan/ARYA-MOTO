import pyfiglet
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
    pyfiglet.print_figlet(text="Login", colors="CYAN", width=100)
    print("\n" * 2)


def menu_box(text):
    styled_text = ""
    for ch in text:
        if ch in "12345":
            styled_text += RED + ch + RESET
        else:
            styled_text += ch
    return styled_text


import db_helper


def main():
    db_helper.ensure_tables()
    show_heading()
    print(style_line("#" * 100))
    print(f"{YELLOW}Welcome to ARYA-MOTO Login Portal{RESET}")
    print(style_line("#" * 100))

    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()

    user = db_helper.get_user_by_name_password(name, password)
    if not user:
        print(f"{RED}Login failed: invalid name or password.{RESET}")
        return

    print(f"{GREEN}Login successful. Welcome, {user.get('CUSTOMER_NAME')}!{RESET}")
    print(style_line("-" * 100))
    print(f"{YELLOW}Name: {user.get('CUSTOMER_NAME')}")
    print(f"Email: {user.get('EMAIL')}")
    print(f"Phone: {user.get('PHONE')}")
    print(style_line("-" * 100))

    # Show vehicles
    vehicles = db_helper.get_vehicles_for_customer(user.get('CUSTOMER_ID'))
    if vehicles:
        print(f"{CYAN}Your vehicles:{RESET}")
        for v in vehicles:
            print(f" - [{v.get('VEHICLE_ID')}] {v.get('BRAND')} {v.get('MODEL')} ({v.get('YEAR')})")
    else:
        print(f"{YELLOW}No vehicles found for your account.{RESET}")

    print("\n")
    print(menu_box("[1] View My Service History"))
    print(menu_box("[2] Add a Vehicle"))
    print(menu_box("[3] Logout"))
    opt = input("Enter your choice: ").strip()
    if opt == "1":
        import view_services
        view_services.main(user.get('CUSTOMER_ID'))
    elif opt == "2":
        # simple add vehicle flow
        brand = input("Vehicle brand: ")
        model = input("Vehicle model: ")
        year = input("Vehicle year: ")
        vid = db_helper.insert_vehicle(user.get('CUSTOMER_ID'), brand, model, year)
        if vid:
            print(f"{GREEN}Vehicle added (ID: {vid}){RESET}")
        else:
            print(f"{RED}Failed to add vehicle.{RESET}")
    else:
        print("Logged out. Goodbye.")
