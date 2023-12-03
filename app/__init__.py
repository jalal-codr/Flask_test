from flask import Flask, request
from pymongo import MongoClient



mongo_uri='mongodb+srv://panda:panda@cluster0.zjjtilw.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_uri)
db=client.db


app = Flask(__name__)
from . import routes
from . import user