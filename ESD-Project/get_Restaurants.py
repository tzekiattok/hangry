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


customer_URL = "http://localhost:5006"
restaurant_URL = "http://localhost:5001"
reservation_URL = "http://localhost:5002"

@app.route("/make_reservation/<string:customerID>", methods=['GET','POST'])
def make_reservation(customerID):
    #static ID for testing
    result = invoke_http(restaurant_URL+'/')
    print(result)
    restaurantList = result["data"]

    return render_template('customer_UI.html', restaurantList=restaurantList,customerID =customerID)

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

@app.route("/reserve/<string:restaurantID>/<string:customerID>",methods=['POST','GET'])
def view_Reservations(restaurantID,customerID):
    result = get_Reservations(restaurantID)
    print(result)
    reservationList = result["data"]
    restaurant_result = get_Restaurant_Details_By_ID(restaurantID)
    return render_template('reservation_UI.html', reservationList=reservationList,customerID=customerID,restaurant_result = restaurant_result)

def get_Restaurant_Details_By_ID(restaurantID):
    def view_Reservations(restaurantID):
        customerID ='tzekiat'#static ID for testing
    result = get_Reservations(restaurantID)
    print(result)
    reservationList = result["data"]
    restaurant_result = get_Restaurant_Details_By_ID(restaurantID)
    restaurant_result = restaurant_result["data"]
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

#to add AMQP in 

#API to send the email
@app.route("/request_reservation/<string:customerID>/<string:reservationID>",methods=['POST','GET'])
def request_Reservation(customerID,reservationID):
    reservation_result =invoke_http(reservation_URL+'/requestReservation/'+customerID+'/'+reservationID)
    print('reservation_result:', reservation_result)
    code = reservation_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of reservation fails-----')
        print("Order status ({:d}) sent to the error microservice:".format(
            code), reservation_result)
        return {
            "code": 500,
            "data": {"reservation_result": reservation_result},
            "message": "reservation request failure sent for error handling."
        }
    customerID = 'bartok'


    customer_result =invoke_http(customer_URL+'/customer/'+customerID)
    print('customer:', customer_result)
    restaurantDetails = reservation_result["data"]
    restaurantID = restaurantDetails["restaurantID"]
    restaurant_result =invoke_http(restaurant_URL+'/restaurantID/'+restaurantID)
    print('restaurant:', restaurant_result)
    #Retrieve customer name
    code = customer_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Retrieval of customer data failed-----')
        print("customer status ({:d}) sent to the error microservice:".format(
            code), customer_result)
        return {
            "code": 500,
            "data": {"customer_result": customer_result},
            "message": "customer retrieval failed."
        }
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
    restEmail = restaurant_result["data"]["email"]
    restName = restaurant_result["data"]["name"]
    customerDetails = customer_result["data"]
    customerName = ['name']
    reservationDetails = reservation_result['data']
    restCapacity = reservationDetails['capacity']
    restDate = reservationDetails['date']
    restTime = reservationDetails['time']
    #payload = "{\"personalizations\": [{\"to\": [{ \"email\": \""+restEmail+"\"}],\"subject\": \""+"Reservation for"+restName+"\" }],\"from\": {  \"email\": \"Lafamme@gmail.com\"},\"content\": [ { \"type\": \"text/plain\", \"value\": \""+"Hello "+customerName+", you had made a reservation on "+str(restDate)+", at"+str(restTime)+" for "+restCapacity+"people"+"\" } ]}"
    message = "hello "+restName+", a customer had requested to make a reservation on "+str(restDate)+" "+str(restTime)+""+" for "+str(restCapacity)+" people. "+" Please go to the website to accept the request."
    payload = "{\"personalizations\": [{\"to\": [{ \"email\": \""+restEmail+"\"}],\"subject\": \""+"Reservation for "+restName+"\" }],\"from\": {  \"email\": \"Lafamme@gmail.com\"},\"content\": [ { \"type\": \"text/plain\", \"value\": \""+message+"\" } ]}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "886f2677a1msh5ff304f26342ba6p1870d2jsn60147b27c6b5",
        'x-rapidapi-host': "rapidprod-sendgrid-v1.p.rapidapi.com"            }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(payload)
    print(response.text,'is the response')
    restID = restaurant_result["data"]["restaurantID"]
    message2 = json.dumps(reservation_result)
    #send email confirmation notification to restaurant owners
    #use of MQ Rabbit
    r_key = restID
    #create a queue for the restaurant if no queue has been established yet
    hostname = "localhost" # default hostname
    port = 5672 # default port
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port,
        heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
))
    exchangename="order_topic"
    exchangetype="topic"
    
    channel = connection.channel()
    queue_name = r_key
    channel.queue_declare(queue=queue_name, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=r_key)
    channel.basic_publish(exchange=exchangename, routing_key=r_key,
            body=message2, properties=pika.BasicProperties(delivery_mode = 2))
    print('msg sent')
    connection.close()

    print('created queue: '+restID)
    return render_template('reservation_request.html',reservation_result=reservation_result)
    
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for making reservation")
    app.run( port=5200, debug=True)