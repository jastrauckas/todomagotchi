from flask import render_template, request
from app import app
import pymongo, re
from pymongo import MongoClient

client = MongoClient("mongodb://admin:123@troup.mongohq.com:10032/todo")
db = client.todo
user_collection = db.user_collection


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
Pass_RE = re.compile(r"^.{3,20}")
email_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def validu(u):
    return USER_RE.match(u)
def validp(p):
    return Pass_RE.match(p)
def verifp(p,v):
    return p==v
def valide(e):
    if not e:
        return True
    return email_RE.match(e)

@app.route('/')
@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method=='GET':
		return render_template("signup.html")
	elif request.method=='POST':
		have_error=False
		username = request.form['username']
		password = request.form['password']
		verify = request.form['verify']
		email = request.form['email']
		uerr=""
        perr=""
        merr=""
        eerr=""
        
        if not validu(username):
            have_error=True
            uerr="That's not a valid username"
        if not validp(password):
            have_error=True
            perr="That wasn't a valid password."
        if not verifp(password,verify):
            have_error=True
            merr="Your passwords didn't match."
        if not valide(email):
            have_error=True
            eerr = "That's not a valid email."
        if have_error:
        	writesignupform(username,uerr,perr,merr,email,eerr)
        else:
        	if user_collection.find_one({'username' : username }) != None:
        		uerr="username already exists"
        		writesignupform(username,uerr,perr,merr,email,eerr)
			user = {	
			username : username,
			password : password
			}
			user_collection.insert(user)
			return "You ROCK"
def writesignupform(uname="",uerr="",perr="",merr="",email="",eerr=""):
	print "LEEEEEEEEEEEEEE"
	return render_template("signup.html", uname= uname,uerr= uerr,perr= perr,merr= merr,email= email,eerr= eerr)
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
