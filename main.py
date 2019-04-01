from flask import Flask,render_template,request,redirect,make_response
import datetime
from orm import ormmanage as manage

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    userid = None
    userid = request.cookies.get("id")
    username = manage.checkUserName(userid)

    return render_template("index.html",username = username)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)

        try:
            result = manage.checkUser(username,password)
            print(username,password)
            res = make_response(redirect('/'))
            res.set_cookie("id",result,expires = datetime.datetime.now()+datetime.timedelta(days=7))
            return res
        except :
            print("111111111111111")
            return redirect("/login")


@app.route("/quit")
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie("id")
    return res

@app.route("/regist",methods=["POST","GET"])
def regist():
    if request.method == "GET":
        print("111")
        return  render_template("regist.html")
    elif request.method == "POST":
        print("222")
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)

        try:
            manage.insertUser(username,password)
            return redirect("/login")
        except:
            return redirect("/regist")

@app.route("/userinfo")
def userinfo():
    print("1111111111111111111111111111111111111111")
    userid = None
    userid = request.cookies.get("id")
    userinfo = manage.queryUser(userid)
    print(userinfo)

    return render_template("userinfo.html",userinfo = userinfo)



@app.route("/list")
def list():
    userid = None
    userid = request.cookies.get("id")
    username = manage.checkUserName(userid)

    result = manage.checkPro(id)
    print(type(result))
    return render_template("list.html",username = username,projectlist =result)

@app.route("/detail/<id>")
def detail(id):
    result = manage.checkOnePro(id)
    print(id)
    print(type(result))
    return render_template("detail.html",projectlist =result)

@app.route("/addpro",methods=["POST","GET"])
def addpro():
    if request.method == "GET":

        return  render_template("addpro.html")
    elif request.method == "POST":
        print("22222222222222222222222222222")
        userid = None
        userid = request.cookies.get("id")

        proname = request.form["proname"]
        proremark = request.form["proremark"]

        print(proname,proremark)

        try:
            manage.addPro(proname,proremark)
            return redirect("/list")
        except:
            print("1111111111111111111111111")
            return redirect("/addpro")

@app.route("/editpro/<id>",methods=["POST","GET"])
def editpro(id):
    print(id)
    if request.method == "GET":
        result = manage.checkOnePro(id)
        return  render_template("editpro.html",projectlist =result)
    elif request.method == "POST":
        print("22222222222222222222222222222")
        proname = request.form["proname"]
        proremark = request.form["proremark"]
        print(proname,proremark)

        try:
            print("3333333333333333333333333")
            manage.editPro(id,proname,proremark)
            print(id)
            return redirect("/detail/{}".format(id))
        except:
            print("444444444444444444444444444")
            return redirect("/list")

@app.route("/delpro/<id>",methods=["POST","GET"])
def delpro(id):
    try:
        manage.delPro(id)
        return redirect("/list")
    except:
        return redirect("/list")




if __name__ == '__main__':
    app.run()