from flask import Flask, request, jsonify,render_template, session
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
fixed_ID = "EighteenChefz"

reservation_URL = "http://localhost:5002"
customer_URL = "http://localhost:5006"

@app.route("/answer_Reservations/<string:restaurantID>", methods=['GET'])
def viewRestaurantReservation(restaurantID):
    
    restaurant_result =invoke_http(reservation_URL + "/pendingreservation/" + restaurantID)
    # Get individual input
    # print(restaurant_result["data"]["reservation"][0])
    return  restaurant_result

@app.route("/answer_Reservation/accept/<string:reservationID>",methods=['POST','GET'])
def acceptReservation(reservationID):
    restaurant_result = invoke_http(reservation_URL + "/reservation/accept/" + reservationID)
    customerID = invoke_http(reservation_URL + "/reservation/customer/" + reservationID)
    customer = invoke_http(customer_URL + "/getCustomerTele/" + customerID["message"])
    invoke_http("https://api.telegram.org/bot1773074094:AAHq8QeKk0AGqSgOz6tsci4-b6zJuJJF4UE/sendmessage?chat_id=" + customer["message"] +"&text= + " + "Your reservation for " + reservationID + " on " + restaurant_result["data"]["date"]  +" at " + restaurant_result["data"]["time"][:5] + " has been confirmed!")
    
    reservationInformation = invoke_http(reservation_URL + "/getreservationID/" + reservationID)
    message = json.dumps(reservationInformation)

    hostname = "localhost" 
    port = 5672
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=hostname, port=port,
            heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
    ))
   
    channel = connection.channel()

    exchangename="order_topic"
    exchangetype="topic"
    channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

    queue_name = customerID["message"]
    channel.queue_declare(queue=queue_name, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=customerID["message"])
    channel.basic_publish(exchange=exchangename, routing_key=customerID["message"], 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))
    return restaurant_result

@app.route("/answer_Reservation/decline/<string:reservationID>",methods=['POST','GET'])
def declineReservation(reservationID):
    restaurant_result =invoke_http(reservation_URL + "/reservation/decline/" + reservationID)
    customerID = invoke_http(reservation_URL + "/reservation/customer/" + reservationID)
    customer = invoke_http(customer_URL + "/getCustomerTele/" + customerID["message"])
    invoke_http("https://api.telegram.org/bot1773074094:AAHq8QeKk0AGqSgOz6tsci4-b6zJuJJF4UE/sendmessage?chat_id=" + customer["message"] +"&text= + " + "So sorry! Your reservation for " + reservationID + " on " + restaurant_result["data"]["date"] + " at " + restaurant_result["data"]["time"][:5] + " has been declined!")
    
    
    reservationInformation = invoke_http(reservation_URL + "/getreservationID/" + reservationID)
    message = json.dumps(reservationInformation)

    hostname = "localhost" 
    port = 5672
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=hostname, port=port,
            heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
    ))
   
    channel = connection.channel()

    exchangename="order_topic"
    exchangetype="topic"
    channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

    queue_name = customerID["message"]
    channel.queue_declare(queue=queue_name, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=customerID["message"])
    channel.basic_publish(exchange=exchangename, routing_key=customerID["message"], 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))
    return restaurant_result

@app.route("/testRoute/<string:reservationID>/<string:customerID>",methods=['POST','GET'])
def sendAcceptNotification(reservationID, customerID):
    reservationInformation = invoke_http(reservation_URL + "/getreservationID/" + reservationID)
    message = json.dumps(reservationInformation)

    hostname = "localhost" 
    port = 5672
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=hostname, port=port,
            heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
    ))
   
    channel = connection.channel()

    exchangename="order_topic"
    exchangetype="topic"
    channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

    queue_name = customerID
    channel.queue_declare(queue=queue_name, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=customerID)
    channel.basic_publish(exchange=exchangename, routing_key=customerID, 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))
    return message


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for replying to reservation")
    app.run( port=5300, debug=True)