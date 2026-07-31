import tkinter as tk
from tkinter import messagebox
import random

# ------------------------------
# Generate Random Number
# ------------------------------
secret_number = random.randint(1, 100)

attempts = 0


# ------------------------------
# Check Guess
# ------------------------------
def check_guess():
    global attempts

    guess = entry_guess.get()

    if guess == "":
        messagebox.showwarning("Warning", "Please enter a number.")
        return

    try:
        guess = int(guess)

    except ValueError:
        messagebox.showerror("Error", "Enter only numbers.")
        return

    attempts += 1

    attempts_label.config(text=f"Attempts : {attempts}")

    if guess < secret_number:

        result_label.config(
            text="Too Low!",
            fg="blue"
        )

    elif guess > secret_number:

        result_label.config(
            text="Too High!",
            fg="red"
        )

    else:

        result_label.config(
            text="Congratulations! Correct Guess",
            fg="green"
        )

        messagebox.showinfo(
            "Winner",
            f"You guessed the number in {attempts} attempts."
        )


# ------------------------------
# New Game
# ------------------------------
def new_game():

    global secret_number
    global attempts

    secret_number = random.randint(1, 100)

    attempts = 0

    entry_guess.delete(0, tk.END)

    attempts_label.config(
        text="Attempts : 0"
    )

    result_label.config(
        text="New Game Started!",
        fg="black"
    )


# ------------------------------
# Main Window
# ------------------------------

root = tk.Tk()

root.title("Number Guessing Game")

root.geometry("450x420")

root.resizable(False, False)

# ------------------------------
# Heading
# ------------------------------

title = tk.Label(
    root,
    text="NUMBER GUESSING GAME",
    font=("Arial", 18, "bold"),
    fg="darkblue"
)

title.pack(pady=20)

# ------------------------------

instruction = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12)
)

instruction.pack()

# ------------------------------

entry_guess = tk.Entry(
    root,
    width=20,
    font=("Arial", 16),
    justify="center"
)

entry_guess.pack(pady=20)

# ------------------------------

guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12),
    width=18,
    bg="#4CAF50",
    fg="white",
    command=check_guess
)

guess_button.pack()

# ------------------------------

attempts_label = tk.Label(
    root,
    text="Attempts : 0",
    font=("Arial", 12)
)

attempts_label.pack(pady=20)

# ------------------------------

result_label = tk.Label(
    root,
    text="Start Guessing...",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=10)

# ------------------------------

new_game_button = tk.Button(
    root,
    text="New Game",
    width=15,
    font=("Arial", 12),
    bg="orange",
    command=new_game
)

new_game_button.pack(pady=10)

# ------------------------------

exit_button = tk.Button(
    root,
    text="Exit",
    width=15,
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=root.destroy
)

exit_button.pack()

# ------------------------------

root.mainloop()