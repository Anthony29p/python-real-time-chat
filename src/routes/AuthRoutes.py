from flask import Blueprint, jsonify, redirect, request
from decouple import config
from src.services.AuthService import AuthService
main = Blueprint('auth_blueprint', __name__)


@main.route('/login', methods=['POST'])
def login():
    try:
        authorization_url = AuthService.login()
        return jsonify({'success': True, 'url': authorization_url})
    except Exception as e:
        print(e)


@main.route('/signup', methods=['POST'])
def signup():
    try:
        AuthService.signup("gato")
        return jsonify({'success': True, 'url': "signup"})
    except Exception as e:
        print(e)


@main.route('/oauth', methods=['GET'])
def oauth():
    try:
        code = request.args.get("code")
        AuthService.oauth(code)
        print("{}/messenger".format(config("FRONTEND_URL")))
    except Exception as e:
        print(e)

    return redirect("{}/messenger".format(config("FRONTEND_URL")))


