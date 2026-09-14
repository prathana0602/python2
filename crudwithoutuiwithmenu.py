import mysql.connector

# ==========================================
# 1. CONNECT TO MYSQL
# ==========================================
try:
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    print("MySQL Connected Successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    print(
        "Please ensure XAMPP/WAMP MySQL server is running and your credentials are correct."
    )
    exit()

# ==========================================
# 2. CREATE DATABASE
# ==========================================
cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
print("Database Checked/Created Successfully")

# ==========================================
# 3. USE DATABASE
# ==========================================
cursor.execute("USE studentdb")

# ==========================================
# 4. CREATE TABLE
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    mobile VARCHAR(15),
    email VARCHAR(100)
)
""")
print("Table Checked/Created Successfully")


# ==========================================
# INSERT STUDENT
# ==========================================
def insert_student():
    print("\n----- INSERT STUDENT -----")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    mobile = input("Enter Mobile: ")
    email = input("Enter Email: ")

    query = """
    INSERT INTO students (firstname, lastname, mobile, email)
    VALUES (%s, %s, %s, %s)
    """
    values = (firstname, lastname, mobile, email)

    cursor.execute(query, values)
    conn.commit()
    print("Student inserted successfully!")
    print("Student ID:", cursor.lastrowid)


# ==========================================
# DISPLAY ALL STUDENTS
# ==========================================
def display_students():
    print("\n----- ALL STUDENTS -----")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No student records found.")
    else:
        for row in rows:
            print(
                "ID:",
                row[0],
                "| First Name:",
                row[1],
                "| Last Name:",
                row[2],
                "| Mobile:",
                row[3],
                "| Email:",
                row[4],
            )


# ==========================================
# UPDATE STUDENT
# ==========================================
def update_student():
    print("\n----- UPDATE STUDENT -----")
    student_id = input("Enter Student ID: ")
    firstname = input("Enter New First Name: ")
    lastname = input("Enter New Last Name: ")
    mobile = input("Enter New Mobile: ")
    email = input("Enter New Email: ")

    query = """
    UPDATE students 
    SET firstname = %s, lastname = %s, mobile = %s, email = %s 
    WHERE id = %s
    """
    values = (firstname, lastname, mobile, email, student_id)

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student ID not found.")


# ==========================================
# DELETE STUDENT
# ==========================================
def delete_student():
    print("\n----- DELETE STUDENT -----")
    student_id = input("Enter Student ID: ")

    query = """
    DELETE FROM students 
    WHERE id = %s
    """
    values = (student_id,)

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")


# ==========================================
# MENU
# ==========================================
while True:
    print("\n================================")
    print("         STUDENT MANAGEMENT")
    print("================================")
    print("1. Insert Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    # INSERT
    if choice == "1":
        insert_student()
    # READ
    elif choice == "2":
        display_students()
    # UPDATE
    elif choice == "3":
        update_student()
    # DELETE
    elif choice == "4":
        delete_student()
    # EXIT
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice! Please try again.")

# ==========================================
# CLOSE CONNECTION
# ==========================================
cursor.close()
conn.close()
print("MySQL connection closed.")
