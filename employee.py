import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employee"
)
import os

cursor = db.cursor()

FILE_PATH = "/media/sahathevan/local disk D/projects/ems project/employees.txt"


def write_table_header():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        with open(FILE_PATH, "w") as file:
            # file.write("-----------------------------------------------\n")
            file.write(f"{'ID':<6} {'Name':<12} {'Department':<15} {'Salary'}\n")
            # file.write("-----------------------------------------------\n")


def save_employee_to_file(emp_id, name, dept, salary):
    write_table_header()
    with open(FILE_PATH, "a") as file:
        file.write(f"{emp_id:<6} {name:<12} {dept:<15} {salary}\n")



def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    sql = "INSERT INTO employees VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (emp_id, name, dept, salary))
    db.commit()

    save_employee_to_file(emp_id, name, dept, salary)
    print("Employee added (DB + File)")



def search_employee(emp_id):
    sql = "SELECT * FROM employees WHERE emp_id=%s"
    cursor.execute(sql, (emp_id,))
    result = cursor.fetchone()

    if result:
        print("\nEmployee Found")
        print("ID:", result[0])
        print("Name:", result[1])
        print("Department:", result[2])
        print("Salary:", result[3])
    else:
        print("Employee not found")


def update_employee():
    emp_id = int(input("Enter ID to update: "))
    salary = int(input("Enter new salary: "))

    sql = "UPDATE employees SET salary=%s WHERE emp_id=%s"
    cursor.execute(sql, (salary, emp_id))
    db.commit()

    print("Employee updated")


def delete_employee():
    emp_id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    db.commit()
    print("Employee deleted")


def view_employees_from_file():
    try:
        with open(FILE_PATH, "r") as file:
            print("\nEmployee Records (Table Format)")
            print("\n-----------------------------------------------")
            print(f"{'ID':<6} {'Name':<12} {'Department':<15} {'Salary'}")
            print("-----------------------------------------------")
            print(file.read())
    except FileNotFoundError:
        print("No employee file found")



while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.View File 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        emp_id = int(input("Enter ID to search: "))
        search_employee(emp_id)

    elif choice == 3:
        update_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        view_employees_from_file()

    else:
        print("Exit")
        break



            

