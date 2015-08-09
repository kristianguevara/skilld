from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy_utils

app = Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skylld.db'
api = Api(app)
db = SQLAlchemy(app)
parser = reqparse.RequestParser()

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

class Users(Resource):
	def get(self):
		return {'hello': 'world'}

	def post(self):
		args = parser.parse_args()
		self.parser.add_argument('user', type=str, location='json', required=True)
		#parser.add_argument('email')
		print self.response

class CreateDb(Resource):
	def get(self):
		if not sqlalchemy_utils.functions.database_exists('sqlite:///skylld.db'):
			db.create_all()
			return "Database successfully created"
		else:
			return 'A database is already existing.'

class DropDb(Resource):
	def get(self):
		if sqlalchemy_utils.functions.database_exists('sqlite:///skylld.db'):
			db.drop_all()
			return "Database successfully dropped!"
		else:
			return 'There is no database existing.'

api.add_resource(Users, '/')
api.add_resource(CreateDb, '/createdb')
api.add_resource(DropDb, '/dropdb')

if __name__ == '__main__':
    app.run(debug=True)