import tkinter as tk
from tkinter import messagebox
import math


class ScientificCalculator:

    def __init__(self, root):

        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x600")
        self.root.config(bg="lightgray")

        # Store expression
        self.expression = ""

        # Input field variable
        self.input_text = tk.StringVar()

        # =========================
        # Display Frame
        # =========================

        input_frame = tk.Frame(root, bg="lightgray")
        input_frame.pack(pady=10)

        self.input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=('Arial', 22),
            width=25,
            bd=10,
            relief=tk.RIDGE,
            justify='right'
        )

        self.input_field.pack(ipady=10)

        # =========================
        # Button Frame
        # =========================

        button_frame = tk.Frame(root)
        button_frame.pack()

        # Button Layout
        buttons = [

            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']

        ]

        # Create Number Buttons

        for row in range(4):

            for col in range(4):

                button = tk.Button(
                    button_frame,
                    text=buttons[row][col],
                    width=8,
                    height=3,
                    font=('Arial', 14),
                    bg="white",
                    command=lambda item=buttons[row][col]:
                    self.calculate() if item == '='
                    else self.button_click(item)
                )

                button.grid(row=row, column=col)

        # =========================
        # Scientific Buttons
        # =========================

        scientific_buttons = [

            ('sin', 4, 0),
            ('cos', 4, 1),
            ('tan', 4, 2),
            ('sqrt', 4, 3),
            ('log', 5, 0),
            ('C', 5, 1),
            ('DEL', 5, 2)

        ]

        for (text, row, col) in scientific_buttons:

            if text == 'C':
                command = self.clear

            elif text == 'DEL':
                command = self.delete

            else:
                command = lambda op=text: self.scientific_operation(op)

            button = tk.Button(
                button_frame,
                text=text,
                width=8,
                height=3,
                font=('Arial', 14),
                bg="lightblue",
                command=command
            )

            button.grid(row=row, column=col)

    # =========================
    # Button Click Function
    # =========================

    def button_click(self, item):

        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    # =========================
    # Clear Function
    # =========================

    def clear(self):

        self.expression = ""
        self.input_text.set("")

    # =========================
    # Delete Function
    # =========================

    def delete(self):

        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    # =========================
    # Calculate Function
    # =========================

    def calculate(self):

        try:

            result = str(eval(self.expression))

            # Display Result
            self.input_text.set(result)

            # Save History
            with open("history.txt", "a") as file:

                file.write(self.expression + " = " + result + "\n")

            self.expression = result

        except:

            messagebox.showerror(
                "Error",
                "Invalid Expression"
            )

            self.clear()

    # =========================
    # Scientific Functions
    # =========================

    def scientific_operation(self, operation):

        try:

            value = float(self.expression)

            if operation == "sin":
                result = math.sin(math.radians(value))

            elif operation == "cos":
                result = math.cos(math.radians(value))

            elif operation == "tan":
                result = math.tan(math.radians(value))

            elif operation == "sqrt":
                result = math.sqrt(value)

            elif operation == "log":
                result = math.log10(value)

            # Display Result
            self.input_text.set(result)

            # Update Expression
            self.expression = str(result)

        except:

            messagebox.showerror(
                "Error",
                "Invalid Scientific Calculation"
            )