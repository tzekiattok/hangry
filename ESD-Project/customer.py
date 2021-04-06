# app.py for ESD-Project
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
#from flask_cors import CORS
app = Flask(__name__)

# Database Configuration
# Database - customer configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbc = SQLAlchemy(app)
#Priority
#Customer->Restaurant->Reservation->Menu->Preorder->Notifications
#Customer DB configuration
class Customer(dbc.Model):
    __tablename__ = 'customer'

    customerID = dbc.Column(dbc.String(64), primary_key=True)
    name = dbc.Column(dbc.String(64), nullable=False)
    phone = dbc.Column(dbc.String(8), nullable=False)
    telegram = dbc.Column(dbc.String(64), nullable=False)
    profilePic = dbc.Column(dbc.String(500), nullable=True)

    def __init__(self, customerID, name, phone, telegram, profilePic):
        self.customerID = customerID
        self.name = name
        self.phone = phone
        self.telegram = telegram
        self.profilePic = profilePic

    def json(self):
        return {"customerID": self.customerID, "name": self.name, "phone": self.phone, "telegram": self.telegram, "profilePic": self.profilePic}

# Routes to to be added1
@app.route("/")
def home():
    return "Welcome to ESD-Project!"
####################################################################################################################################################################

#Customer Functions

####################################################################################################################################################################
# Customer: return all customers
@app.route("/customer")
def get_all():
    # capital C, you are calling a class created above
    customerList = Customer.query.all()
    if len(customerList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "books": [customer.json() for customer in customerList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404

# Customer: return all specific customer based on ID
@app.route("/customer/<string:customerID>")
def retrieve_customer_by_ID(customerID):
    # capital C, you are calling a class created above
    customer= Customer.query.filter_by(customerID=customerID).first()
    if customer:
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404

#Register Customer
@app.route("/register/<string:customerID>", methods=['GET','POST'])
def create_book(customerID):
    if (Customer.query.filter_by(customerID=customerID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "customerID": customerID
                },
                "message": "Customer already exists."
            }
        ), 400
 
    #data = request.get_json()
    customer = Customer(customerID,'Bhorbee Bee', '96189197', '@sexyBhorbee', 'NULL')
 
    try:
        dbc.session.add(customer)
        dbc.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "customerID": customerID
                },
                "message": "An error occurred creating the book."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": customer.json()
        }
    ), 201

@app.route("/getCustomerTele/<string:customerID>")
def retrieve_telegram_by_ID(customerID):
    # capital C, you are calling a class created above
    customer = Customer.query.filter_by(customerID=customerID).first()
    
    return jsonify(
        {
            "code": 200,
            "message": str(customer.telegram)
        }
    )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customer."
        }
    ), 404

####################################################################################################################################################################
# Dont edit what is after this
if __name__ == '__main__':
    app.run(port=5006, debug=True)
#docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/customer toktzekiat/customer