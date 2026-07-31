# Student Grade Calculator

A production-quality desktop application built using Python and Tkinter designed for academic performance tracking, student evaluation, and automated record-keeping. Part of the **Data-Science-Mastery** repository.

---

## Features
- **Modern Dark Theme UI:** Designed with high-contrast slate panels, clean typography (`Segoe UI`), and intuitive layout geometry.
- **Robust Input Validation:** Prevents empty submissions, negative numbers, out-of-range marks (>100), and string anomalies in score fields.
- **Automated Analytics:** Computes Total Marks, Average Score, Percentage, Highest/Lowest scoring subjects, Letter Grades (`A+` to `F`), and Pass/Fail statuses.
- **Persistent Storage:** Automatically writes and appends student performance profiles into a local `students.csv` database.
- **Real-time Live Clock:** Integrated header timestamps displaying current system date and time.

---

## Technologies Used
- **Python 3.13+**
- **Tkinter & ttk** (Native GUI Framework)
- **CSV Module** (Data persistence)
- **OS Module** (File system verification)

---

## Project Structure
```text
02_Student_Grade_Calculator/
│
├── calculator.py
├── README.md
├── requirements.txt
├── students.csv
│
├── screenshots/
│      ├── app.png
│      └── result.png
│
└── assets/