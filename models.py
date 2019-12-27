from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
# import mysql.connector
import enum

Base = declarative_base()
#engine = create_engine('mysql://root:ascs3Vw.@#asdcE@localhost/testDatabase', 
    # echo=True)
engine = create_engine('sqlite:///mydb.db', echo = False) 

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
    __table_args__ = (UniqueConstraint('emp_no'), )

    def __init__(self, __tablename__, emp_no, birth_date, first_name, last_name, gender, hire_date):
        self.dbname = __tablename__
        self.emp_no = emp_no
        self.birth_date = birth_date
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.hire_date = hire_date

    def __str__(self):
        
        return ("<Table: '%s', emp_no: '%d', birth_date: '%s', first: '%s', last: '%s', gender: '%s', hire: '%s'>" % (self.dbname, self.emp_no, str(self.birth_date), self.first_name, self.last_name, str(self.gender), str(self.hire_date)))


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
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    username = Column(String(30), nullable = False)

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key = True)
    client_id = Column(Integer)
    
class Grant(Base):
    __tablename__ = "grants"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User')
    client_id = Column(String(40), ForeignKey('client.client_id'), nullable=False)
    client = relationship('Client')
    code = Column(String(255), index=True, nullable=False)
    redirect_uri = Column(String(255))
    epires = Column(DateTime)
    _scopes = Column(Text)

    def delete(self):
        Base.delete(self)
        Base.commit()
        return self

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []

class Token(Base):
    __tablename__ = "token"

    id =  Column( Integer, primary_key=True)
    client_id =  Column(
         String(40),  ForeignKey('client.client_id'),
        nullable=False,
    )
    client =  relationship('Client')

    user_id =  Column(
         Integer,  ForeignKey('user.id')
    )
    user =  relationship('User')

    # currently only bearer is supported
    token_type =  Column( String(40))

    access_token =  Column( String(255), unique=True)
    refresh_token =  Column( String(255), unique=True)
    expires =  Column( DateTime)
    _scopes =  Column( Text)

    def delete(self):
        Base.delete(self)
        Base.commit()
        return self

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []

Base.metadata.create_all(engine)