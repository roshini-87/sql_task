from sqlalchemy import create_engine, Column, Integer, Numeric, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy engine
engine = create_engine('postgresql://postgres:1234@localhost/roshini')

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the Order model
class Order(Base):
    __tablename__ = 'orders'
    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer)
    salesman_id = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# First Query
query1 = (
    session.query(Order.salesman_id, func.max(Order.purch_amt).label('max_purchase'))
    .filter(Order.purch_amt <= 2000)
    .group_by(Order.salesman_id)
    .order_by(func.max(Order.purch_amt).desc())
    .limit(5)
)

# Execute the first query and print the result
result1 = query1.all()
print("Query 1 Result:", result1)

# Second Query
query2 = (
    session.query( Order.salesman_id, func.max(Order.purch_amt).label('max_purchase'))
    .filter(Order.purch_amt > 100)
    .group_by(Order.salesman_id)
    .order_by(func.max(Order.purch_amt).asc())
    .limit(5)
)

# Execute the second query and print the result
result2 = query2.all()
print("Query 2 Result:", result2)
