import socket
import network
import ujson

from machine import PWM, Pin
from time import sleep

# Initialize PWM
servo = PWM(Pin(12), freq=50, duty=0)
pwm1 = PWM(Pin(4), freq=50, duty=0)
pwm2 = PWM(Pin(5), freq=50, duty=0)

def get_duty(direction):
    duty = (10 / 18) * direction
    return int(duty)

# Wi-Fi settings, change them to yours!
wlanSSID = '8b2bnsd9g'
wlanPWD = 'hje9cb3mi'

# UDP settings, change PORT to yours!
espPORT = 65113
espSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wlanSSID, wlanPWD)
while not wlan.isconnected():
    pass
print('ESP8266> Network config:', wlan.ifconfig())

# Setup UDP socket
espSocket.bind(('0.0.0.0', espPORT))
print('ESP8266> Listening on port %d' % espPORT)

flag = 1
# Ensure resources are released properly
try:
    # Receive data through UDP
    while flag:
        data, sockAddr = espSocket.recvfrom(1024)
        temp_data = data.decode('ascii')
        print('ESP8266> from', sockAddr, 'Received:', temp_data)
        json_data = ujson.loads(temp_data)
        if data:
            key = json_data['key']
            status = json_data['status']
            print(key, status)
            if key == 'x' and status == 1:
                print('exit')
                flag = 0
                break
            if status == 1:
                if key == 's':
                    print('on s')
                    pwm2.duty(1024)#get_duty(90)
                    pwm1.duty(0)
                    sleep(0.05)
                elif key == 'w':
                    print('on w')
                    pwm1.duty(1024)#get_duty(60)
                    pwm2.duty(0)
                    sleep(0.05)
            elif status == 0:
                print('on [_]')
                pwm1.duty(1023)
                pwm2.duty(1023)
                sleep(0.05)
finally:
    # Release resources
    espSocket.close()
    print('ESP8266> Socket closed')

