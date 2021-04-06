from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Over here there will be 3 functions 
#1) View PreOrder
#2) Make PreOrder -> Choosing Item and select quantity (ERMM IDK WHAT AM I DOING)
#3) Make Payment (NOT DONE)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/pre_order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
class pre_order(db.Model):
    __tablename__ = 'pre_order'

    orderID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.VARCHAR)

    def __init__(self,orderID,customerID,status):
        self.orderID = orderID
        self.customerID = customerID
        self.status = status
 
    def json(self):
        return {"orderID": self.orderID, "customerID":self.customerID , "status":self.status }

class pre_order_items(db.Model):
    __tablename__ = "pre_order_items"

    orderID = db.Column(db.Integer, primary_key=True)
    itemID = db.Column(db.Integer)
    itemName = db.Column(db.VARCHAR)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self,orderID,itemID,itemName,price,quantity):
        self.orderID = orderID
        self.itemID = itemID
        self.itemName = itemName
        self.price = price
        self.quantity = quantity
 
    def json(self):
        return {"orderID":self.orderID, "itemID":self.itemID , "itemName":self.itemName,"price":self.price ,"quantity":self.quantity }

#View all the pre_orders
@app.route("/pre_order")
def view_all():
    pre_order_list = pre_order.query.all()
    if len(pre_order_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "pre_order": [pre_order.json() for pre_order in pre_order_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no pre_order."
        }
    ), 404
 
# View the pre_order -> Order1
@app.route("/pre_order/<string:Order1>")
def find_by_order(Order1):
    specific_order = pre_order.query.filter_by(orderID=Order1).first()
    if specific_order:
        return jsonify(
            {
                "code": 200,
                "data": specific_order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "pre Order not found."
        }
    ), 404


#Creating pre_order 
@app.route("/pre_order/<string:Order7>", methods=['POST'])
def create_pre_order(Order7):
    #Follow SQL style Where Field name = Data 
    if (pre_order.query.filter_by(orderID=Order7).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Order7": Order7
                },
                "message": "Order7 already exists."
            }
        ), 400
 
    data = request.get_json()
 #DK book = Book(isbn13, **data)
    Order7 = pre_order(Order7, **data)

    try:
        db.session.add(pre_order)
        db.session.commit()

    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Order7": Order7
                },
                "message": "An error occurred creating the book."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": pre_order.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(port=5004, debug=True)

