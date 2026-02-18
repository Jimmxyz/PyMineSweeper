# SETTINGS
# Option to enable colored output. 
# If you don't want colors, set this to False.
color = True

import game

# Function to ask the user for a numeric value
# Loops until a valid integer between min and max is provided.
def chooseValue(msg, min, max):
    value = ""
    while type(value) != int:
        try:
            # Ask user for input
            value = int(input(f"Please choose the {msg} of the grid :"))
            
            # Check if value is within the allowed range
            if value < min or value > max:
                print(f"Must be greater than {min} and less than {max}")
                value = ""
        except:
            # Catch any invalid input (non-integer)
            print("Wrong input")
            value = ""
    return value


# Global variables for grid size
global height, width
height = chooseValue("height", 5, 50)
width = chooseValue("width", 5, 50)

# Percentage of mines (converted to a decimal)
rng = chooseValue("percentage of mine", 1, 100) / 100

# Generate the grid using the function from the game module
global grid, cursor
grid = game.gen_the_grid(height, width, rng)

# Cursor position starts at top-left
cursor = [0, 0]

# Function to print the grid
# If color is disabled, uses simple formatting
def printGrid(type):
    for i_index, i in enumerate(grid):
        for j_index, j in enumerate(i):
            if not color:
                # Format without colors
                if cursor[0] == i_index and cursor[1] == j_index:
                    format(j, True)
                else:
                    format(j, False)
            else:
                # Format with colors (complex for beginners)
                # Note: The color logic is optional and can be disabled
                colorize(j, i_index, j_index, type)
        print()

# --------------------------
# This function is COMPLEX for beginners
# It colors cells based on their value and game state.
# Optional: You can ignore color by setting color=False
def colorize(nb, x, y, type):
    clear = "\u001b[0m"
    blue = "\u001b[48;2;26;122;201m"
    mine_color = "\u001b[48;2;201;75;26m\u001b[1m"

    # Background for normal / win / lose states
    if (x + y) % 2 == 0 and (type == "standar" or type == "win"):
        green = "\u001b[48;2;88;168;88m"
        brown = "\u001b[48;2;231;164;133m"
    elif type == "standar" or type == "win":
        green = "\u001b[48;2;82;153;82m"
        brown = "\u001b[48;2;214;140;105m"
    elif (x + y) % 2 == 0 and type == "loose":
        green = "\u001b[48;2;38;51;38m"
        brown = "\u001b[48;2;61;42;33m"
    elif type == "loose":
        green = "\u001b[48;2;43;68;43m"
        brown = "\u001b[48;2;73;52;42m"

    flag_color = "\u001b[38;2;210;0;0m\u001b[1m"

    # Color for numbers (1–7)
    if nb == 1: nbColor = "\u001b[38;2;73;74;210m\u001b[1m"
    elif nb == 2: nbColor = "\u001b[38;2;64;120;67m\u001b[1m"
    elif nb == 3: nbColor = "\u001b[38;2;210;73;73m\u001b[1m"
    elif nb == 4: nbColor = "\u001b[38;2;140;57;161m\u001b[1m"
    elif nb == 5: nbColor = "\u001b[38;2;243;237;38m\u001b[1m"
    elif nb == 6: nbColor = "\u001b[38;2;106;232;226m\u001b[1m"
    elif nb == 7: nbColor = "\u001b[38;2;133;133;131m\u001b[1m"
    else: nbColor = "\u001b[38;2;0;0;0m\u001b[1m"

    # Coloring the current cursor cell
    if x == cursor[0] and y == cursor[1] and type != "win":
        if nb == 11 and type == "loose":
            print(f"{mine_color}[X]{clear}", end="")
        elif nb >= 12:
            print(f"{green}[{flag_color}F{clear}{green}]{clear}", end="")
        elif nb >= 10:
            print(f"{green}[ ]{clear}", end="")
        elif nb == 0:
            print(f"{brown}[ ]{clear}", end="")
        else:
            print(f"{brown}[{nbColor}{nb}{clear}{brown}]{clear}", end="")
        return

    # Coloring other cells based on game state
    if nb == 11 and type == "loose":
        print(f"{mine_color} X {clear}", end="")
    elif nb == 13 and type == "loose":
        print(f"{mine_color} F {clear}", end="")
    elif nb >= 12 and type != "win":
        print(f"{green}{flag_color} F {clear}", end="")
    elif nb >= 10:
        print(f"{green}   {clear}", end="")
    elif nb == 0  and type != "win":
        print(f"{brown}   {clear}", end="")
    elif type == "win":
        print(f"{blue}   {clear}", end="")
    else:
        print(f"{brown} {nbColor}{nb} {clear}", end="")

# Format for non-colored display
def format(nb, isCursor):
    if isCursor:
        if nb >= 12:
            print("[F]", end="")
        elif nb >= 10:
            print("[▓]", end="")
        elif nb == 0:
            print("[░]", end="")
        else:
            print(f"[{nb}]", end="")
        return
    if nb >= 12:
        print("▓F▓", end="")
    elif nb >= 10:
        print("▓▓▓", end="")
    elif nb == 0:
        print("░░░", end="")
    else:
        print(f"▒{nb}▒", end="")

# Initial print of the grid
printGrid("standar")

# --------------------------
# Main game loop
# --------------------------
def gameMain():
    import os
    import sys

    # Complex part for handling keyboard input across platforms
    # Beginners: This section is advanced and not required if you just want the game logic
    if os.name == "nt":
        import msvcrt

        def get_key():
            key = msvcrt.getch()
            if key == b'\xe0':
                key = msvcrt.getch()
                return {
                    b'H': "UP",
                    b'P': "DOWN",
                    b'K': "LEFT",
                    b'M': "RIGHT"
                }.get(key)
            elif key == b'\r':
                return "ENTER"
            elif key == b' ':
                return "SPACE"
            elif key == b"q" or key == b"Q":
                return "Q"
            return None
    else:
        import tty
        import termios

        # Complex input function for Unix systems
        # Beginners: Optional, this is advanced terminal handling
        def get_key():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = sys.stdin.read(1)
                if key == "\x1b":
                    key += sys.stdin.read(2)
                    return {
                        "\x1b[A": "UP",
                        "\x1b[B": "DOWN",
                        "\x1b[D": "LEFT",
                        "\x1b[C": "RIGHT"
                    }.get(key)
                elif key == "\r":
                    return "ENTER"
                elif key == " ":
                    return "SPACE"
                elif key == "q" or key == "Q":
                    return "Q"
                return None
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # Main loop of the game
    while True:
        global grid
        action = get_key()  # Wait for a key press from the user

        # Quit the game if user presses Q
        if action == "Q":
            break

        # ----------------------------
        # Cursor movement
        # ----------------------------
        if action == "UP" and cursor[0] > 0:
            cursor[0] -= 1  # Move cursor up

            
            # Clear the terminal and redraw the grid
            # os.system('cls') is for Windows
            # os.system('clear') is for Linux/Mac
            os.system('cls' if os.name == 'nt' else 'clear')
            printGrid("standar")

        if action == "DOWN" and cursor[0] < height - 1:
            cursor[0] += 1  # Move cursor down
            os.system('cls' if os.name == 'nt' else 'clear')
            printGrid("standar")

        if action == "LEFT" and cursor[1] > 0:
            cursor[1] -= 1  # Move cursor left
            os.system('cls' if os.name == 'nt' else 'clear')
            printGrid("standar")

        if action == "RIGHT" and cursor[1] < width - 1:
            cursor[1] += 1  # Move cursor right
            os.system('cls' if os.name == 'nt' else 'clear')
            printGrid("standar")

        # ----------------------------
        # Reveal a cell
        # ----------------------------
        if action == "ENTER":
            temp = game.mine(grid, cursor[0], cursor[1])

            if temp == "Mine":
                # Player hit a mine, game over
                os.system('cls' if os.name == 'nt' else 'clear')
                printGrid("loose")
                print("Game Over !")
                break

            if temp != "Flag":
                grid = temp  # Update the grid with revealed cells

                # Check if there are still unrevealed cells (10 or 12)
                isThere = False
                for i in grid:
                    for j in i:
                        if j == 10 or j == 12:
                            isThere = True
                            break
                    if isThere: break

                if not isThere:
                    # All cells revealed, player wins
                    os.system('cls' if os.name == 'nt' else 'clear')
                    printGrid("win")
                    print("Victory !")
                    break

                # Redraw grid after revealing
                os.system('cls' if os.name == 'nt' else 'clear')
                printGrid("standar")

        # ----------------------------
        # Place or remove a flag
        # ----------------------------
        if action == "SPACE":
            grid = game.flagIt(grid, cursor[0], cursor[1])
            os.system('cls' if os.name == 'nt' else 'clear')
            printGrid("standar")

# Start the game
gameMain()