from flask import Flask
from sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with, abort, fields, reqparse


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(30), nullable=False)
  
  def __repr__(self):
    return f'name: {self.name} - email: {self.email}'
  
arg_user = reqparse.RequestParser()
arg_user.add_argument('name', type=str, help='name must be a string', required=True)
arg_user.add_argument('email', type=str, help='email must be a string', required=True)

userFields = {
  'id': fields.Integer,
  'name': fields.String,
  'email': fields.String 
}

class User(Resource):
  @marshal_with(userFields)
  def get(self):
    uses = User.query.all()
    return users
    