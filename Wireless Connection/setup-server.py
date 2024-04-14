from flask import Flask, render_template
  # modules for web server
from flask_socketio import SocketIO, send, emit
  # for WebSocket
import socket
  # modules for UDP connection (ESP8266)

# UDP settings
# change IP & PORT to yours!
espIP = '192.168.1.10'
espPORT = 16384
espAddr = (espIP, espPORT)
espSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # socket.AF_INET -> use IPv4; socket.SOCK_DGRAM -> UDP
espSocket.setblocking(0)

# web server config
app = Flask(__name__)
webSocketio = SocketIO(app)
@app.route("/")
def index(): # web
  return render_template('index.html')

# handling the WebSocket connection
@webSocketio.on('message')
def handleMessage(message):
  sendUDPpackage(message)

#run server
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=25564, debug=True)

# udp
def sendUDPpackage(data):
  espSocket.sendto(data, espAddr)

def recvUDPpackage():
  try:
    data, recvAddr = espSocket.recvfrom(1024)
  except socket.error:
    data, recvAddr = None, None
      # no packages received: return (None, None)
  return data, recvAddr