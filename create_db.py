import sqlite3

with sqlite3.connect("student_grades.db") as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS grades")

    cursor.execute("""
    CREATE TABLE grades(
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
    """)

    data = [
        (1, "Aman", "Math", 95, "A"),
        (2, "Anshu", "Math", 78, "C"),
        (3, "Akshu", "History", 98, "B"),
        (4, "Rahul", "History", 92, "A"),
        (5, "Divyansh", "Science", 85, "B"),
        (6, "Nandini", "Math", 65, "D")
    ]

    cursor.executemany("INSERT INTO grades VALUES(?, ?, ?, ?, ?)", data)

print("Database created  successfully")
