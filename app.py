from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt import JWT, jwt_required

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
from security import authenticate, identity
from resources.user import UserRegister

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()
