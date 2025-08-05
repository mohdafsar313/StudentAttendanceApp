import tkinter as tk
from tkinter import messagebox
from db import get_connection

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance")
        self.root.geometry("1500x800")
        self.students = []
        self.attendance_vars = {}

        self.load_students()
        self.build_ui()

    def load_students(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, student_name, roll_number FROM Students")
        self.students = [s for s in cursor.fetchall() if s[1] != "Student Name"]
        conn.close()

    def build_ui(self):
        tk.Label(self.root, text="📋 Student Attendance List", font=("Arial", 20, "bold")).pack(pady=20)

        canvas = tk.Canvas(self.root, bg="#ffffff")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.frame = tk.Frame(canvas, bg="#ffffff")
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create each row
        for index, (student_id, name, roll) in enumerate(self.students):
            row_frame = tk.Frame(self.frame, bg="#f5f5f5")
            row_frame.pack(fill="x", padx=30, pady=6)

            label = tk.Label(row_frame, text=f"{index + 1}. {name} (Roll: {roll})", font=("Arial", 12), bg="#f5f5f5")
            label.pack(side="left", padx=10)

            var = tk.StringVar(value="Present")
            self.attendance_vars[student_id] = var

            # Status label
            status_label = tk.Label(row_frame, text="Marked Present", font=("Arial", 10), bg="#f5f5f5", fg="green")
            status_label.pack(side="right", padx=10)

            def update_status_label(v=var, s_label=status_label):
                if v.get() == "Present":
                    s_label.config(text="Marked Present", fg="green")
                else:
                    s_label.config(text="Marked Absent", fg="red")

            present_btn = tk.Radiobutton(row_frame, text="Present", variable=var, value="Present",
                                         bg="lightgreen", indicatoron=0, width=10, font=("Arial", 10),
                                         command=update_status_label)

            absent_btn = tk.Radiobutton(row_frame, text="Absent", variable=var, value="Absent",
                                        bg="lightcoral", indicatoron=0, width=10, font=("Arial", 10),
                                        command=update_status_label)

            absent_btn.pack(side="right", padx=2)
            present_btn.pack(side="right", padx=2)

        # Submit button
        tk.Button(self.root, text="✅ Submit Attendance", command=self.submit_attendance,
                  font=("Arial", 13), bg="green", fg="white", padx=20, pady=5).pack(pady=30)

    def submit_attendance(self):
        conn = get_connection()
        cursor = conn.cursor()

        present_list = []
        absent_list = []

        for student in self.students:
            student_id, name, roll = student
            status = self.attendance_vars[student_id].get()

            if status == "Absent":
                cursor.execute("INSERT INTO Absence (student_id) VALUES (%s)", (student_id,))
                absent_list.append(f"{name} (Roll: {roll})")
            elif status == "Present":
                present_list.append(f"{name} (Roll: {roll})")

        conn.commit()
        conn.close()

        summary = "✅ Present Students:\n"
        summary += "\n".join(present_list) if present_list else "None"
        summary += "\n\n❌ Absent Students:\n"
        summary += "\n".join(absent_list) if absent_list else "None"

        messagebox.showinfo("Attendance Summary", summary)
