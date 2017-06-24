#Moaz Nabeel LED with integer outputs

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_pin1=17
led_pin2=18
led_pin3=27
GPIO.setup(led_pin1,GPIO.OUT)
GPIO.setup(led_pin2,GPIO.OUT)
GPIO.setup(led_pin3,GPIO.OUT)
A=input("Enter any integer up till 3: ")
A=int(A)
if A == 1:
        GPIO.output(led_pin1,1)
        time.sleep(1)
        GPIO.output(led_pin1,1)
        time.sleep(0.25)
elif A == 2:
        GPIO.output(led_pin1,1)
        GPIO.output(led_pin2,1)
        time.sleep(1)
        GPIO.output(led_pin1,0)
        GPIO.output(led_pin2,0)
        time.sleep(0.25)
elif A == 3:
        GPIO.output(led_pin1,1)
        GPIO.output(led_pin2,1)
        GPIO.output(led_pin3,1)
        time.sleep(1)
        GPIO.output(led_pin1,0)
        GPIO.output(led_pin2,0)
        GPIO.output(led_pin3,0)
        time.sleep(0.25)
else:
        print("Errorrrrrrrrrrr")
        GPIO.cleanup()
