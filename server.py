import flask
from flask import Flask, render_template, request, redirect, url_for, \
	abort, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy_utils

#engine = create_engine('mysql+gaerdbms:///mydb', connect_args={"instance":"firststeps"})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skylld.db'
DEBUG=True
app.config.from_object(__name__)
app.secret_key= 'wmjei9jrceimw9rjcwxfijopw'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=False)
	password = db.Column(db.String(80), unique=False)
	firstname = db.Column(db.String(80), unique=False)
	lastname = db.Column(db.String(80), unique=False)
	country = db.Column(db.String(80), unique=False)
	city = db.Column(db.String(80), unique=False)
	middlename = db.Column(db.String(80), unique=False)
	typeid = db.Column(db.String(80), unique=False)
	birthday = db.Column(db.String(80), unique=False)
	telephonenumber = db.Column(db.String(80), unique=False)
	cellphonenumber = db.Column(db.String(80), unique=False)
	nationality = db.Column(db.String(80), unique=False)
	datejoined = db.Column(db.String(80), unique=False)
	totaljobsdone = db.Column(db.String(80), unique=False)
	picture = db.Column(db.String(80), unique=False)
	isactivated = db.Column(db.String(80), unique=False)


	def __init__(self, email, password, firstname, lastname, country, city):
		self.email = email
		self.password = password
		self.firstname = firstname
		self.lastname = lastname
		self.country = country
		self.city = city

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

@app.route('/createdb')
def create_db():
	if not sqlalchemy_utils.functions.database_exists('sqlite:///skylld.db'):
		db.create_all()
	else:
		return 'The database was already created <br/> <a href="/">click here to go back</a>'
	return "created the database!"

@app.route('/dropdb')
def drop_db():
	if sqlalchemy_utils.functions.database_exists('sqlite:///skylld.db'):
		db.drop_all()
	else:
		return 'The database was already dropped <br/> <a href="/">click here to go back</a>'
	return "Database successfully dropped!"

@app.route('/')
def index():
	user_list = User.query.all()
	return render_template('index.html', user_list=user_list)

@app.route('/register', methods=['POST'])
def register_user():
	message = "";
	if request.method == 'POST':
		user = User(request.form['username'], request.form['password'], 'test@email.com')
		db.session.add(user)
		db.session.commit()
		message = "User successfully registered!"
		flash(message)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()