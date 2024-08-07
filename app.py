from config import configuration
from src import init_app, init_socket

configuration = configuration['development']
app = init_app(configuration)
socketio = init_socket()

if __name__ == '__main__':
    socketio.run(app)
