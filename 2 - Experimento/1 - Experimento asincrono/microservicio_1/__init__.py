from flask import Flask
from celery import Celery

def create_app(config_name):
    app = Flask(__name__)
    return app