"""
    orm

"""

class Book():
    def __init__(self,_id,_name,_price):
        self.id = _id
        self.name = _name
        self.price = _price

    def __str__(self):
        return "id: %s name: %s price: %s" % (self.id,self.name,self.price)

from  sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:intel123@localhost/flaskdb",
                                    encoding='utf8', echo=True)

from  sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import Column,Integer,String,ForeignKey
class User(Base):
    __tablename__ = "user"
    id = Column(Integer ,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    proname = Column(String(20),nullable=False)
    proremark = Column(String(100))

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
