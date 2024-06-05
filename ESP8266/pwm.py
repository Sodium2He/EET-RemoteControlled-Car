from machine import PWM,Pin
from time import sleep
servo=PWM(Pin(12),freq=50,duty=0)#�?向控�?
pwm1=PWM(Pin(4),freq=50,duty=0)#两路pwm波控制前进方�?
pwm2=PWM(Pin(5),freq=50,duty=0)
def get_duty(direction):
   duty=(10/18)*direction
   return int(duty)

def control(press_houtui,press_qianjin,shache):
  if press_qianjin==1:
     pwm1.duty(get_duty(0))
     pwm2.duty(0)
     sleep(1)
  elif press_qianjin==2:
     pwm1.duty(get_duty(60))
     pwm2.duty(0)
     sleep(1) 
  elif press_qianjin==3:
     pwm1.duty(get_duty(120))
     pwm2.duty(0)
     sleep(1) 
  elif press_qianjin==4:
     pwm1.duty(get_duty(180))
     pwm2.duty(0)
     sleep(1) 
  elif press_houtui==1:
     pwm2.duty(get_duty(90))
     pwm1.duty(0)
     sleep(1) 
  elif shache==1:
     pwm1.duty(1023)
     pwm2.duty(1023)
     sleep(1) 
   
