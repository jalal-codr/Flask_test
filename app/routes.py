from . import app
from flask import request
from flask_restful import Resource, Api
from . import db
import json

api = Api(app)


@app.route('/')
def index():
    return('Hello World')

# class User(Resource):
#     def post(self):
#         user = request.get_json()
#         new_user = {
#             "name":user['name'],
#             "age":user['age']
#         }
#         new_user_json=json.dumps(new_user)
#         user_collection = db['users']
#         user_collection.insert_one(new_user_json)
#         return(new_user_json)
    

#     def get(self):
#         users = db.users.find()
#         users_json= json.loads(users)
#         return(users_json)
    

# api.add_resource(User,'/user')