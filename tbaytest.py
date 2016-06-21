from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship

# class Manufacturer(Base):
#     __tablename__ = 'manufacturer'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     guitars = relationship("Guitar", backref="manufacturer")

# class Guitar(Base):
#     __tablename__ = 'guitar'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)

#     manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'),
#                              nullable=False)

# fender = Manufacturer(name="Fender")
# strat = Guitar(name="Stratocaster", manufacturer=fender)
# tele = Guitar(name="Telecaster")
# fender.guitars.append(tele)
# Base.metadata.create_all(engine)

# session.add_all([fender, strat, tele])
# session.commit()

# for guitar in fender.guitars:
#     print(guitar.name)
#     print(guitar.id)
# # print(tele.manufacturer.name)

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport
Base.metadata.create_all(engine)

session.add(beyonce)
session.commit()

print(beyonce.passport.issue_date)
print(passport.owner.name)
print(passport.owner.id)