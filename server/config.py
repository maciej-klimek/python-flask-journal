from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe_database.db"
app.config["SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "static/images"

db = SQLAlchemy(app)
