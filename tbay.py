from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

user_bid_table = Table('user_bid_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('bid_id', Integer, ForeignKey('bid.id'))
)

bid_item_table = Table('bid_item_association', Base.metadata,
    Column('bid_id', Integer, ForeignKey('bid.id')),
    Column('item_id', Integer, ForeignKey('item.id'))
)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    seller_id = Column(Integer, ForeignKey(seller.id), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", backref="seller")
    bids = relationship("Bid", secondary="user_bid_association",
                            backref="userbid")

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    floating_price = Column(Integer, nullable=False)
    items = relationship("Items", secondary="bid_item_association",
                            backref="biditem")
    
Base.metadata.create_all(engine)


# beyonce = User()
# beyonce.username = "bknowles"
# beyonce.password = "crazyinlove"
# sylvester = User()
# sylvester.username = "sylvester"
# sylvester.password = "meow453"
# jane = User()
# jane.username = "jane"
# jane.password = "mejane879"
# Base.metadata.create_all(engine)

# session.add_all([beyonce, sylvester, jane])
# session.commit()

# prints user info
# for user in session.query(User).all():
#     print user.username
#     print user.password
#     print user.id

#prints item info    
for item in session.query(Item).all():
    print item.id
    print item.name
    print item.description
    
##change username of 31st user
# user = session.query(User).get(31)
# user.username = "solange"
# session.commit()

##change description of 5th item
# item = session.query(Item).get(5)
# item.description = "this is a test"
# session.commit()

# #delete 30th user
# user = session.query(User).get(30)
# session.delete(user)
# session.commit()

# #delete 6th item
# item = session.query(Item).get(6)
# session.delete(item)
# session.commit()