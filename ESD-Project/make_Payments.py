from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

#Complex MS
import json
import os
import amqp_setup
import pika
import requests
from invokes import invoke_http
import os
import requests


app = Flask(__name__)
CORS(app)

#3 Functions in general 
#1) Check reservations -> Display them if any Done 
#2.1) Click on reservations -> Display menu on UI as a table Done
#2.2) Select item and quantity  Done
#2.3) Compute the total in another page Done
#4) Payment

#customerID ='Bartok'
#reservationID = '3'
#restaurantID = "Eighteenchefz"

#List of Microservices needed for this COMPLEX microservice
customer_URL = "http://localhost:5006/"
restaurant_URL = "http://localhost:5001/"

#@app.route("/customerID/<string:customerID>" ,methods =['GET','POST'])
reservation_URL = "http://localhost:5002/"

pre_order_URL = "http://localhost:5004/"

#@app.route("/menu/<string:restaurantid>")
menu_URL = "http://localhost:5005/"

# #Function 1 Checking if reservations are made.
# #Reservation are 1-19, #USE reservation 3 -> Customer ID Bartok
@app.route("/check_reservation", methods=['GET'])
def check_reservation():
    #static ID for testing
    customerID ='Bartok'
    reservationID = '3'

    #Function to get the list of reservations
    def get_Reservations(customerID):
        print('\n-----Invoking order microservice-----')

        #Invoking the microservice -> Reservation
        reservation_result = invoke_http(reservation_URL + '/customerID/' + customerID)

        #Printing to see  if it works?
        print('reservations:',reservation_result)
        return reservation_result

    #Checking if the reservations are working 
    result = get_Reservations(customerID)
    print("this is reservations result", result)
    reservationsList = result["data"]

    return reservationsList
    #Putting it in the Payment UI
    # return render_template('reservation_UI.html', reservationsList = reservationsList)

    #Look at Error/Working code?
    code = result['code']
    if code not in range(200, 300):
        print('\n\n-----Retrieval of reservation failed-----')
        print("Order status ({:d}) sent to the error microservice:".format(code), result)

        return {
            "code": 500,
            "data": {"reservation_result": result},
            "message": "reservation creation creation failure sent for error handling."
        }


#Function 2 Display Menu:
@app.route("/get_menu/<string:restaurantID>", methods=['GET'])

def get_menu(restaurantID):
    customerID ='Bartok'
    reservationID = '3'
    restaurantID = "EighteenChefz"

    #Function to get the list of items from menu
    def get_restaurant_menu(restaurantID):
        print('\n-----Invoking order microservice-----')

        #Invoking the microservice -> Menu
        menu_result = invoke_http(menu_URL + '/menu/' + restaurantID)
    
        #Printing to see  if it works?
        print('menu:',menu_result)
        return menu_result

    result = get_restaurant_menu(restaurantID)
    print("this is menu result", result)
    menuList = result["data"]
    return menuList

    #Putting it in the UI
    
    # return render_template('check_reservation.html', menuList = menuList)

    # Look at Error/Working code?
    code = result['code']
    if code not in range(200, 300):
        print('\n\n-----Retrieval of reservation failed-----')
        print("Order status ({:d}) sent to the error microservice:".format(code),result)

        return {
            "code": 500,
            "data": {"menu_result": result},
            "message": "menu creation failure sent for error handling."
        }

#Function 3:
# @app.route("/", methods=['PUT'])


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for making reservation")
    app.run( port=5300, debug=True)