import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='afs313',
        database='student_attendance_app'
    )
