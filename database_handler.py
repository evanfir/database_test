import mysql.connector
import sqlite3
from classes import employees, departments, dept_manager, dept_emp, titles, salaries, session_scope

# mydb = mysql.connector.connet(
#     host = "localhost",
#     user = "root",
#     passwd = "ascs3Vw.@#asdcE",
#     database = "employeeTestDB"
# )
mydb = sqlite3.connect("mydb.db")

my_cursor = mydb.cursor()

# new_employee = departments(
#         dept_no = "DD01",
#         dept_name = "department#1"
# )

# with session_scope() as session:
#     session.add(new_employee)
#     session.commit()
#     session.flush

# my_cursor.execute(open("load_departments.dump").read())
# mydb.commit()
# my_cursor = mydb.cursor()

my_cursor.execute(open("load_employees.dump").read())
mydb.commit()
my_cursor = mydb.cursor()

# my_cursor.execute(open("load_dept_manager.dump").read())
# mydb.commit()
# my_cursor = mydb.cursor()
