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
# -------------------------------------

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
    pyfiglet.print_figlet(text="About Us", colors="GREEN", width=100)
    print("\n" * 2)


def main():
    show_heading()
    print(style_line("#" * 100))
    print(f"{YELLOW}ARYA-MOTO - Automobile Service Management System{RESET}")
    print(style_line("#" * 100))
    print(f"""
{GREEN}ARYA-MOTO stands for:{RESET}
  {CYAN}A{RESET}utomated
  {CYAN}R{RESET}esource
  {CYAN}Y{RESET}ard for
  {CYAN}A{RESET}utomobiles – 
  {CYAN}M{RESET}anagement
  {CYAN}O{RESET}f
  {CYAN}T{RESET}erminal
  {CYAN}O{RESET}perations

{YELLOW}About the System:{RESET}
ARYA-MOTO is a comprehensive automobile service management system designed to streamline
the management of vehicle registrations, service records, and terminal operations. The system
provides an easy-to-use interface for customers to register their vehicles and track their
service history.

{YELLOW}Features:{RESET}
  • Customer Registration
  • Vehicle Management
  • Service Record Tracking
  • Comprehensive Service History
  • Efficient Resource Management

{YELLOW}Contact Us:{RESET}
For more information or support, please visit our website or contact our support team.

{CYAN}Thank you for using ARYA-MOTO!{RESET}
""")
    print(style_line("#" * 100))
    print("\n")
