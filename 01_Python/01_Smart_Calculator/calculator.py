import tkinter as tk


class SmartCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("380x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E1E")

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=8,
            relief="ridge",
            bg="white"
        )
        self.display.pack(fill="both", padx=15, pady=20, ipady=12)

        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack()

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#1E1E1E")
            row_frame.pack(expand=True, fill="both")

            for button in row:
                if button == "=":
                    command = self.calculate
                elif button == "C":
                    command = self.clear
                else:
                    command = lambda value=button: self.click(value)

                tk.Button(
                    row_frame,
                    text=button,
                    font=("Arial", 18, "bold"),
                    width=5,
                    height=2,
                    bg="#2D89EF" if button == "=" else "#3C3F41",
                    fg="white",
                    activebackground="#0078D7",
                    command=command
                ).pack(side="left", padx=5, pady=5)

    def click(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    SmartCalculator(root)
    root.mainloop()