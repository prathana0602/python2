import tkinter as tk
from tkinter import messagebox, ttk

students_db = {}
current_id = 1
selected_id = None

def clear_fields():
    global selected_id
    selected_id = None
    firstname_entry.delete(0, tk.END)
    lastname_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def display_data():
    for item in tree.get_children():
        tree.delete(item)

    for student_id, info in students_db.items():
        tree.insert(
            "",
            tk.END,
            values=(
                student_id,
                info["firstname"],
                info["lastname"],
                info["mobile"],
                info["email"],
            ),
        )


def insert_data():
    global current_id
    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()
    mobile = mobile_entry.get().strip()
    email = email_entry.get().strip()

    if firstname == "" or lastname == "":
        messagebox.showerror(
            "Error", "Please enter First Name and Last Name"
        )
        return

    students_db[current_id] = {
        "firstname": firstname,
        "lastname": lastname,
        "mobile": mobile,
        "email": email,
    }
    current_id += 1

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()
    display_data()


def select_data(event):
    global selected_id
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        if values:
            selected_id = int(values[0])  # Explicitly target index 0

            # Clear entry fields manually without wiping selected_id
            firstname_entry.delete(0, tk.END)
            lastname_entry.replace(0, tk.END) if hasattr(
                lastname_entry, "replace"
            ) else lastname_entry.delete(0, tk.END)
            mobile_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)

            # Insert selected values into the fields
            firstname_entry.insert(0, values[1])
            lastname_entry.insert(0, values[2])
            mobile_entry.insert(0, values[3])
            email_entry.insert(0, values[4])


def update_data():
    global selected_id
    if selected_id is None:
        messagebox.showerror("Error", "Please select a student")
        return

    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()

    if firstname == "" or lastname == "":
        messagebox.showerror(
            "Error", "Please enter First Name and Last Name"
        )
        return

    students_db[selected_id] = {
        "firstname": firstname,
        "lastname": lastname,
        "mobile": mobile_entry.get().strip(),
        "email": email_entry.get().strip(),
    }

    messagebox.showinfo("Success", "Student Updated Successfully")
    clear_fields()
    display_data()


def delete_data():
    global selected_id
    if selected_id is None:
        messagebox.showerror("Error", "Please select a student")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete", "Do you want to delete this student?"
    )
    if confirm:
        del students_db[selected_id]
        messagebox.showinfo("Success", "Student Deleted Successfully")
        clear_fields()
        display_data()


root = tk.Tk()
root.title("In-Memory Student CRUD Application")
root.geometry("900x550")

# ---------------- FORM ----------------
tk.Label(root, text="First Name").place(x=50, y=50)
firstname_entry = tk.Entry(root, width=30)
firstname_entry.place(x=180, y=50)

tk.Label(root, text="Last Name").place(x=50, y=100)
lastname_entry = tk.Entry(root, width=30)
lastname_entry.place(x=180, y=100)

tk.Label(root, text="Mobile").place(x=50, y=150)
mobile_entry = tk.Entry(root, width=30)
mobile_entry.place(x=180, y=150)

tk.Label(root, text="Email").place(x=50, y=200)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=180, y=200)

tk.Button(root, text="Add", command=insert_data).place(x=180, y=250)
tk.Button(root, text="Update", command=update_data).place(x=250, y=250)
tk.Button(root, text="Delete", command=delete_data).place(x=330, y=250)
tk.Button(root, text="Clear", command=clear_fields).place(x=410, y=250)

columns = ("ID", "First Name", "Last Name", "Mobile", "Email")
tree = ttk.Treeview(root, columns=columns, show="headings")

for column in columns:
    tree.heading(column, text=column)

tree.column("ID", width=50)
tree.place(x=400, y=50, width=480, height=400)
tree.bind("<ButtonRelease-1>", select_data)

display_data()
root.mainloop()
