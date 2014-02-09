from flask import Flask, render_template, request
import pymongo, re
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient("mongodb://admin:123@troup.mongohq.com:10032/todo")

db = client.todo
user_collection = db.user_collection

@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method=='GET':
		return render_template("login.html")
	elif request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		if len(username) > 0 and len(password) > 0:
		 	userinfo = user_collection.find_one({'username' : username })
		 	print userinfo
		 	if userinfo!=None and userinfo['password']==password:
				return render_template('user.html', username = username, password = password)
			else:
			    return render_template("login.html", errmsg="Login Error")
        else:
	        return render_template("login.html", errmsg="Login Error")
	        
@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method=='GET':
		return render_template("signup.html")
	elif request.method=='POST':
		username = request.form['username']
		password = request.form['password']
        if len(username) > 0 and len(password) > 0:
            if user_collection.find_one({'username' : username }) == None:
                user = {	
                    'username' : username,
                    'password' : password
                }
                user_collection.insert(user)
                return render_template('user.html', username = username, password = password)

            else:
                return render_template('signup.html', error = 'Username already exists.')

        else:
            return render_template('signup.html', error = 'Both fields must be complete.')
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
