# import os
# print("DB Path:", os.path.abspath("student_grades.db"))

import sqlite3

conn = sqlite3.connect("student_grades.db")
cur = conn.cursor()

cur.execute("SELECT * FROM grades")
rows = cur.fetchall()

print("All Data:", rows)

cur.execute("SELECT name FROM grades WHERE grade = 'D'")
print("D Grade:", cur.fetchall())

conn.close()
