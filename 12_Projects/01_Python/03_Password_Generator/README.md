# Password Generator (Professional Portfolio Version)

A secure, highly customizable desktop application built with Python and Tkinter for generating robust random passwords. Part of the **Data-Science-Mastery** repository.

---

## Project Overview

The **Password Generator** application provides an intuitive graphical user interface (GUI) designed to help users generate strong, cryptographically secure passwords. Users can specify custom password lengths and toggle character sets including uppercase letters, lowercase letters, numbers, and punctuation symbols.

---

## Features

- **Customizable Length:** Define precise password character lengths (supporting standard and high-security requirements).
- **Granular Character Toggles:** Select or deselect Uppercase (`A-Z`), Lowercase (`a-z`), Numbers (`0-9`), and Symbols (`!@#$%^&*`).
- **Secure Random Generation:** Utilizes Python's `random` module to pull from standardized character pools.
- **Modern Dark Theme UI:** Designed with an aesthetic dark slate palette, high-contrast elements, and clean `Segoe UI` typography.
- **Robust Error Handling:** Validates empty entries, invalid non-numeric lengths, and unselected character types via popup alert dialogues.
- **Real-time Live Clock:** Integrated header timestamps displaying the current system date and time.

---

## Technologies Used

- **Python 3.13+**
- **Tkinter & ttk** (Native GUI framework)
- **Random Module** (Pseudo-random selection)
- **String Module** (ASCII character sets)
- **Datetime Module** (Live timestamp tracking)

*No external third-party packages are required.*

---

## Project Structure

```text
03_Password_Generator/
│
├── password_generator.py
├── README.md
├── requirements.txt
│
├── screenshots/
│      ├── app.png
│      └── result.png
│
└── assets/