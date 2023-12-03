from . import app
from flask import request,jsonify
from flask_restful import Resource, Api
from . import db
import json

api = Api(app)

class User(Resource):
    def post(self):
        user = request.get_json()
        new_user = {
            "name":user['name'],
            "age":user['age']
        }
        user_collection = db['users']
        result = user_collection.insert_one(new_user)
        if result.acknowledged:
            inserted_id = str(result.inserted_id)
            return {"message": "Object saved successfully", "_id": inserted_id}, 201
        else:
            return {"message": "Failed to save object"}, 500
    

    def get(self):
        user_collection = db['users']
        users = user_collection.find()
        users_list= list(users)
        for obj in users_list:
            obj["_id"] = str(obj["_id"])
        return jsonify(users_list)
    
api.add_resource(User,'/user')