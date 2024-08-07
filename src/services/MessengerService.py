from flask_socketio import Namespace, emit
from flask import request


class MessengerService(Namespace):

    def on_connect(self):
        print('Client connected {}'.format(request.sid))

    def on_disconnect(self):
        print('Client disconnected {}'.format(request.sid))

    def on_message(self, data):
        try:
            current_socket_id = request.sid
            body = {"data": data, "id": current_socket_id}
            emit('message', body, broadcast=True)
            print('received message: ' + data)
        except:
            print("An unexpected error occurred")
