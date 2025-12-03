import pyfiglet
import db_helper


def main():
    db_helper.ensure_tables()
    pyfiglet.print_figlet(text = "Log Service Visit", colors = "YELLOW", width = 100)
    print("\n" * 2)

    name = input("Enter your name: ")
    password = input("Enter your password: ")
    user = db_helper.get_user_by_name_password(name, password)
    if not user:
        print("Invalid credentials. Cannot log service.")
        return

    customer_id = user.get('CUSTOMER_ID')
    vehicles = db_helper.get_vehicles_for_customer(customer_id)
    if not vehicles:
        print("No vehicles found for your account. Add one first.")
        return

    print("Your vehicles:")
    for v in vehicles:
        print(f" - [{v.get('VEHICLE_ID')}] {v.get('BRAND')} {v.get('MODEL')} ({v.get('YEAR')})")

    vid = input("Enter vehicle ID to log service for: ")
    try:
        vid = int(vid)
    except ValueError:
        print("Invalid vehicle ID")
        return

    desc = input("Service description: ")
    sid = db_helper.insert_service(customer_id, vid, desc)
    if sid:
        print(f"Service logged (ID: {sid})")
    else:
        print("Failed to log service.")