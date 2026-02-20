# ==========================================================
# PyMineSweeper - Graphical Version using Tkinter
# ==========================================================
# This version uses Tkinter to create a graphical interface.
# Instead of playing in the terminal, we create real windows,
# buttons, popups, and interactive elements.
#
# Tkinter works with an "event-driven" system:
# The program waits for user actions (clicks, inputs, etc.)
# and reacts when they happen.
# ==========================================================

import game                          # Import the game logic (your other script)
import tkinter as tk                 # Tkinter library (renamed to tk for convenience)
from tkinter import messagebox as mb # Popup dialog windows (error / info)


# ==========================================================
# FIRST WINDOW (Settings Window)
# ==========================================================

# tk.Tk() creates the main window of the application
ask = tk.Tk()

# Window title (text shown at the top bar)
ask.title("PyMineSweeper UI")

# Minimum and maximum allowed size
ask.minsize(300, 250)
ask.maxsize(300, 250)

# Set exact size and position on screen
# Format: "WIDTHxHEIGHT+X+Y"
ask.geometry("300x250+50+50")


# ----------------------------------------------------------
# Tkinter Variables
# ----------------------------------------------------------
# StringVar is a special variable type used by Tkinter.
# It allows the Entry widget (input box) to stay linked
# with a Python variable.

width = tk.StringVar(value="20")
height = tk.StringVar(value="20")
prcent = tk.StringVar(value="25")


# ----------------------------------------------------------
# Labels (Text elements)
# ----------------------------------------------------------
# grid() places elements in a table system (rows/columns)

tk.Label(ask, text="Height").grid(row=0)
tk.Label(ask, text="Width").grid(row=3, column=1)
tk.Label(ask, text="").grid(row=4)
tk.Label(ask, text="% of Mine : ").grid(row=5)

# Decorative square (purely visual)
tk.Button(ask, text=" ", bg="#303030",
          borderwidth=0, height=7).grid(row=0, column=1,
                                        rowspan=2, sticky="nsew")


# ----------------------------------------------------------
# Entry fields (input boxes)
# ----------------------------------------------------------
# textvariable links the Entry to the StringVar defined above

tk.Entry(ask, textvariable=height).grid(row=1, column=0)
tk.Entry(ask, textvariable=width).grid(row=2, column=1)
tk.Entry(ask, textvariable=prcent).grid(row=5, column=1)


# ==========================================================
# Function called when pressing the "Start" button
# ==========================================================
def startGame():

    # ------------------------------------------
    # Convert user input into numbers
    # ------------------------------------------
    try:
        game_width = int(width.get())
        game_height = int(height.get())
        game_prct = int(prcent.get()) / 100
    except:
        # If conversion fails, show error popup
        mb.showerror(title="Impossible value",
                     message="Impossible to convert one of the values to a number")
        return

    # ------------------------------------------
    # Validate values
    # ------------------------------------------

    if game_width < 5:
        mb.showerror(title="Impossible value",
                     message="The minimum width is 5")
        return

    if game_width > 30:
        mb.showerror(title="Impossible value",
                     message="The maximum width is 30")
        return

    if game_height < 5:
        mb.showerror(title="Impossible value",
                     message="The minimum height is 5")
        return

    if game_height > 30:
        mb.showerror(title="Impossible value",
                     message="The maximum height is 30")
        return

    if game_prct > 0.8:
        mb.showerror(title="Impossible value",
                     message="The maximum mine percentage is 80%")
        return

    if game_prct < 0.05:
        mb.showerror(title="Impossible value",
                     message="The minimum mine percentage is 5%")
        return

    # ------------------------------------------
    # Initialize game grid
    # ------------------------------------------

    global grid, gamePlay
    grid = game.gen_the_grid(game_height, game_width, game_prct)
    gamePlay = True

    # Close settings window
    ask.destroy()


    # ======================================================
    # SECOND WINDOW (Game Window)
    # ======================================================

    root = tk.Tk()
    root.title("PyMineSweeper UI")
    root.minsize(200, 200)
    root.geometry("600x600+50+50")

    # Frame acts as a container for the grid of buttons
    frame = tk.Frame(root, padx=20, pady=20, bg="skyblue")
    frame.pack(expand=True, fill="both")


    # ======================================================
    # LEFT CLICK FUNCTION
    # ======================================================
    def left_click(row, col):
        global grid, gamePlay

        if not gamePlay:
            return

        temp = game.mine(grid, row, col)

        if temp == "Mine":
            printTheGrid("loose")
            gamePlay = False
            mb.showinfo(title="Game Over",
                        message="You have found a mine.")
            root.destroy()

        elif temp != "Flag":
            grid = temp

            # Check if there are still hidden cells
            isThere = False
            for i in grid:
                for j in i:
                    if j == 10 or j == 12:
                        isThere = True
                        break
                if isThere:
                    break

            # If no hidden cell → victory
            if not isThere:
                printTheGrid("win")
                gamePlay = False
                mb.showinfo(title="Victory",
                            message="You have won!")
                root.destroy()
                return

            printTheGrid("standar")


    # ======================================================
    # RIGHT CLICK FUNCTION (Place flag)
    # ======================================================
    def right_click(row, col):
        global grid, gamePlay

        if not gamePlay:
            return

        grid = game.flagIt(grid, row, col)
        printTheGrid("standar")


    # ======================================================
    # Create grid of buttons (visual board)
    # ======================================================

    global buttons
    buttons = {}

    for row in range(game_height):
        for col in range(game_width):

            # Alternate colors for chessboard effect
            if (row + col) % 2 == 0:
                bg_color = "#58a858"
            else:
                bg_color = "#529952"

            btn = tk.Button(frame,
                            text=" ",
                            bg=bg_color,
                            borderwidth=0,
                            font=("bold"),
                            width=1)

            btn.grid(row=row, column=col, sticky="nsew")

            # Store button reference in dictionary
            buttons[(row, col)] = btn

            # Bind mouse events
            btn.bind("<Button-1>",
                     lambda e, r=row, c=col: left_click(r, c))

            btn.bind("<Button-3>",
                     lambda e, r=row, c=col: right_click(r, c))


    # Allow rows/columns to expand if window resized
    for i in range(game_height):
        frame.grid_rowconfigure(i, weight=1)

    for j in range(game_width):
        frame.grid_columnconfigure(j, weight=1)


    # Start event loop
    root.mainloop()


# ==========================================================
# Function to update the visual grid
# ==========================================================
def printTheGrid(type):

    global grid

    for i_index, i in enumerate(grid):
        for j_index, j in enumerate(i):

            # Hidden cells
            if j == 10 or j == 11:
                if type == "loose" and j == 11:
                    buttons[(i_index, j_index)].config(bg="#fb542b", text="💣")
                    continue
                buttons[(i_index, j_index)].config(text=" ")

            # Flagged cells
            elif j == 12 or j == 13:
                if type == "win":
                    buttons[(i_index, j_index)].config(text=" ")
                    continue
                if type == "loose" and j == 13:
                    buttons[(i_index, j_index)].config(bg="#fb542b", text="🚩")
                    continue
                buttons[(i_index, j_index)].config(fg="#d20000",
                                                   text="🚩",
                                                   font=("bold"))

            # Revealed cells
            elif j < 10 and type == "win":
                buttons[(i_index, j_index)].config(bg="skyblue", text=" ")

            elif j < 10:

                if (i_index + j_index) % 2 == 0:
                    bg_color = "#e7a485"
                else:
                    bg_color = "#d68c69"

                if j == 0:
                    buttons[(i_index, j_index)].config(bg=bg_color, text="")
                elif j == 1:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#494ad2",
                                text="1", font=("bold"))
                elif j == 2:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#407843",
                                text="2", font=("bold"))
                elif j == 3:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#d24949",
                                text="3", font=("bold"))
                elif j == 4:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#8c39a1",
                                text="4", font=("bold"))
                elif j == 5:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#d5d038",
                                text="5", font=("bold"))
                elif j == 6:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#6ae8e2",
                                text="6", font=("bold"))
                elif j == 7:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#858583",
                                text="7", font=("bold"))
                else:
                    buttons[(i_index, j_index)]\
                        .config(bg=bg_color, fg="#020000",
                                text="8", font=("bold"))


# ==========================================================
# Start Button (in settings window)
# ==========================================================

tk.Button(ask,
          text='Start',
          command=startGame,
          width=10).grid(row=6, column=1,
                         sticky=tk.W, pady=4)

# Start first window event loop
ask.mainloop()