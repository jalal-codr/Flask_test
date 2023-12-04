from . import app
from flask import request
from flask_restful import Resource, Api
from . import db
import json

api = Api(app)


@app.route('/')
def index():
    return('Hello World')
