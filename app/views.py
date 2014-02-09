from flask import Flask, render_template, request
import pymongo, re
from pymongo import MongoClient
import os

app = Flask(__name__)

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
		username = request.form['username']
		password = request.form['password']
        if len(username) > 0 and len(password) > 0:
            print user_collection.find_one({'username' : username })
            if user_collection.find_one({'username' : username }) == None:
                user = {	
                    username : username,
                    password : password
                }
                user_collection.insert(user)
                return render_template('user.html', username = username, password = password)

            else:
                return render_template('signup.html', error = 'Username already exists.')

        else:
            return render_template('signup.html', error = 'Both fields must be complete.')


def writesignupform(uname="",uerr="",perr="",merr="",email="",eerr=""):
	print "LEEEEEEEEEEEEEE"
	return render_template("signup.html", uname= uname,uerr= uerr,perr= perr,merr= merr,email= email,eerr= eerr)
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    print "App running on port 5000."
