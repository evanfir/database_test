from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
import mysql.connector
import enum

Base = declarative_base()
#engine = create_engine('mysql://root:ascs3Vw.@#asdcE@localhost/testDatabase', 
    # echo=True)
engine = create_engine('sqlite:///mydb.db', echo = True) 

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session(bind=engine)
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

class genderEnum(enum.Enum):
    M = "male"
    F = "female"

class employees(Base):
    __tablename__ = "employees"

    emp_no = Column(Integer, primary_key=True, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(genderEnum), nullable=False)
    hire_date = Column(DateTime, nullable=False)

class departments(Base):
    __tablename__ = "departments"

    dept_no = Column(String(4), primary_key = True, nullable=False)
    dept_name = Column(String(40), nullable=False)

class dept_manager(Base):
    __tablename__ = "dept_manager"

    emp_no = Column(Integer, ForeignKey("employees.emp_no"), primary_key = True, nullable=False)
    dept_no = Column(String(4), ForeignKey("departments.dept_no"), primary_key = True, nullable=False)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=False)

class dept_emp(Base):
    __tablename__ = "dept_emp"

    emp_no = Column(Integer, ForeignKey("employees.emp_no"), primary_key = True, nullable=False)
    dept_no = Column(String(4), ForeignKey("departments.dept_no"), primary_key = True, nullable=False)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=False)

class titles(Base):
    __tablename__ = "titles"

    emp_no = Column(Integer, ForeignKey("employees.emp_no"), primary_key = True, nullable=False)
    title = Column(String(50), nullable=False)
    from_date = Column(DateTime, primary_key = True, nullable=False)
    to_date = Column(DateTime)

class salaries(Base):
    __tablename__ = "salaries"
    
    emp_no = Column(Integer, ForeignKey("employees.emp_no"), primary_key = True, nullable=False)
    salary = Column(Integer, nullable=False)
    from_date = Column(DateTime, primary_key = True, nullable=False)
    to_date = Column(DateTime, nullable=False)


Base.metadata.create_all(engine)