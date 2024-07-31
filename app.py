from flask_socketio import SocketIO, emit
from flask import request
from decouple import config
from config import configuration
from src import init_app

configuration = configuration['development']
app = init_app(configuration)

socketio = SocketIO(app, cors_allowed_origins=config("FRONTEND_URL"))


@socketio.on('message')
def handle_message(data):
    current_socket_id = request.sid
    body = {"data": data, "id": current_socket_id}
    emit('message', body, broadcast=True)
    print('received message: ' + data)


if __name__ == '__main__':
    socketio.run(app)
