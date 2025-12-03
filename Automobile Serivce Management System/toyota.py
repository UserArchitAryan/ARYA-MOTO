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


def main():
    print("\n" * 2)
    pyfiglet.print_figlet(text="TOYOTA", colors="YELLOW", width=100)
    print("\n" * 2)
    print(style_line("#" * 100))
    print(f"{YELLOW}Toyota Vehicle Service Module{RESET}")
    print(style_line("#" * 100))
    print("\nToyota service feature is under development.")
    print("Please try again later.")
    print("\n")
