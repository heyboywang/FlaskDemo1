from orm import model
from sqlalchemy import create_engine

enegin = create_engine("mysql+mysqlconnector://root:intel123@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=enegin)()

def insertUser(username,password):
    result = session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
    print(result)

def checkUser(username,password):
    result = session.query(model.User).filter(model.User.username == username).filter(model.User.password==password).first().id
    if result:
        return str(result)
    else:
        return False

def queryUser(userid):
    result = session.query(model.User.id,model.User.username,model.User.password).filter(model.User.id == userid).first()
    if result:
        return result
    else:
        return False

def checkUserName(userid):
    result = session.query(model.User.username).filter(model.User.id == userid).first()
    if result:
        return result
    else:
        return False

def checkPro(id):
    result = session.query(model.Project.id,model.Project.proname)
    if result:
        return result
    else:
        return False

def checkOnePro(id):
    result = session.query(model.Project.id,model.Project.proname,model.Project.proremark).filter(model.Project.id == id).first()
    if result:
        return result
    else:
        return False

def addPro(proname,proremark):
    session.add(model.Project(proname=proname,proremark=proremark))
    session.commit()
    session.close()

def editPro(id,proname,proremark):
    session.query(model.Project).filter(model.Project.id == id).first().proname = proname
    session.query(model.Project).filter(model.Project.id == id).first().proremark = proremark
    session.commit()

def delPro(proid):
    session.query(model.Project).filter(model.Project.id == proid).delete()
    session.commit()