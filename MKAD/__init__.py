from flask import Flask
from .calculator.routes import calculator

def create_app():
    app = Flask(__name__)

    app.register_blueprint(calculator)

    return app
