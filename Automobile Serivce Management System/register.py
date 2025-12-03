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

db_helper.ensure_tables()

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
    pyfiglet.print_figlet(text="Registration", colors="YELLOW", width=100)
    print("\n" * 2)


def display_registration(NAME, AGE, EMAIL, PHONE, ADDRESS):
    print("\n" * 2)
    print("Welcome and Thank you for registering with ARYA-MOTO!")
    print(style_line("#" * 100))
    print(f"{YELLOW}Name: {NAME}")
    print(f"Age: {AGE}")
    print(f"Email: {EMAIL}")
    print(f"Phone: {PHONE}")
    print(f"Address: {ADDRESS}{RESET}")
    print(style_line("#" * 100))
    print("\n")


def save_to_database(NAME, AGE, EMAIL, PHONE, ADDRESS, PASSWORD):
    customer_id = db_helper.insert_user(NAME, AGE, EMAIL, PHONE, ADDRESS, PASSWORD)
    if customer_id:
        print(f"{GREEN}✅ Registration data saved successfully! Your ID: {customer_id}{RESET}")
    else:
        print(f"{RED}❌ Failed to save registration data.{RESET}")
    return customer_id


def menu_box(text):
    screen_width = 128
    styled_text = ""
    for ch in text:
        if ch in "12345":
            styled_text += RED + ch + RESET
        else:
            styled_text += ch
    return styled_text


def main():
    show_heading()

    NAME = input("Enter your name: ")
    AGE = input("Enter your age: ")
    EMAIL = input("Enter your email: ")
    PHONE = input("Enter your phone number: ")
    ADDRESS = input("Enter your address: ")
    PASSWORD = input("Choose a password (store securely): ")

    display_registration(NAME, AGE, EMAIL, PHONE, ADDRESS)
    cust_id = save_to_database(NAME, AGE, EMAIL, PHONE, ADDRESS, PASSWORD)

    # Ask to add a vehicle now
    if cust_id:
        add = input("Would you like to add a vehicle now? (y/n): ").strip().lower()
        if add == 'y':
            brand = input("Vehicle brand: ")
            model = input("Vehicle model: ")
            year = input("Vehicle year: ")
            vid = db_helper.insert_vehicle(cust_id, brand, model, year)
            if vid:
                print(f"{GREEN}Vehicle added (ID: {vid}){RESET}")
            else:
                print(f"{RED}Failed to add vehicle.{RESET}")

    print(menu_box("[1] Add a vehicle"))
    print(menu_box("[2] Log Service Visit"))
    print(menu_box("[3] View All Services Records"))
    print(menu_box("[4] Exit"))

    opt = input("Enter your choice: ")
    if opt == "1":
        print("You have chosen to Add a vehicle.")
        import brands
        brands.main()
    elif opt == "2":
        print("You have chosen to Log a service visit.")
        import add_vehicle
        add_vehicle.main()
    elif opt == "3":
        print("You have chosen to view all service records.")
        import view_services
        view_services.main()
    elif opt == "4":
        print("\nExiting the program. Thank you for using ARYA-MOTO!\n")
        pyfiglet.print_figlet(text="THANK YOU", colors="BLUE", width=100)
    else:
        print("Invalid option. Please try again.")
        main()


if __name__ == "__main__":
    main()
