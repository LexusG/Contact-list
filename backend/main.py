# Importing necessary modules from Flask framework.
# Importing the app instance and the db object from the config module.
# Importing the Contact model from the models module.
from flask import request, jsonify
from config import app, db
from models import Contact

# Defining a route for handling GET requests to "/contacts"
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Querying all contacts from the Contact table
    contacts = Contact.query.all()
    
    # Converting each Contact object to JSON format
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    
    # Returning the contacts as a JSON response
    return jsonify({"contacts": json_contacts})

# Defining a route for handling POST requests to "/contacts"
@app.route("/contacts", methods=["POST"])
def create_contact():
    # Retrieving data from the request JSON payload
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
   
    # Validating presence of required fields
    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "You must include a first name, last name and email"}), 
            400,
        )
    
    # Creating a new Contact instance    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        # Adding the new contact to the database session and committing the changes
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        # Handling exceptions and returning an error response
        return jsonify({"message": str(e)}), 400
    # Returning a success response
    return jsonify({"message": "User Created!"}), 201


# Running the Flask app
if __name__ == "__main__":
    # Creating all database tables within the app context
    with app.app_context():
        db.create_all()
    
    # Running the app in debug mode
    app.run(debug=True)

    