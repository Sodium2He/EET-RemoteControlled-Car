# Directly download this file into your chip, main.py should run automatically as soon as the power is on.
import socket
import network
#import pwm
import ujson

from machine import PWM,Pin
from time import sleep
servo=PWM(Pin(12),freq=50,duty=0)
pwm1=PWM(Pin(4),freq=50,duty=0)
pwm2=PWM(Pin(5),freq=50,duty=0)
def get_duty(direction):
   duty=(10/18)*direction
   return int(duty)

# Wi-Fi settings, change them to yours!
wlanSSID = '8b2bnsd9g'
wlanPWD  = 'hje9cb3mi'

# UDP settings, change PORT to yours!
espPORT = 65100
espSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wlanSSID, wlanPWD)
while not wlan.isconnected():
    pass
print('ESP8266> Network config:', wlan.ifconfig())

# setup UDP socket
espSocket.bind(('0.0.0.0', espPORT))
print('ESP8266> Listening on port %d' %espPORT)
 
# receive data through UDP
while True:
    data, sockAddr = espSocket.recvfrom(1024)
    print('ESP8266> from', sockAddr, 'Received:', data)
    json_data = ujson.loads(data)
    # sock.sendto()
    if data:
      #message = data.decode()
      key = json_data['key']
      status = json_data['status']
      if status == 1:
        if key == 's':
          pwm2.duty(get_duty(90))
          pwm1.duty(0)
          sleep(1)
        elif key == 'w':
          pwm1.duty(get_duty(60))
          pwm2.duty(0)
          sleep(1)
        elif status == 0:
          pwm1.duty(1023)
          pwm2.duty(1023)
          sleep(1) 
    break        


