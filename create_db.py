import sqlite3

#connect to sqLite datbase
connection = sqlite3.connect("student_grades.db")
cursor = connection.cursor()


#create a table
cursor.execute("""
	CREATE TABLE IF NOT EXISTS grades(
	id INTEGER PRIMARY KEY,
	name TEXT,
	subject TEXT,
	score INTEGER,
	grade TEXT
)
""")

# inseert some dummy data
data =[ 
	(1, "Aman", "Math", 95, "A"),
	(2, "Anshu", "Math", 78, "C"),
	(3, "Akshu", "History", 98, "B"),
	(4, "Rahul", "History", 92, "A"),
	(5, "Divyansh", "Science", 85, "B"),
	(6, "Nandini", "Math", 65, "D")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES(?, ?, ?, ?, ?)", data)
connection.commit()
connection.close()

print("Database created and populated successfully")

