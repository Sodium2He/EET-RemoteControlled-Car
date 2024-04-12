from flask import Flask, render_template, jsonify, request
  # modules for web server
import socket
  # modules for UDP connection

# UDP settings
# change IP & PORT to yours!
espIP = '192.168.1.10'
espPORT = 16384
sockAddr = (espIP, espPORT)
espSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # socket.AF_INET -> use IPv4; socket.SOCK_DGRAM -> UDP
espSocket.setblocking(0)

# flask
app = Flask(__name__)
@app.route("/")
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=25564, debug=True)

# udp
def sendUDPpackage(data):
  espSocket.sendto(data, sockAddr)

def recvUDPpackage():
  try:
    data, recvAddr = espSocket.recvfrom(1024)
  except socket.error:
    data, recvAddr = None, None
      # no packages received: return (None, None)
  return data, recvAddr