from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from os import environ
import json
import amqp_setup
#Restaurant DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
dbr = SQLAlchemy(app)

#monitorBindingKey='*.restaurant'

notificationList = []

'''@app.route("/update",methods = ['GET','POST'])
def updateNotification():
    print('FK LA BODOH')
    #print(json.dumps(notificationList))
    #return notificationList'''

@app.route("/notifications/<string:restaurantID>",methods = ['GET','POST'])
def checkNotifications(restaurantID):
    amqp_setup.channel.stop_consuming() 
    amqp_setup.check_setup()
    queue_name = restaurantID  
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print('starting to listen for request of '+ restaurantID+'....')
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages;
    
    
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.
@app.route("/stop")
def exit():
    amqp_setup.channel.stop_consuming()
    print('stopping incoming notifications....')
    


def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an notification by " + __file__)
    processNotification(body)

    print() # print a new line feed

def processNotification(notification):
    print("Printing the notification message:")
    try:
        restNotification = json.loads(notification)
        print("--JSON:", restNotification)
    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", notification)
    print()


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')    
    '''print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    '''
    app.run(port=5003, debug=True)
    #checkNotifications()
    
    
   
