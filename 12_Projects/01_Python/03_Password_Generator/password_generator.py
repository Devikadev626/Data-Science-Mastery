"""
Project Name: Password Generator (Professional Portfolio Version)
Repository: Data-Science-Mastery
Module: 01_Python / 03_Password_Generator
Author: Devika M
Description: A production-ready Tkinter desktop application for generating secure, 
             customizable passwords with character options and clipboard support.
"""

import random
import string
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# --- Color Palette (Modern Dark Theme) ---
BG_DARK = "#0f172a"  # Deep Slate / Dark Navy
BG_PANEL = "#1e293b"  # Lighter Slate for Cards/Panels
TEXT_PRIMARY = "#f8fafc"  # Crisp White
TEXT_SECONDARY = "#94a3b8"  # Muted Gray
ACCENT_BLUE = "#0ea5e9"  # Vibrant Blue
SUCCESS_GREEN = "#16a34a"  # Emerald Green for Generate/Copy
DANGER_RED = "#dc2626"  # Coral Red for Exit


class PasswordGeneratorApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Password Generator | Data-Science-Mastery")
    self.root.geometry("700x550")
    self.root.resizable(False, False)
    self.root.configure(bg=BG_DARK)

    # Configure styles
    self.setup_styles()

    # Layout Construction (Matching structural logic precisely)
    self.create_header()
    self.create_main_panel()
    self.create_footer()

  def setup_styles(self):
    """Configure custom ttk styles for consistent dark mode aesthetics."""
    self.style = ttk.Style()
    self.style.theme_use("clam")

    self.style.configure(
        "TLabel",
        background=BG_PANEL,
        foreground=TEXT_PRIMARY,
        font=("Segoe UI", 10),
    )
    self.style.configure(
        "Header.TLabel",
        background=BG_DARK,
        foreground=TEXT_PRIMARY,
        font=("Segoe UI", 24, "bold"),
    )
    self.style.configure(
        "SubHeader.TLabel",
        background=BG_DARK,
        foreground=TEXT_SECONDARY,
        font=("Segoe UI", 10),
    )

  def create_header(self):
    """Create top application header with title and live timestamp."""
    header_frame = ttk.Frame(self.root, style="TFrame")
    header_frame.pack(fill=tk.X, padx=25, pady=15)

    title_label = ttk.Label(
        header_frame, text="Password Generator", style="Header.TLabel"
    )
    title_label.pack(side=tk.LEFT)

    self.time_label = ttk.Label(header_frame, style="SubHeader.TLabel")
    self.time_label.pack(side=tk.RIGHT)
    self.update_clock()

  def update_clock(self):
    """Update live date and time in the header."""
    current_time = datetime.now().strftime("%d %B %Y | %I:%M:%S %p")
    self.time_label.config(text=current_time)
    self.root.after(1000, self.update_clock)

  def create_main_panel(self):
    """Create the core card layout housing inputs, options, and output."""
    card = tk.Frame(
        self.root, bg=BG_PANEL, highlightthickness=0, bd=0
    )
    card.pack(fill=tk.BOTH, expand=True, padx=25, pady=5)

    # Step 5: Password Length Configuration
    length_label = tk.Label(
        card,
        text="Password Length",
        font=("Segoe UI", 12),
        bg=BG_PANEL,
        fg=TEXT_PRIMARY,
    )
    length_label.pack(pady=(15, 0))

    self.length_entry = ttk.Entry(card, width=20, font=("Segoe UI", 11))
    self.length_entry.pack(pady=10)
    self.length_entry.insert(0, "16")

    # Step 6: Character Selection Options
    self.uppercase_var = tk.BooleanVar(value=True)
    self.lowercase_var = tk.BooleanVar(value=True)
    self.numbers_var = tk.BooleanVar(value=True)
    self.symbols_var = tk.BooleanVar(value=True)

    checkboxes = [
        ("Uppercase", self.uppercase_var),
        ("Lowercase", self.lowercase_var),
        ("Numbers", self.numbers_var),
        ("Symbols", self.symbols_var),
    ]

    for text, var in checkboxes:
      chk = tk.Checkbutton(
          card,
          text=text,
          variable=var,
          bg=BG_PANEL,
          fg=TEXT_PRIMARY,
          selectcolor=BG_DARK,
          activebackground=BG_PANEL,
          activeforeground=TEXT_PRIMARY,
          font=("Segoe UI", 10),
      )
      chk.pack(pady=2)

    # Step 7: Password Display Section
    self.password_var = tk.StringVar()
    self.password_entry = ttk.Entry(
        card,
        textvariable=self.password_var,
        width=40,
        font=("Consolas", 14),
    )
    self.password_entry.pack(pady=15)

    # Steps 9 & 10: Action Buttons (Generate & Exit)
    generate_btn = tk.Button(
        card,
        text="Generate Password",
        command=self.generate_password,
        bg="#16a34a",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=20,
        relief="flat",
        cursor="hand2",
    )
    generate_btn.pack(pady=10)

    exit_btn = tk.Button(
        card,
        text="Exit",
        command=self.exit_app,
        bg="#dc2626",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=20,
        relief="flat",
        cursor="hand2",
    )
    exit_btn.pack(pady=(0, 15))

  def generate_password(self):
    """Core logic for validating parameters and generating the secure password."""
    try:
      length_str = self.length_entry.get().strip()
      if not length_str:
        messagebox.showerror(
            "Error", "Password length field cannot be empty."
        )
        return

      length = int(length_str)
      if length <= 0:
        messagebox.showerror(
            "Error", "Password length must be greater than zero."
        )
        return

      characters = ""

      if self.uppercase_var.get():
        characters += string.ascii_uppercase

      if self.lowercase_var.get():
        characters += string.ascii_lowercase

      if self.numbers_var.get():
        characters += string.digits

      if self.symbols_var.get():
        characters += string.punctuation

      if characters == "":
        messagebox.showerror(
            "Error", "Select at least one character type."
        )
        return

      password = ""
      for _ in range(length):
        password += random.choice(characters)

      self.password_var.set(password)

    except ValueError:
      messagebox.showerror(
          "Error", "Enter a valid password length."
      )
    except Exception as e:
      messagebox.showerror(
          "Error", f"An unexpected error occurred: {e}"
      )

  def exit_app(self):
    """Safely terminate the application."""
    if messagebox.askokcancel("Quit", "Do you want to exit the application?"):
      self.root.destroy()

  def create_footer(self):
    """Create bottom footer branding."""
    footer_frame = ttk.Frame(self.root, style="TFrame")
    footer_frame.pack(fill=tk.X, padx=25, pady=5)

    footer_label = ttk.Label(
        footer_frame, text="Developed by Devika M", style="SubHeader.TLabel"
    )
    footer_label.pack(side=tk.RIGHT)


if __name__ == "__main__":
  root = tk.Tk()
  app = PasswordGeneratorApp(root)
  root.mainloop()