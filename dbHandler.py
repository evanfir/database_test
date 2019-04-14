import mysql.connector
import sqlite3
from classes import employees, departments, dept_manager, dept_emp, titles, salaries, session_scope
import datetime


class dbHandler:
    def __init__(self, dbname):
        self._dbname = dbname
        self._conn = sqlite3.connect(dbname)
        self._cursorObj = self._conn.cursor()

        