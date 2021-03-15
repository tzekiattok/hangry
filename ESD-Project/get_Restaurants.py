from flask import Flask, request, jsonify,render_template
from flask_cors import CORS


import os

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)


customer_URL = "http://localhost:5000"
restaurant_URL = "http://localhost:5001"
reservation_URL = "http://localhost:5002"

@app.route("/make_reservation", methods=['GET'])
def make_reservation():
    customerID ='Bartok'#static ID for testing
    result = get_Restaurants()
    print(result)
    restaurantList = result["data"]

    return render_template('customer_UI.html', restaurantList=restaurantList)

    '''
    return jsonify(
        {
        "code": result["code"],
        "data":{
            "restaurants": [r.json() for r in restaurantList]
        }
        }
    )'''
def get_Restaurants():
    print('\n-----Invoking order microservice-----')
    restaurant_result =invoke_http(restaurant_URL)
    print('restaurant_result:', restaurant_result)
    return restaurant_result
    code = restaurant_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of restaurantfails-----')
        print("Order status ({:d}) sent to the error microservice:".format(
            code), restaurant_result)
        return {
            "code": 500,
            "data": {"order_result": restaurant_result},
            "message": "Order creation failure sent for error handling."
        }

@app.route("/reserve/<string:restaurantID>",methods=['POST','GET'])
def view_Reservations(restaurantID):
    customerID ='tzekiat'#static ID for testing
    result = get_Reservations(restaurantID)
    print(result)
    reservationList = result["data"]
    restaurant_result = get_Restaurant_Details_By_ID(restaurantID)
    return render_template('reservation_UI.html', reservationList=reservationList,customerID=customerID,restaurant_result = restaurant_result)
def get_Restaurant_Details_By_ID(restaurantID):
    restaurant_result =invoke_http(restaurant_URL+"/"+restaurantID)
    print('restaurant_result:', restaurant_result)
    return restaurant_result
    code = restaurant_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of restaurantfails-----')
        print("Order status ({:d}) sent to the error microservice:".format(
            code), restaurant_result)
        return {
            "code": 500,
            "data": {"order_result": restaurant_result},
            "message": "Order creation failure sent for error handling."
        }

def get_Reservations(restaurantID):
    reservation_result =invoke_http(reservation_URL+'/reservation/'+restaurantID)
    print('restaurant_result:', reservation_result)
    return reservation_result
    code = reservation_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of restaurantfails-----')
        print("Order status ({:d}) sent to the error microservice:".format(
            code), reservation_result)
        return {
            "code": 500,
            "data": {"order_result": reservation_result},
            "message": "Order creation failure sent for error handling."
        }
@app.route("/request_reservation/<string:customerID>/<string:reservationID>",methods=['POST','GET'])
def request_Reservation(customerID,reservationID):
    reservation_result =invoke_http(reservation_URL+'/requestReservation/'+customerID+'/'+reservationID)
    print('reservation_result:', reservation_result)
    code = reservation_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of restaurantfails-----')
        print("Order status ({:d}) sent to the error microservice:".format(
            code), reservation_result)
        return {
            "code": 500,
            "data": {"order_result": reservation_result},
            "message": "Order creation failure sent for error handling."
        }
    return render_template('reservation_request.html',reservation_result=reservation_result)
    
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for making reservation")
    app.run( port=5200, debug=True)