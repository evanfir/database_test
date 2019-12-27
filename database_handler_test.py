# import mysql.connector
import sqlite3
from models import employees, departments, dept_manager, dept_emp, titles, salaries, session_scope, genderEnum
from sqlalchemy.sql import text
from sqlalchemy import engine
import datetime
import json
import jsonify 

# mydb = mysql.connector.connet(
#     host = "localhost",
#     user = "root",
#     passwd = "ascs3Vw.@#asdcE",
#     database = "employeeTestDB"
# )

mydb = sqlite3.connect("mydb.db")

my_cursor = mydb.cursor()

# def make_dict(columns, query = None):
#     for item in columns:
#         key = str(item).split('.')
#         # newColumns = key
#     return key
# with session_scope() as session:
# with engine.connect("mydb.db") as session:
# data = ({ "emp_no": 10002}, {"emp_no": 10005})
# statement = text("""SELECT * FROM employees WHERE (emp_no = :emp_no)""")
# for line in data:
#     print(line)
#     result = my_cursor.execute(statement, **line)
#     print(result)
# M = "male"
# with session_scope() as session:
#     # a = genderEnum("male").M
#     if True:#args['db'] == "employees":
#         data = ({"emp_no": 15, "birth_date": "1989-10-12",  
#             "first_name": "ev", "last_name": "fir", "gender": 'M', 
#             "hire_date": "2012-10-24"}, )
#         # data = ({"emp": 10002}, {"emp": 10005})
#         statement = text('''SELECT * FROM employees WHERE (employees.emp_no = (:emp_no))''')
#         # statement = text('''INSERT INTO 'employees'(emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (:emp_no, :birth_date, :first_name, :last_name, :gender, :hire_date) ''')
#         for line in data:
#             # print("\n\n",line,"\n\n")               
#             info = session.execute(statement, line)
#             # session.commit()
#             print(info.first())
# with session_scope() as session:
    # info = session.query(departments).filter(
    #                 departments.dept_no == "d001").first()
# info = my_cursor.execute('''SELECT FROM ''')
# print(info.dept_name)
    # info._criterion.right.effective_value
    # print()
    # info.column_descriptions
    # print(info.__table__.columns)
    # jsonreturn = jsonify(json_list = info)
    # print(jsonreturn)
# new_employee = departments(
#         dept_no = "DD01",
#         dept_name = "department#1"
# )

# with session_scope() as session:
#     session.add(new_employee)
#     session.commit()
#     session.flush
exe = open("load_departments.dump").read()
time1 = datetime.datetime.now()
my_cursor.execute(exe)
time2 = datetime.datetime.now()
print("\nload_departments: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()

exe = open("load_employees.dump").read()
time1 = datetime.datetime.now()
my_cursor.executescript(exe)
time2 = datetime.datetime.now()
print("\nload_employees: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()

exe = open("load_dept_manager.dump").read()
time1 = datetime.datetime.now()
my_cursor.executescript(exe)
time2 = datetime.datetime.now()
print("\nload_dept_manager: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()

exe = open("load_dept_emp.dump").read()
time1 = datetime.datetime.now()
my_cursor.executescript(exe)
time2 = datetime.datetime.now()
print("\nload_dept_emp: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()

exe = open("load_titles.dump").read()
time1 = datetime.datetime.now()
my_cursor.executescript(exe)
time2 = datetime.datetime.now()
print("\nload_titles: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()

exe = open("load_salaries1.dump").read()
time1 = datetime.datetime.now()
my_cursor.executescript(exe)
time2 = datetime.datetime.now()
print("\nload_salaries1: ",time2 - time1, "\n")
mydb.commit()
my_cursor = mydb.cursor()
