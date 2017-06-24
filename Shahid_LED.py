#Taha Shahid 1 2 3 LED

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin1=12
pin2=22
pin3=27

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

N=input("Enter Integer number from 1 to 3: ")
N=int(N)

if N == 1:
	GPIO.output(pin1,1)
	time.sleep(1)
	GPIO.output(pin1,0)
	time.sleep(0.5)
elif N == 2:
	GPIO.output(pin1,1)
	GPIO.output(pin2,1)
	time.sleep(1)
	GPIO.output(pin1,0)
	GPIO.output(pin2,0)
	time.sleep(0.5)
elif N == 3:
	GPIO.output(pin1,1)
        GPIO.output(pin2,1)
	GPIO.output(pin3,1)
	time.sleep(1)
	GPIO.output(pin1,0)
        GPIO.output(pin2,0)
	GPIO.output(pin3,0)
	time.sleep(0.5)
else:
	print("Cleanup")
	GPIO.cleanup()

