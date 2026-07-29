import tkinter as tk
from tkinter import messagebox
import math


class SmartCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("420x650")
        self.root.configure(bg="#1E1E2E")
        self.root.resizable(False, False)

        self.expression = ""

        # ---------------- Display ---------------- #

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 28),
            bg="#2A2A40",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white"
        )

        self.display.pack(fill="both", padx=15, pady=20, ipady=18)

        # ---------------- Buttons ---------------- #

        button_frame = tk.Frame(root, bg="#1E1E2E")
        button_frame.pack()

        buttons = [
            ["AC", "⌫", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["%", "0", ".", "="],
            ["x²"]
        ]

        for row in buttons:

            frame = tk.Frame(button_frame, bg="#1E1E2E")
            frame.pack()

            for button in row:

                if button == "=":
                    bg = "#4CAF50"

                elif button in ["/", "*", "-", "+"]:
                    bg = "#FF9800"

                elif button in ["AC", "⌫"]:
                    bg = "#F44336"

                elif button in ["√", "x²", "%"]:
                    bg = "#3F51B5"

                else:
                    bg = "#2F3542"

                tk.Button(
                    frame,
                    text=button,
                    font=("Segoe UI", 18, "bold"),
                    width=5,
                    height=2,
                    bg=bg,
                    fg="white",
                    activebackground="#616161",
                    relief="flat",
                    command=lambda value=button: self.button_click(value)
                ).pack(side="left", padx=5, pady=5)

    # ---------------- Button Events ---------------- #

    def button_click(self, value):

        if value == "=":
            self.calculate()

        elif value == "AC":
            self.clear()

        elif value == "⌫":
            self.backspace()

        elif value == "√":
            self.square_root()

        elif value == "x²":
            self.square()

        elif value == "%":
            self.percentage()

        else:
            self.expression += value
            self.update_display()

    # ---------------- Display ---------------- #

    def update_display(self):

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    # ---------------- Calculator Functions ---------------- #

    def calculate(self):

        try:
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()

        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def clear(self):

        self.expression = ""
        self.update_display()

    def backspace(self):

        self.expression = self.expression[:-1]
        self.update_display()

    def square(self):

        try:
            result = float(self.expression)
            self.expression = str(result ** 2)
            self.update_display()

        except:
            messagebox.showerror("Error", "Enter a valid number")

    def square_root(self):

        try:
            result = float(self.expression)

            if result < 0:
                messagebox.showerror(
                    "Error",
                    "Cannot calculate square root of a negative number."
                )
                return

            self.expression = str(round(math.sqrt(result), 8))
            self.update_display()

        except:
            messagebox.showerror("Error", "Enter a valid number")

    def percentage(self):

        try:
            result = float(self.expression)
            self.expression = str(result / 100)
            self.update_display()

        except:
            messagebox.showerror("Error", "Enter a valid number")


# ---------------- Main ---------------- #

if __name__ == "__main__":

    root = tk.Tk()

    SmartCalculator(root)

    root.mainloop()