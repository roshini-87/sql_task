from sqlalchemy import create_engine, Column, Integer, String, distinct, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy engine
engine = create_engine('postgresql://postgres:1234@localhost/roshini')

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the EmployeeHistory model
class EmployeeHistory(Base):
    __tablename__ = 'employee_history'
    employee_id = Column(Integer, primary_key=True)
    job_id = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Write the SQLAlchemy ORM query
query = (
    session.query(EmployeeHistory.employee_id)
    .group_by(EmployeeHistory.employee_id)
    .having(func.count(distinct(EmployeeHistory.job_id)) >= 2)
)

# Execute the query and print the result
result = query.all()
print("Result:", result)
