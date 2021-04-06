import json
import os
from flask import Flask, request, jsonify,render_template, redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import amqp_setup
app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/notification'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbn = SQLAlchemy(app)

class Notification(dbn.Model):
    __tablename__ = 'notification'

    notificationNum = dbn.Column(dbn.INT, primary_key=True)
    reservationID = dbn.Column(dbn.String(64), nullable = False)
    receiverId = dbn.Column(dbn.String(64), nullable = False)
    customerId = dbn.Column(dbn.String(64), nullable = False)
    restaurantID = dbn.Column(dbn.String(64), nullable = False)
    reservationDate = dbn.Column(dbn.String(64), nullable = False)
    reservationTime = dbn.Column(dbn.String(64), nullable = False)
    duration = dbn.Column(dbn.String(64), nullable = False)
    status = dbn.Column(dbn.String(64), nullable = False)


    def json(self):
        return {"notificationNum": self.notificationNum, "reservationID": self.reservationID, "receiverId": self.receiverId, "customerId": self.customerId, "restaurantID": self.restaurantID, "reservationDate": self.reservationDate, "reservationTime": self.reservationTime, "duration": self.duration, "status": self.status}
    # def __init__(self, notificationNum, reservationID, receiverId, customerId, restaurantID, reservationDate, reservationTime):
    #     self.notificationNum = notificationNum
    #     self.reservationID = reservationID
    #     self.receiverId = receiverId
    #     self.customerId = customerId
    #     self.restaurantID = restaurantID
    #     self.reservationDate = reservationDate
    #     self.reservationTime = reservationTime




@app.route("/notifications/<string:userID>", methods = ['GET'])
def receiveNotification(userID):
    amqp_setup.channel.stop_consuming()
    amqp_setup.check_setup()
    
    queue_name = userID
    
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.connection.process_data_events(time_limit=5)
    amqp_setup.channel.start_consuming()
    # while amqp_setup.channel._consumer_infos:
    #     amqp_setup.channel.connection.process_data_events(time_limit=1)
    print("AMQP Stopped")

@app.route("/retrieveNotifications/", methods = ['GET'])
def getNotification():
    #notification = Notification.query.all()
    print("Success!")
    return "Yes"

@app.route("/getNotifications/<string:uid>")
def pending_reservation_restaurant_by_ID(uid):
    # capital R, you are calling a class created above
    NotificationList= Notification.query.filter_by(receiverId= uid)
    if NotificationList:
            #Must json.encode back when updating to DB
        return jsonify(
            {
                "code": 200,
                "data": {
                    "notification": [notification.json() for notification in  NotificationList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no notifications for this restaurant."
        }
    ), 404




def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an notification by " + __file__)

    processNotification(body) #Edit this to modify the output
    print() # print a new line feed
    #amqp_setup.channel.stop_consuming()
   
    # if status.method.message_count == 0:
    #     amqp_setup.channel.stop_consuming()
    #     print("AMQP Stopped")
    


def processNotification(msg):
    print("Printing the notification message:")
    try:
        error = json.loads(msg)
        

        print(type(error))
        createNewNotificationRecord(error)
        #print(error)
        #print(error["data"]["reservation"])
        print("--JSON:", error)
    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", msg)
    print()

def createNewNotificationRecord(msg):
    if("reservation" in msg['data'].keys()):
        data = msg["data"]["reservation"][0]
    else:
        data = msg["data"]
  
    receiverId = data["customerID"]
    capacity = data["capacity"]
    customerId = data["customerID"]
    reservationId = data["reservationID"]
    restaurantId = data["restaurantID"]
    date = data["date"]
    time = data["time"]
    duration = data["duration"]
    status = data["status"]
    #Notification.query.filter_by(notificationNum).last()
    obj = Notification(reservationID=reservationId, receiverId=receiverId, customerId=customerId, restaurantID=restaurantId, reservationDate=date, reservationTime=time, duration=duration, status=status)
    # dbn.drop_all()
    # dbn.create_all()
    print(data)
    dbn.session.add(obj)
    dbn.session.commit()
    app.logger.info(obj.notificationNum)




if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')    
    print("\nThis is " + os.path.basename(__file__), end='')
    #print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    #receiveNotification()
    app.run(port=5008, debug=True)