# Importing the db instance from the config module
from config import db

# Defining a Contact class that inherits from db.Model (provided by SQLAlchemy)
class Contact(db.Model):
    # Defining columns for the Contact table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Method to convert Contact object to JSON format
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,   
        }