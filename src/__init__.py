from flask import Flask
from flask_socketio import SocketIO
from decouple import config
from .routes import IndexRoutes, AuthRoutes
from .services import MessengerService
from flask_cors import CORS

app = Flask(__name__)


def init_app(configuration):
    # Configuration
    app.config.from_object(configuration)
    CORS(app)
    cors = CORS(app, resource={
        r"/*": {
            "origins": config("FRONTEND_URL")
        }
    })


    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    return app


def init_socket():
    # Configuration
    socketio = SocketIO(app, cors_allowed_origins=config("FRONTEND_URL"))

    # Namespaces
    socketio.on_namespace(MessengerService.MessengerService('/'))

    return socketio
