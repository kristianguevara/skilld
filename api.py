import flask
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy_utils
from werkzeug.serving import run_simple

#engine = create_engine('mysql+gaerdbms:///mydb', connect_args={"instance":"firststeps"})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////skylld.db'
DEBUG=True
app.config.from_object(__name__)
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=False)
	password = db.Column(db.String(80), unique=False)
	email = db.Column(db.String(120), unique=False)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

class entries(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), unique=False)
	text = db.Column(db.String(120), unique=False)

	def __init__(self, title, text):
		self.title = title
		self.text = text

	def __repr__(self):
		return '<entries %r>' % self.title

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():
	if request.method == 'POST':
		message = ""
	return redirect(url_for('index', user_message = message))

if __name__ == '__main__':
	run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)