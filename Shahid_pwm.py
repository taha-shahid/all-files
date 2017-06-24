import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin=17
switch1_pin=18
switch2_pin=23

GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(switch1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

pwm_led = GPIO.PWM(led_pin,500)
duty=50
pwm_led.start(duty)

try:
	while True:
		0 < duty < 100
		if GPIO.input(switch1_pin)== 0:
			pwm_led.ChangeDutyCycle(duty)
			if duty < 100:
				duty=duty+5
			time.sleep(0.25)
			duty < 100
		if GPIO.input(switch2_pin)== 0:
			pwm_led.ChangeDutyCycle(duty)
			if duty > 0:
				duty=duty-5
			time.sleep(0.25)
			duty > 1
finally:
	print('Cleaning up')
	GPIO.cleanup()
