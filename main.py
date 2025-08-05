from excel_importer import import_students_from_excel
from attendance_ui import AttendanceApp
from print_absentees import print_absentees
import tkinter as tk

# Step 1: Import students from Excel
import_students_from_excel("students.xlsx")

# Step 2: Launch Attendance UI
root = tk.Tk()
app = AttendanceApp(root)
root.mainloop()

# Step 3: Print Absentees after UI closes
print_absentees()
