from db import get_connection
from datetime import datetime

def print_absentees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.student_name, s.roll_number, s.course_name, a.date_time
        FROM Absence a
        JOIN Students s ON a.student_id = s.id
        ORDER BY a.date_time DESC
    """)
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("\n📋 No absentees found.\n")
        return

    print("\n" + "=" * 80)
    print("📋  ABSENTEE REPORT".center(80))
    print(f"🕒  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(80))
    print("=" * 80)
    print(f"{'Sl.No':<6} {'Student Name':<25} {'Roll Number':<15} {'Course':<20} {'Date/Time':<30}")
    print("-" * 80)

    for i, rec in enumerate(records, start=1):
        name, roll, course, dt = rec
        print(f"{i:<6} {name:<25} {roll:<15} {course:<20} {dt.strftime('%Y-%m-%d %H:%M'):<30}")

    print("=" * 80 + "\n")
