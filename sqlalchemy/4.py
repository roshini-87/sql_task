from sqlalchemy import create_engine, Column, Integer, Numeric, Date, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create an SQLAlchemy engine
engine = create_engine('postgresql://postgres:1234@localhost/roshini')

# Create an SQLAlchemy base class
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    cust_name = Column(VARCHAR(255))
    city = Column(VARCHAR(255))
    grade = Column(Integer)
    salesman_id = Column(Integer, ForeignKey('salesman.salesman_id'))
    salesman = relationship('Salesman', back_populates='customers')
    orders = relationship('Order', back_populates='customer')

# Define the Salesman model
class Salesman(Base):
    __tablename__ = 'salesman'
    salesman_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    city = Column(VARCHAR(255))
    commission = Column(FLOAT)
    customers = relationship('Customer', back_populates='salesman')

# Define the Order model
class Order(Base):
    __tablename__ = 'orders'
    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    customer = relationship('Customer', back_populates='orders')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# First Query
query1_result = (
    session.query(Customer.cust_name, Customer.city, Customer.grade, Salesman.name, Order.ord_no, Order.ord_date, Order.purch_amt)
    .outerjoin(Order, Customer.customer_id == Order.customer_id)
    .outerjoin(Salesman, Customer.salesman_id == Salesman.salesman_id)
    .filter(Order.purch_amt >= 2000, Customer.grade != None)
    .all()
)

# Print the result of the first query
print("\nquery 1 result:\n")
for row in query1_result:
    print(row)

# Second Query
query2_result = (
    session.query(Customer.cust_name, Customer.city, Order.ord_no, Order.ord_date, Order.purch_amt)
    .outerjoin(Order, Customer.customer_id == Order.customer_id)
    .filter(Customer.grade != None, Order.customer_id != None)
    .all()
)

# Print the result of the second query
print("\n query 2 result:\n")
for row in query2_result:
    print(row)
