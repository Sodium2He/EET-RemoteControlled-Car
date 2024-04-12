# Directly download this file into your chip, main.py should run automatically as soon as the power is on.
import socket
import network
import pwm

# Wi-Fi settings, change them to yours!
wlanSSID = '8b2bnsd9g'
wlanPWD  = 'hje9cb3mi'

# UDP settings, change PORT to yours!
espPORT = 16384
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
    # sock.sendto()

    ''' 仅作演示，待后续实现
    if data:
      message = data.decode()  # 将bytes解码为字符串
      if ':' in message:
        parts = message.split(':')
        pin_number = int(parts[0])
        duty_cycle = int(parts[1])
        set_pwm(pin_number, duty_cycle)  # 调用pwm模块设置PWM
    '''
