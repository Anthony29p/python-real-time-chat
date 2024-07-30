from flask import Blueprint, jsonify, request
from decouple import config

main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    print(config('PORT')),
    return 'Hello World!'
