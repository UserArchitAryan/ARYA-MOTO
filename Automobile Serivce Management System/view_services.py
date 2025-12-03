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


def main(customer_id=None):
    db_helper.ensure_tables()
    print("\n" * 2)
    pyfiglet.print_figlet(text = "Service View", colors = "YELLOW", width = 100)
    print("\n" * 2)

    print(style_line("#" * 100))
    print(f"{YELLOW}View My Service Records{RESET}")
    print(style_line("#" * 100))

    if customer_id is None:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        user = db_helper.get_user_by_name_password(name, password)
        if not user:
            print("Invalid credentials.")
            return
        customer_id = user.get('CUSTOMER_ID')

    services = db_helper.get_services_for_customer(customer_id)
    if not services:
        print("No past services found for this account.")
        return

    for s in services:
        svc_date = s.get('SERVICE_DATE')
        desc = s.get('SERVICE_DESC')
        vid = s.get('VEHICLE_ID')
        brand = s.get('BRAND') or ''
        model = s.get('MODEL') or ''
        print(style_line("-" * 80))
        print(f"Service ID: {s.get('SERVICE_ID')}  Date: {svc_date}")
        print(f"Vehicle: [{vid}] {brand} {model}")
        print(f"Details: {desc}")
    print(style_line("-" * 80))