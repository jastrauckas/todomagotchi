from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
import os, pymongo, re, json
from bson import json_util
from pymongo import MongoClient
from app import app


client = MongoClient("mongodb://admin:123@troup.mongohq.com:10032/todo")
if client:
	db = client.todo
	user_collection = db.user_collection
	task_collection = db.task_collection

def toJson(data):
#Convert Mongo object(s) to JSON
	return json.dumps(data, default=json_util.default)

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
				resp = make_response(render_template('index.html'))
				resp.set_cookie('username',username)
				return resp
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
                resp = make_response(render_template('index.html'))
                resp.set_cookie('username',username)
                return resp

            else:
                return render_template('signup.html', error = 'Username already exists.')

        else:
            return render_template('signup.html', error = 'Both fields must be complete.')
              
@app.route('/newtask',methods=['POST'])
def newtask():
	username = request.cookies.get('username')
	header = request.form['header']
	name = request.form['name']
	value = request.form['value']
	#created = request.form['created']
	if username and header and name and value:
		task = {	
                    'username' : username,
                    'header' : header,
                    'name' : name,
                    'value' : value,
                    'complete' : False#,
                    #'created' : created
                }
		task_collection.insert(task)
		return redirect(url_for('refresh'))

@app.route('/refresh')
def refresh():
	username = request.cookies.get('username')
	if username:
		cursor = task_collection.find({'username' : username })
		results = []
		for todo in cursor:
			results.append(todo)
		return render_template('index.html', tasks =results)
	else:
		return redirect(url_for('login'))

@app.route('/addtask', methods=['POST', 'GET'])
def addtask():
	if request.method=='GET':
		return render_template("addtask.html")
	elif request.method=='POST':
		username = request.cookies.get('username')
		header = request.form['header']
		name = request.form['name']
		value = request.form['value']
		#created = request.form['created']
		if username and header and name and value:
			task = {	
		                'username' : username,
		                'header' : header,
		                'name' : name,
		                'value' : value,
		                'complete' : False#,
		                #'created' : created
		            }
			task_collection.insert(task)
			return redirect(url_for('refresh'))

@app.route('/completed', methods=['POST'])
def index():
	id = request.form['id']
	if id:
		task_collection.update({_id : id}, {"$set":{'complete' : True}})
    return redirect(url_for('refresh'))
	
@app.route('/index')
def index():
    return redirect(url_for('refresh'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
#    app.debug = True
    app.run(host='0.0.0.0', port=port)
    #print "App running on port 5000."
