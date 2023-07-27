from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declared_attr
from db import Base as Basex

class Base(Basex):
   __abstract__ = True
   
   @declared_attr
   def __tablename__(self):
       return self.__name__.lower()
   
class product(Base):
    id = Column(Integer, primary_key=True, index=True)
    Product_Name = Column(String(20))
    Product_Brand = Column(String(20))
    Product_Price = Column(Float)
    Product_description = Column(String(50))
    