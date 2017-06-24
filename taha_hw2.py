import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
p1=4
p2=17
p3=18
p4=27

GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)
GPIO.setup(p3,GPIO.OUT)
GPIO.setup(p4,GPIO.OUT)

try:
        GPIO.output(p1,1)
        time.sleep(0.5)
        GPIO.output(p1,0)
        time.sleep(0.5)
        GPIO.output(p2,1)
        time.sleep(0.5)
        GPIO.output(p2,0)
        time.sleep(0.5)
        GPIO.output(p3,1)
        time.sleep(0.5)
        GPIO.output(p3,0)
        time.sleep(0.5)
        GPIO.output(p4,1)
        time.sleep(0.5)
        GPIO.output(p4,0)
        time.sleep(0.25)
        GPIO.output(p4,1)
        time.sleep(0.5)
        GPIO.output(p4,0)
        time.sleep(0.5)
        GPIO.output(p3,1)
        time.sleep(0.5)
        GPIO.output(p3,0)
        time.sleep(0.5)
        GPIO.output(p2,1)
        time.sleep(0.5)
        GPIO.output(p2,0)
        time.sleep(0.5)
        GPIO.output(p1,1)
        time.sleep(0.5)
        GPIO.output(p1,0)
        time.sleep(0.5)

finally:
        print("Cleaning Up!")
        GPIO.cleanup()
