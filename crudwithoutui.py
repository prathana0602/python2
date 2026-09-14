import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")
cursor = conn.cursor()
print("MySQL Connected Successfully")

cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
print("Database Created Successfully")

cursor.execute("USE studentdb")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    mobile VARCHAR(15),
    email VARCHAR(100)
)
""")
print("Table Created Successfully")

insert_query = """
INSERT INTO students 
(firstname, lastname, mobile, email) 
VALUES (%s, %s, %s, %s)
"""
insert_values = ("Yash", "Kotecha", "9876543210", "yash@gmail.com")
cursor.execute(insert_query, insert_values)
conn.commit()
print("Data Inserted Successfully")

inserted_id = cursor.lastrowid

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n----- STUDENT DATA -----")
for row in rows:
    print(row)

update_query = """ UPDATE students SET mobile = %s WHERE id = %s"""
update_values = ("9999999999", inserted_id)
cursor.execute(update_query, update_values)
conn.commit()
print("\nData Updated Successfully")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n----- UPDATED STUDENT DATA -----")
for row in rows:
    print(row)

delete_query = """DELETE FROM students WHERE id = %s """
delete_values = (inserted_id,)
cursor.execute(delete_query, delete_values)
conn.commit()
print("\nData Deleted Successfully")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n----- FINAL STUDENT DATA -----")
for row in rows:
    print(row)

cursor.close()
conn.close()
print("\nMySQL Connection Closed")
