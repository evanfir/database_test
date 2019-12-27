from flask import Flask#, render_template, request, redirect
from flask_restful import Api, Resource, reqparse
# import mysql.connector
import sqlite3
from models import employees, departments, dept_manager, dept_emp, titles, salaries, session_scope
# import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import text
from contextlib import contextmanager
# from bottle import get
import json as json
import decimal, datetime
from flask import json
from flask_oauthlib.provider import OAuth2Provider
from flask_bcrypt import Bcrypt


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

parser = reqparse.RequestParser()

# @app.route('/')
class DB(Resource):
    #adding all possible arguments to the parser
    #then we can access each with args['argument's name']
    #location: 'header', 'json'
    parser.add_argument('db') #table name
    parser.add_argument('emp', location='headers') #emp_no
    parser.add_argument('bd', location='headers') #birth_day
    parser.add_argument("f", location='headers') #first name
    parser.add_argument("l", location='headers') #last name
    parser.add_argument("g", location='headers') #gender
    parser.add_argument("hired", location='headers') #hire_date
    parser.add_argument("deptno", location='headers') #department_no
    parser.add_argument("deptna", location='headers') #dept_name
    parser.add_argument("from", location='headers') #from_date
    parser.add_argument("to", location='headers') #to_date
    parser.add_argument('title', location='headers') #title
    parser.add_argument('cmd', location='headers') #sql command
    parser.add_argument('text', type = list, location='json') #always use type=list for location='json'
    # with app.app_context():
        # rr = 
    # print(request.headers)
    
    #GET request
    #means select
    #HTTP request samples: 
    #   /db?db="dbname"&emp=1005&f=hihi
    #   /db?cmd=SELECT * FROM dbname WHERE key = value ....
    #only OR values
    #returns *
    def get(self):
        args = parser.parse_args()
        print("\n\nbodyvalue: ", ''.join(args['text']), "\n\n")
        infoList = list()
        statement = ""
        # print("\n\n",args,"\n\n")
        with session_scope() as session:
            #make a dict list of variables for sqlalchemy
            data = ({"db_name": args['db'], "emp_no": args['emp'], "birth_date": args['bd'],
                "first_name": args['f'], "last_name": args['l'], "gender": args['g'], 
                "hire_date": args['hired'], "dept_no": args['deptno'], "dept_name": args['deptna'],
                "from_date": args['from'], "to_date": args['to'], "title": args['title'], "cmd": args['cmd']}, )
            
            #if user have direct command:
            if args['cmd'] is not None:
                info = session.execute(args['cmd'])
                result = info.fetchone()
                while result is not None:
                    print(str(result))
                    infoList.append(str(result))
                    result = info.fetchone()
            #if user wants to get query by the db name
            else:
                if args['db'] == "employees":
                    statement = text('''SELECT * FROM employees WHERE \
                        (employees.emp_no = :emp_no \
                        OR employees.first_name = :first_name \
                        OR employees.last_name = :last_name)''')
                    
                elif args['db'] == "departments":
                    statement = text('''SELECT * FROM departments WHERE \
                        (departments.dept_no = :dept_no OR departments.dept_name = :dept_name)''')
                    
                elif args['db'] == "dept_emp":
                    statement = text('''SELECT * FROM dept_emp WHERE \
                        (dept_emp.emp_no = :emp_no \
                        OR dept_emp.dept_no = :dep_no \
                        OR dept_emp.from_date = :from_date\
                        OR dept_emp.to_date = :to_date)''')
                    
                elif args['db'] == "dept_manager":
                    statement = text('''SELECT * FROM dept_manager WHERE \
                        (dept_manager.emp_no = :emp_no \
                        OR dept_manager.dept_no = :dep_no \
                        OR dept_manager.from_date = :from_date\
                        OR dept_manager.to_date = :to_date)''')
                    
                elif args['db'] == "salaries":
                    statement = text('''SELECT * FROM salaries WHERE \
                        (salaries.emp_no = :emp_no \
                        OR salaries.from_date = :from_date\
                        OR salaries.to_date = :to_date)''')
                    
                elif args['db'] == "titles":
                    statement = text('''SELECT * FROM titles WHERE \
                        (titles.emp_no = :emp_no \
                        OR titles.title = :title \
                        OR titles.from_date = :from_date\
                        OR titles.to_date = :to_date)''')
                
                for line in data:
                    info = session.execute(statement, line)
                    result = info.fetchone()
                    while result is not None:
                        print(str(result))
                        infoList.append(str(result))
                        result = info.fetchone()

        return infoList, 202

    #POST http request
    #user can only input sql command
    def post(self):
        args = parser.parse_args()
        with session_scope() as session:
            if args['cmd'] is not None:
                session.execute(args['cmd'])
                session.commit()
        return "done", 202


api.add_resource(DB, "/db")  

def runFlask():
    app.run(debug=True)

if __name__ == "__main__":
    runFlask()