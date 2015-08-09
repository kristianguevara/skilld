from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy_utils
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('sqlite:///skylld2.db')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skylld2.db'
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
		return '<User %r>' % self.email

def new_alchemy_encoder():
	_visited_objs = []
	class AlchemyEncoder(json.JSONEncoder):
		def default(self, obj):
			if isinstance(obj.__class__, DeclarativeMeta):
                    # don't re-visit self
				if obj in _visited_objs:
					return None
					_visited_objs.append(obj)

                    # an SQLAlchemy class
					fields = {}
					for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
						fields[field] = obj.__getattribute__(field)
                    # a json-encodable dict
				return fields

			return json.JSONEncoder.default(self, obj)
        return AlchemyEncoder

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

@app.route('/users', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		user = User(request.form['email'], request.form['password'], request.form['firstname'], request.form['lastname'], \
			request.form['country'], request.form['city'])
		db.session.add(user)
		db.session.commit()
		return "User successfully reigstered"
	else:
		return jsonify(session.query(User).all())


if __name__ == '__main__':
    app.run(debug=True)