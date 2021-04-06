from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/menu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class menu(db.Model):
    __tablename__ = 'menu'

    menuid = db.Column(db.Integer, primary_key=True)
    itemid = db.Column(db.Integer, primary_key=True)
    restaurantid = db.Column(db.String(64), primary_key=True)
    category = db.Column(db.String(64), nullable=False)
    itemname = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    image = db.Column(db.String(1024), nullable=False)

    def __init__(self, menuid, itemid, restaurantid, category, itemname, description, price, image):
        self.menuid = menuid
        self.itemid = itemid
        self.restaurantid = restaurantid
        self.category = category
        self.itemname = itemname
        self.description = description
        self.price = price
        self.image = image

    def json(self):
        return {"menuid": self.menuid, "itemid": self.itemid, "restaurantid": self.restaurantid, "category": self.category, "itemname": self.itemname, "description": self.description,  "price": self.price, "image": self.image}

# @app.route("/menu")
# def get_all():
#     menulist = menu.query.all()
#     if len(menulist):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "menus": [menu.json() for menu in menulist]
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "There are no books."
#         }
#     ), 404


@app.route("/menu/<string:restaurantid>")
def get_restaurantmenu(restaurantid):
    result = menu.query.filter_by(restaurantid=restaurantid).all()
    if len(result):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "menu": [menu1.json() for menu1 in  result]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such menu."
        }
    ), 404

if __name__ == '__main__':
    app.run(port=5005, debug=True) 