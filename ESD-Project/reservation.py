from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

#Restaurant DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/reservation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbr = SQLAlchemy(app,session_options={"autoflush": False}) #autoflush = false to disable query session issues with searching
dbr.autoflush = False
class Reservation(dbr.Model):
    __tablename__ = 'reservation'
    reservationID = dbr.Column(dbr.INT, primary_key=True)
    restaurantID = dbr.Column(dbr.String(64), primary_key=True)
    customerID = dbr.Column(dbr.String(64), nullable=True)
    capacity = dbr.Column(dbr.INT, nullable=False)
    date = dbr.Column(dbr.Date, nullable=False)
    time = dbr.Column(dbr.Time, nullable=False)
    duration = dbr.Column(dbr.Float(precision=2),nullable = False)
    status = dbr.Column(dbr.String(10),nullable=False)

    def __init__(self, reservationID, restaurantID, customerID, capacity,date,time,duration,status):
        self.reservationID = reservationID
        self.restaurantID = restaurantID
        self.customerID = customerID
        self.capacity =capacity
        self.date =date
        self.time = time
        self.duration = duration
        self.status = status
    def json(self):
        return {"reservationID": self.reservationID,"restaurantID": self.restaurantID, "customerID": self.customerID, "capacity": self.capacity, "date": self.date, "time": self.time,"duration": self.duration,"status": self.status}

####################################################################################################################################################################

#reservation Functions

####################################################################################################################################################################

#view all reservations
@app.route("/reservation")
def get_all_reservations():
    # capital R, you are calling a class created above
    reservationList = Reservation.query.all()
    if len(reservationList):
        for x in reservationList:
            temp = json.dumps(x.time,default= str)
            temp = temp[1:-1]
            x.time = temp
            temp = json.dumps(x.date,default= str)
            temp = temp[1:-1]
            x.date= temp
            
            #Must json.encode back when updating to DB
        x = jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  reservationList]
                }
            }
        )
        
        return x
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404


@app.route("/requestReservation/<string:customerID>/<int:reservationID>", methods=['GET','PUT'])
def create_reservation(customerID,reservationID):
   
    #data = request.get_json()
    res = Reservation.query.filter_by(reservationID=reservationID).first()
    if res:
        #data = request.get_json()
        res.customerID = customerID
        res.status = "pending"
        dbr.session.commit()
        #convert date time format to string as JSONIFY does not allow DT format
        temp = json.dumps(res.time,default= str)
        temp = temp[1:-1]
        res.time = temp
        temp = json.dumps(res.date,default= str)
        temp = temp[1:-1]
        res.date= temp
        return jsonify(
            {
                "code": 201,
                "data": res.json()
            }
        ), 201
    


# Customer: return all specific restaurant based on ID 
@app.route("/reservation/<string:restaurantID>")
def reservation_restaurant_by_reservationID(restaurantID):
    # capital R, you are calling a class created above
    reservationList2= Reservation.query.filter_by(restaurantID= restaurantID,status = "open")
    
    if reservationList2:
        for x in reservationList2:
            temp1 = json.dumps(x.time,default= str)
            temp1 = temp1[1:-1]
            x.time = temp1
            temp2 = json.dumps(x.date,default= str)
            temp2 = temp2[1:-1]
            x.date= temp2
            
            #Must json.encode back when updating to DB
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  reservationList2]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reservations for this restaurant."
        }
    ), 404



@app.route("/reservationID/<int:reservationID>")
def reservation_restaurant_by_ID(reservationID):
    # capital R, you are calling a class created above
    reservationList2= Reservation.query.filter_by(reservationID= reservationID,status = "open")
    
    if reservationList2:
        for x in reservationList2:
            
            temp1 = json.dumps(x.time,default= str)
            temp1 = temp1[1:-1]
            x.time = temp1
            temp2 = json.dumps(x.date,default= str)
            temp2 = temp2[1:-1]
            x.date= temp2
            
            #Must json.encode back when updating to DB
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  reservationList2]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reservations for this restaurant."
        }
    ), 404
#get reservation by customerID
@app.route("/customerID/<string:customerID>" ,methods =['GET','POST'])
def retrieve_reservation_by_customer(customerID):
    # capital R, you are calling a class created above
    customerList= Reservation.query.filter_by(customerID=customerID)
    for x in customerList:
            
            temp1 = json.dumps(x.time,default= str)
            temp1 = temp1[1:-1]
            x.time = temp1
            temp2 = json.dumps(x.date,default= str)
            temp2 = temp2[1:-1]
            x.date= temp2
    if customerList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  customerList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reservations under this customer."
        }
    ), 404
#reserve a slot

@app.route("/reservation/customer/<string:reservationID>" ,methods =['GET','POST'])
def retrieve_customerID_by_reservationID(reservationID):
    # capital R, you are calling a class created above
    reservationRecord = Reservation.query.filter_by(reservationID = reservationID).first()
    customerId = reservationRecord.customerID
    
    if customerId:
        return jsonify(
            {
                "code": 200,
                "message": customerId
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customer under this reservation."
        }
    ), 404


@app.route("/reservation/accept/<string:reservationID>", methods = ['GET', 'POST'])
def accept_reservation(reservationID):
    
    reservationRecord = Reservation.query.filter_by(reservationID = reservationID).first()
    reservationRecord.status = 'confirmed'
    dbr.session.commit()
    
    return jsonify(
            {
                "code": 200,
                "message": "Reservation ID: " + str(reservationRecord.reservationID) + " has been confirmed!",
                "data": {
                    "time": str(reservationRecord.time),
                    "date": str(reservationRecord.date)
                }
            }
        )

@app.route("/reservation/decline/<string:reservationID>", methods = ['GET', 'POST'])
def decline_reservation(reservationID):
    
    reservationRecord = Reservation.query.filter_by(reservationID = reservationID).first()
    reservationRecord.status = 'declined'
    dbr.session.commit()
    
    return jsonify(
            {
                "code": 200,
                "message": "Reservation ID: " + str(reservationRecord.reservationID) + " has been declined!",
                "data": {
                    "time": str(reservationRecord.time),
                    "date": str(reservationRecord.date)
                }
            }
        )
@app.route("/pendingreservation/<string:restaurantID>")
def pending_reservation_restaurant_by_ID(restaurantID):
    # capital R, you are calling a class created above
    reservationList2= Reservation.query.filter_by(restaurantID= restaurantID,status = "pending")
    if reservationList2:
        for x in reservationList2:
            
            temp1 = json.dumps(x.time,default= str)
            temp1 = temp1[1:-1]
            x.time = temp1
            temp2 = json.dumps(x.date,default= str)
            temp2 = temp2[1:-1]
            x.date= temp2
            
            #Must json.encode back when updating to DB
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  reservationList2]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reservations for this restaurant."
        }
    ), 404


@app.route("/getreservationID/<int:reservationID>")
def get_any_reservation_by_id(reservationID):
    # capital R, you are calling a class created above
    reservationList2= Reservation.query.filter_by(reservationID= reservationID)
    
    if reservationList2:
        for x in reservationList2:
            
            temp1 = json.dumps(x.time,default= str)
            temp1 = temp1[1:-1]
            x.time = temp1
            temp2 = json.dumps(x.date,default= str)
            temp2 = temp2[1:-1]
            x.date= temp2
            
            #Must json.encode back when updating to DB
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reservation": [reservation.json() for reservation in  reservationList2]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reservations for this restaurant."
        }
    ), 404
####################################################################################################################################################################
# Dont edit what is after this
if __name__ == '__main__':
    app.run(port=5002, debug=True)
