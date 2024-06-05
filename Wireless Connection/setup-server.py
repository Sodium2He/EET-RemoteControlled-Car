from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import socket

# UDP settings
# Change IP & PORT to your ESP8266's IP and port
espIP = '192.168.137.238'
espPORT = 65100
espAddr = (espIP, espPORT)
espSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
espSocket.setblocking(0)

# Web server config
app = Flask(__name__, template_folder='web', static_folder='web')
app.config['SECRET_KEY'] = 'secret!'
webSocketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

# Handling the WebSocket connection
@webSocketio.on('message')
def handleMessage(message):
    print(f"Received message: {message}")
    sendUDPpackage(message.encode('ascii'))  # Encode message to bytes

# UDP send function
def sendUDPpackage(data):
    espSocket.sendto(data, espAddr)

# UDP receive function
def recvUDPpackage():
    try:
        data, recvAddr = espSocket.recvfrom(1024)
    except socket.error:
        data, recvAddr = None, None
    return data, recvAddr

# Run server
if __name__ == '__main__':
    webSocketio.run(app, host='0.0.0.0', port=25564, debug=True)
