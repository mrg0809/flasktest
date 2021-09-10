from flask import Blueprint

calculator = Blueprint('calculator', __name__)

@calculator.route('/')
def index():
    return '<h1>Welcome</h1>'
