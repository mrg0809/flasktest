from flask import Blueprint, render_template
from decimal import Decimal
from yandex_geocoder import Client

calculator = Blueprint('calculator', __name__)

client = Client("0dc2619f-d090-4dcc-85da-0446f3e3ccfd")

'''address = client.coordinates(c1)'''

@calculator.route('/')
def index():
    return render_template('index.html')

@calculator.route('/distance/<address>', methods=['GET'])
def distance(address):
    print(address)
    return '<h1>Welcome</h1>'