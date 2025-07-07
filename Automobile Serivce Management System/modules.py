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

def welcome_box():
    screen_width = 128  # Your program's fixed width

    box_width = 38  # Total width of the box (must match inner content length + padding + borders)
    left_padding = (screen_width - box_width) // 2
    
    #ASCII color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    # Color format for menu box
    border_color = CYAN
    text_color = YELLOW

    title_text = "MENU".center(box_width - 2)
    top = border_color + "╔" + "═" * (box_width - 2) + "╗" + RESET
    mid = border_color + "║" + text_color + title_text + border_color + "║" + RESET
    bot = border_color + "╚" + "═" * (box_width - 2) + "╝" + RESET

    print(" " * left_padding + top)
    print(" " * left_padding + mid)
    print(" " * left_padding + bot)

welcome_box()

def menu_box(text):
    screen_width = 128  # Your program's fixed width
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    for ch in text:
        if ch == ("[1]", "[2]", "[3]", "[4]", "[5]"):
            styled_text += "RED" + ch