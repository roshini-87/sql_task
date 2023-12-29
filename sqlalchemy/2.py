from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy engine
engine = create_engine('postgresql://postgres:1234@localhost/roshini')

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the Salesman model
class Salesman(Base):
    __tablename__ = 'salesman'
    salesman_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city = Column(String(255))
    commission = Column(Float)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# First Query
query1 = (
    session.query(Salesman)
    .filter(Salesman.commission.between(0.10, 0.12))
)

# Execute the first query and print the result
result1 = query1.all()
for salesman in result1:
    print(salesman.salesman_id, salesman.name, salesman.city, salesman.commission)

# Second Query
query2 = (
    session.query(func.avg(Salesman.commission).label('average'))
    .filter(Salesman.commission.between(0.12, 0.14))
)

# Execute the second query and print the result
result2 = query2.scalar()
print("Average Commission:", result2)
