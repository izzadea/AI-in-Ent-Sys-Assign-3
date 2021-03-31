import sqlite3
conn = sqlite3.connect("database.db")

print("opened database successfully")

conn.execute("CREATE TABLE students(student_id INTEGER, first_name TEXT, last_name TEXT, DOB date, amount_due INTEGER)")

print("table created success")

conn.close()