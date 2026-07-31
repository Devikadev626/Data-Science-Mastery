"""
Project Name: Student Grade Calculator (Professional Portfolio Version)
Repository: Data-Science-Mastery
Module: 01_Python / 02_Student_Grade_Calculator
Author: Devika M
Description: A production-ready Tkinter desktop application for calculating 
             academic performance, validating scores, and managing student CSV records.
"""

import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# --- Color Palette (Modern Dark Theme) ---
BG_DARK = "#0f172a"  # Deep Slate / Dark Navy
BG_PANEL = "#1e293b"  # Lighter Slate for Cards/Panels
TEXT_PRIMARY = "#f8fafc"  # Crisp White
TEXT_SECONDARY = "#94a3b8"  # Muted Gray
ACCENT_BLUE = "#0ea5e9"  # Vibrant Blue
ACCENT_HOVER = "#0284c7"  # Darker Blue for hover
SUCCESS_GREEN = "#10b981"  # Emerald Green for Pass/Save
DANGER_RED = "#ef4444"  # Coral Red for Fail/Errors
WARNING_YELLOW = "#f59e0b"  # Amber for Reset


class StudentGradeCalculatorApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Student Grade Calculator | Data-Science-Mastery")
    self.root.geometry("900x700")
    self.root.resizable(False, False)
    self.root.configure(bg=BG_DARK)

    # Configure global styles for ttk widgets
    self.setup_styles()

    # Main UI Layout Container
    self.create_header()
    self.create_main_container()
    self.create_footer()

  def setup_styles(self):
    """Configure custom ttk styles to match the dark theme."""
    self.style = ttk.Style()
    self.style.theme_use("clam")

    # Label styles
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
        font=("Segoe UI", 16, "bold"),
    )
    self.style.configure(
        "SubHeader.TLabel",
        background=BG_DARK,
        foreground=TEXT_SECONDARY,
        font=("Segoe UI", 10),
    )
    self.style.configure(
        "Section.TLabel",
        background=BG_PANEL,
        foreground=ACCENT_BLUE,
        font=("Segoe UI", 11, "bold"),
    )

    # Frame styles
    self.style.configure("TFrame", background=BG_DARK)
    self.style.configure("Card.TFrame", background=BG_PANEL)

  def create_header(self):
    """Create top application header with title and live timestamp."""
    header_frame = ttk.Frame(self.root, style="TFrame")
    header_frame.pack(fill=tk.X, padx=20, pady=15)

    title_label = ttk.Label(
        header_frame, text="STUDENT GRADE CALCULATOR", style="Header.TLabel"
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

  def create_main_container(self):
    """Create the split-pane layout for inputs and results."""
    main_container = ttk.Frame(self.root, style="TFrame")
    main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

    # Left Panel: Inputs (Student Info & Marks)
    left_panel = tk.Frame(
        main_container, bg=BG_PANEL, bd=0, highlightthickness=0
    )
    left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

    self.create_student_info_section(left_panel)
    self.create_marks_section(left_panel)
    self.create_action_buttons(left_panel)

    # Right Panel: Results & Analytics
    right_panel = tk.Frame(
        main_container, bg=BG_PANEL, bd=0, highlightthickness=0
    )
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

    self.create_result_section(right_panel)

  def create_student_info_section(self, parent):
    """Create student metadata input fields."""
    ttk.Label(parent, text="Student Information", style="Section.TLabel").pack(
        anchor="w", padx=15, pady=(15, 10)
    )

    fields_frame = tk.Frame(parent, bg=BG_PANEL)
    fields_frame.pack(fill=tk.X, padx=15, pady=5)

    self.entries = {}
    labels = [
        ("Student Name:", "name"),
        ("Student ID:", "id"),
        ("Department:", "dept"),
        ("Semester:", "sem"),
    ]

    for idx, (text, key) in enumerate(labels):
      row = idx // 2
      col = (idx % 2) * 2

      lbl = tk.Label(
          fields_frame,
          text=text,
          bg=BG_PANEL,
          fg=TEXT_SECONDARY,
          font=("Segoe UI", 9),
      )
      lbl.grid(row=row * 2, column=col, sticky="w", pady=(5, 2))

      entry = tk.Entry(
          fields_frame,
          bg=BG_DARK,
          fg=TEXT_PRIMARY,
          insertbackground=TEXT_PRIMARY,
          relief="flat",
          font=("Segoe UI", 10),
      )
      entry.grid(
          row=row * 2 + 1,
          column=col,
          sticky="ew",
          padx=(0, 10),
          ipady=4,
          pady=(0, 8),
      )
      self.entries[key] = entry

    fields_frame.columnconfigure(0, weight=1)
    fields_frame.columnconfigure(2, weight=1)

  def create_marks_section(self, parent):
    """Create input fields for the 5 core subjects."""
    ttk.Label(
        parent, text="Subject Marks (0 - 100)", style="Section.TLabel"
    ).pack(anchor="w", padx=15, pady=(15, 10))

    marks_frame = tk.Frame(parent, bg=BG_PANEL)
    marks_frame.pack(fill=tk.X, padx=15, pady=5)

    self.mark_entries = {}
    subjects = [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Excel",
    ]

    for idx, subj in enumerate(subjects):
      lbl = tk.Label(
          marks_frame,
          text=subj,
          bg=BG_PANEL,
          fg=TEXT_SECONDARY,
          font=("Segoe UI", 9),
      )
      lbl.grid(row=idx, column=0, sticky="w", pady=4)

      entry = tk.Entry(
          marks_frame,
          bg=BG_DARK,
          fg=TEXT_PRIMARY,
          insertbackground=TEXT_PRIMARY,
          relief="flat",
          font=("Segoe UI", 10),
          width=15,
      )
      entry.grid(row=idx, column=1, sticky="e", pady=4, ipady=3)
      self.mark_entries[subj] = entry

    marks_frame.columnconfigure(0, weight=1)

  def create_action_buttons(self, parent):
    """Create interactive control buttons with custom styling."""
    btn_frame = tk.Frame(parent, bg=BG_PANEL)
    btn_frame.pack(fill=tk.X, padx=15, pady=20)

    # Action Buttons Setup
    buttons = [
        ("Calculate", ACCENT_BLUE, self.calculate_result),
        ("Reset", WARNING_YELLOW, self.reset_fields),
        ("Save Record", SUCCESS_GREEN, self.save_record),
        ("Exit", DANGER_RED, self.exit_app),
    ]

    for text, color, cmd in buttons:
      btn = tk.Button(
          btn_frame,
          text=text,
          bg=color,
          fg="#ffffff",
          activebackground=TEXT_SECONDARY,
          activeforeground="#ffffff",
          relief="flat",
          font=("Segoe UI", 9, "bold"),
          cursor="hand2",
          command=cmd,
      )
      btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=3, ipady=6)

  def create_result_section(self, parent):
    """Create the professional Result Panel displaying computed metrics."""
    ttk.Label(parent, text="Performance Dashboard", style="Section.TLabel").pack(
        anchor="w", padx=15, pady=(15, 10)
    )

    self.result_display_frame = tk.Frame(parent, bg=BG_DARK)
    self.result_display_frame.pack(
        fill=tk.BOTH, expand=True, padx=15, pady=(0, 15)
    )

    self.result_labels = {}
    metrics = [
        ("Student Name", "N/A"),
        ("Student ID", "N/A"),
        ("Department", "N/A"),
        ("Semester", "N/A"),
        ("Total Marks", "0 / 500"),
        ("Average Score", "0.00"),
        ("Percentage", "0.00%"),
        ("Highest Mark", "N/A"),
        ("Lowest Mark", "N/A"),
        ("Overall Grade", "N/A"),
        ("Final Status", "N/A"),
    ]

    for idx, (label_text, default_val) in enumerate(metrics):
      lbl_title = tk.Label(
          self.result_display_frame,
          text=label_text,
          bg=BG_DARK,
          fg=TEXT_SECONDARY,
          font=("Segoe UI", 9),
      )
      lbl_title.grid(row=idx, column=0, sticky="w", padx=10, pady=3)

      lbl_val = tk.Label(
          self.result_display_frame,
          text=default_val,
          bg=BG_DARK,
          fg=TEXT_PRIMARY,
          font=("Segoe UI", 9, "bold"),
      )
      lbl_val.grid(row=idx, column=1, sticky="e", padx=10, pady=3)
      self.result_labels[label_text] = lbl_val

    self.result_display_frame.columnconfigure(0, weight=1)
    self.result_display_frame.columnconfigure(1, weight=1)

  def validate_marks(self):
    """Validate student metadata and ensure marks are numerical integers between 0 and 100."""
    try:
      # Check metadata fields
      for key, entry in self.entries.items():
        if not entry.get().strip():
          messagebox.showerror(
              "Validation Error",
              f"The '{key.capitalize()}' field cannot be empty.",
          )
          return None

      marks_dict = {}
      for subj, entry in self.mark_entries.items():
        val_str = entry.get().strip()
        if not val_str:
          messagebox.showerror(
              "Validation Error", f"Mark for '{subj}' cannot be empty."
          )
          return None

        mark = float(val_str)
        if not (0 <= mark <= 100):
          messagebox.showerror(
              "Validation Error",
              f"Mark for '{subj}' must be between 0 and 100.",
          )
          return None
        marks_dict[subj] = mark

      return marks_dict

    except ValueError:
      messagebox.showerror(
          "Validation Error",
          "Invalid input detected. Please enter numeric values for marks.",
      )
      return None

  def calculate_grade(self, percentage):
    """Assign letter grade based on overall percentage criteria."""
    if percentage >= 90:
      return "A+"
    elif percentage >= 80:
      return "A"
    elif percentage >= 70:
      return "B"
    elif percentage >= 60:
      return "C"
    elif percentage >= 50:
      return "D"
    else:
      return "F"

  def calculate_result(self):
    """Compute performance metrics and update the UI result panel."""
    marks_data = self.validate_marks()
    if not marks_data:
      return

    try:
      # Computations
      total_marks = sum(marks_data.values())
      avg_score = total_marks / len(marks_data)
      percentage = (total_marks / 500.0) * 100

      highest_subj = max(marks_data, key=marks_data.get)
      lowest_subj = min(marks_data, key=marks_data.get)

      # Pass Criteria: Every subject >= 50
      all_passed = all(m >= 50 for m in marks_data.values())
      status = "PASS" if all_passed else "FAIL"
      grade = self.calculate_grade(percentage)

      # Update Result Panel UI
      self.result_labels["Student Name"].config(
          text=self.entries["name"].get().strip()
      )
      self.result_labels["Student ID"].config(
          text=self.entries["id"].get().strip()
      )
      self.result_labels["Department"].config(
          text=self.entries["dept"].get().strip()
      )
      self.result_labels["Semester"].config(
          text=self.entries["sem"].get().strip()
      )
      self.result_labels["Total Marks"].config(
          text=f"{total_marks:.1f} / 500"
      )
      self.result_labels["Average Score"].config(text=f"{avg_score:.2f}")
      self.result_labels["Percentage"].config(text=f"{percentage:.2f}%")
      self.result_labels["Highest Mark"].config(
          text=f"{highest_subj} ({marks_data[highest_subj]})"
      )
      self.result_labels["Lowest Mark"].config(
          text=f"{lowest_subj} ({marks_data[lowest_subj]})"
      )
      self.result_labels["Overall Grade"].config(text=grade)

      status_color = SUCCESS_GREEN if status == "PASS" else DANGER_RED
      self.result_labels["Final Status"].config(
          text=status, fg=status_color
      )

      messagebox.showinfo(
          "Success", "Calculations completed successfully!"
      )

    except Exception as e:
      messagebox.showerror(
          "Error", f"An unexpected error occurred during calculation: {e}"
      )

  def save_record(self):
    """Save student info, marks, and calculated outcomes to students.csv."""
    # Ensure calculation has been performed or valid data is present
    marks_data = self.validate_marks()
    if not marks_data:
      return

    try:
      total_marks = sum(marks_data.values())
      avg_score = total_marks / len(marks_data)
      percentage = (total_marks / 500.0) * 100
      grade = self.calculate_grade(percentage)
      all_passed = all(m >= 50 for m in marks_data.values())
      status = "PASS" if all_passed else "FAIL"

      file_exists = os.path.isfile("students.csv")

      headers = [
          "Student Name",
          "Student ID",
          "Department",
          "Semester",
          "Python",
          "SQL",
          "Statistics",
          "Machine Learning",
          "Excel",
          "Total",
          "Average",
          "Percentage",
          "Grade",
          "Result",
      ]

      row_data = [
          self.entries["name"].get().strip(),
          self.entries["id"].get().strip(),
          self.entries["dept"].get().strip(),
          self.entries["sem"].get().strip(),
          marks_data["Python"],
          marks_data["SQL"],
          marks_data["Statistics"],
          marks_data["Machine Learning"],
          marks_data["Excel"],
          total_marks,
          f"{avg_score:.2f}",
          f"{percentage:.2f}%",
          grade,
          status,
      ]

      with open("students.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
          writer.writerow(headers)
        writer.writerow(row_data)

      messagebox.showinfo(
          "Database Updated",
          "Record successfully saved to 'students.csv'!",
      )

    except Exception as e:
      messagebox.showerror(
          "File Error", f"Failed to save record to CSV: {e}"
      )

  def reset_fields(self):
    """Clear all input entries and reset result displays."""
    for entry in self.entries.values():
      entry.delete(0, tk.END)

    for entry in self.mark_entries.values():
      entry.delete(0, tk.END)

    for key, lbl in self.result_labels.items():
      if key == "Final Status":
        lbl.config(text="N/A", fg=TEXT_PRIMARY)
      else:
        lbl.config(text="N/A" if "Name" in key or "ID" in key or "Department" in key or "Semester" in key or "Mark" in key else "0 / 500" if "Total" in key else "0.00")

    messagebox.showinfo("Reset", "All fields have been cleared.")

  def exit_app(self):
    """Safely close the application window."""
    if messagebox.askokcancel("Quit", "Do you want to exit the application?"):
      self.root.destroy()

  def create_footer(self):
    """Create bottom footer branding."""
    footer_frame = ttk.Frame(self.root, style="TFrame")
    footer_frame.pack(fill=tk.X, padx=20, pady=10)

    footer_label = ttk.Label(
        footer_frame, text="Developed by Devika M", style="SubHeader.TLabel"
    )
    footer_label.pack(side=tk.RIGHT)


if __name__ == "__main__":
  root = tk.Tk()
  app = StudentGradeCalculatorApp(root)
  root.mainloop()