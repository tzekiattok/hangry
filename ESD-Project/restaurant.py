from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from os import environ
#Restaurant DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
dbr = SQLAlchemy(app)

class Restaurant(dbr.Model):
    __tablename__ = 'restaurant'

    restaurantID = dbr.Column(dbr.String, primary_key=True)
    name = dbr.Column(dbr.String(64), nullable=False)
    branch = dbr.Column(dbr.String(64), nullable=False)
    category = dbr.Column(dbr.String(64), nullable=False)
    location = dbr.Column(dbr.String(64), nullable=False)
    description = dbr.Column(dbr.String(500), nullable=False)
    rating = dbr.Column(dbr.Float(precision=2))
    review = dbr.Column(dbr.String(300), nullable=True)

    def __init__(self, restaurantID, name, branch, category, location, description, rating, review):
        self.restaurantID = restaurantID
        self.name = name
        self.branch=  branch
        self.category = category
        self.location = location
        self.description = description
        self.rating = rating
        self.review= review

    def json(self):
        return {"restaurantID": self.restaurantID, "name": self.name, "branch": self.branch, "category": self.category, "location": self.location,"description" :self.description,"rating": self.rating,"review": self.review}

####################################################################################################################################################################

#Restaurant Owner Functions

####################################################################################################################################################################


@app.route("/")
def get_all_restaurants():
    # capital R, you are calling a class created above
    restaurantList = Restaurant.query.all()
    if len(restaurantList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "restaurant": [restaurant.json() for restaurant in  restaurantList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404

# Customer: return all specific restaurant based on ID 
@app.route("/<string:restaurantID>")
def retrieve_restaurant_by_ID(restaurantID):
    # capital R, you are calling a class created above
    restaurant= Restaurant.query.filter_by(restaurantID= restaurantID).first()
    if restaurant:
        return jsonify(
            {
                "code": 200,
                "data": restaurant.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no restaurant."
        }
    ), 404
#get restaurant by name
@app.route("/name/<string:name>")
def retrieve_restaurant_by_name(name):
    # capital R, you are calling a class created above
    restaurant= Restaurant.query.filter_by(name=name).first()
    if restaurant:
        return jsonify(
            {
                "code": 200,
                "data": restaurant.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no restaurant."
        }
    ), 404
#Register Restaurant
@app.route("/restaurant/register/<string:restaurantID>", methods=['GET','POST'])
def create_restaurant(restaurantID):
    if (Restaurant.query.filter_by(restaurantID=restaurantID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "restaurantID": restaurantID
                },
                "message": "Customer already exists."
            }
        ), 400
 
    #data = request.get_json()
    restaurant = Restaurant(restaurantID,'Bhorbee Bee', '96189197', '@sexyBhorbee', 'NULL')
 
    try:
        dbr.session.add(restaurant)
        dbr.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "restaurantID": restaurantID
                },
                "message": "An error occurred creating the restaurant."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": restaurant.json()
        }
    ), 201

####################################################################################################################################################################
# Dont edit what is after this
if __name__ == '__main__':
    app.run(port=5001, debug=True)
