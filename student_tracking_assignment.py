import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class StudentTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Tracking")

        # Database setup
        self.conn = sqlite3.connect("student_data.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Create the main frame
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(main_frame, text="Student Tracking", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Student Information Form
        form_frame = tk.LabelFrame(main_frame, text="Student Information", padx=10, pady=10)
        form_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Labels and Entry Widgets
        labels = ["First Name:", "Last Name:", "Phone Number:", "Email:", "Current Course:"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="w", pady=2)
            entry = tk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, sticky="ew", pady=2)
            self.entries[label_text.replace(":", "").replace(" ", "_").lower()] = entry

        # Submit Button
        submit_button = tk.Button(form_frame, text="Submit", command=self.add_student)
        submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Student List Display
        list_frame = tk.LabelFrame(main_frame, text="Student List", padx=10, pady=10)
        list_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.tree = ttk.Treeview(list_frame, columns=("ID", "First Name", "Last Name", "Phone Number", "Email", "Current Course"), show="headings")
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.tree.heading("Phone Number", text="Phone Number", anchor=tk.CENTER)
        self.tree.heading("Email", text="Email", anchor=tk.CENTER)
        self.tree.heading("Current Course", text="Current Course", anchor=tk.CENTER)

        # Adjust column widths for better display
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("First Name", width=100, anchor=tk.W)
        self.tree.column("Last Name", width=100, anchor=tk.W)
        self.tree.column("Phone Number", width=100, anchor=tk.W)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Current Course", width=120, anchor=tk.W)
        
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Delete Button
        delete_button = tk.Button(list_frame, text="Delete Selected", command=self.delete_student)
        delete_button.pack(pady=5)

        self.load_students()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT,
                email TEXT,
                current_course TEXT
            )
        """)
        self.conn.commit()

    def add_student(self):
        first_name = self.entries["first_name"].get()
        last_name = self.entries["last_name"].get()
        phone_number = self.entries["phone_number"].get()
        email = self.entries["email"].get()
        current_course = self.entries["current_course"].get()

        if not all([first_name, last_name, phone_number, email, current_course]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        self.cursor.execute("INSERT INTO students (first_name, last_name, phone_number, email, current_course) VALUES (?, ?, ?, ?, ?)",
                            (first_name, last_name, phone_number, email, current_course))
        self.conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        self.clear_entries()
        self.load_students()

    def load_students(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.cursor.execute("SELECT * FROM students")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

    def delete_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete.")
            return

        student_id = self.tree.item(selected_item)["values"][0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student ID {student_id}?")
        if confirm:
            self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.load_students()

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentTracker(root)
    root.mainloop()

