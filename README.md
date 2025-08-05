# 🧑‍🎓 Student Attendance App (Python + MySQL)

A lightweight desktop application for tracking student attendance using Python and MySQL.

## 🚀 Features

- 📥 Import student data from Excel (`.xlsx`)
- ✅ Mark attendance via a GUI toggle switch
- 📊 Store attendance data in MySQL database
- 🖨️ Print or display absentee list

## 🛠️ Technologies Used

- Python 3.x
- `tkinter` for GUI
- `openpyxl` for reading Excel files
- `mysql-connector-python` for MySQL interaction

## 🗂️ Folder Structure

StudentAttendanceApp/
│
├── main.py # Entry point
├── import_excel.py # Logic to import Excel
├── attendance_gui.py # GUI to toggle attendance
├── db_config.py # DB connection config
├── print_absentees.py # Print absentees logic
├── students.xlsx # Sample Excel input
├── requirements.txt # Dependencies
└── README.md # This file


## 🧾 Sample Excel Format (`students.xlsx`)

| Student Name | Roll Number | Course Name |
|--------------|-------------|-------------|
| Afsar K A     | 101         | BSc CS      |
| John Doe      | 102         | BSc IT      |

## ⚙️ How to Run

1. 📦 **Install dependencies**

pip install -r requirements.txt
🛢️ Set up MySQL database

CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_number VARCHAR(50),
    course VARCHAR(100)
);

CREATE TABLE absentees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
🖥️ Run the app
python main.py
📝 TODO
Add date-based filtering

Export report to Excel

Add login/authorization

🤝 Contributing
Pull requests are welcome. Please make sure your changes are well-tested.

📬 Contact
Mohammed Afsar K A
GitHub • Email



### ✅ Add to Git and Push
git add README.md
git commit -m "Add README file"
git push
