# Importing necessary modules from Flask framework
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Creating an instance of the Flask class
app = Flask(__name__)

# Allowing Cross-Origin Resource Sharing (CORS) for the Flask app
CORS(app)

# Configuration settings for the SQLAlchemy database
# Setting the path to the SQLite database file
app.config["SQLALCHEMY_DATABASE_URL"] = "sqllite:///database.db"
# Disabling modification tracking to reduce overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Creating an instance of the SQLAlchemy class with the Flask app as its argument
db = SQLAlchemy(app)