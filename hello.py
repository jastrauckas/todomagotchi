import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
from app import views


#SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","postgresql://qblbhphbktvdte:iYAAtsP_8ey0Y8o_rdCvNrS2b/dfephno04q3i00")

# configuration
DATABASE = 'ec2-50-16-201-126.compute-1.amazonaws.com'
DEBUG = True
SECRET_KEY = 'yowza'
USERNAME = 'qblbhphbktvdte'
PASSWORD = '-iYAAtsP_8ey0Y8o_rdCvNrS2b'

app.config.from_object(__name__)
db=SQLAlchemy(app)

#def connect_db():
#	return SQLAlchemy.connect(app.config['DataBase'])

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')    
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', var=name)
    
if __name__ == '__main__':
    app.run(debug=True)
