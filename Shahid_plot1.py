from matplotlib.pyplot import *
from numpy import *

t= arange(1,3,0.01)
T= (6*log(t))-(7*exp(0.2*t))

figure(1)
clf()
plot(t,T)

xlabel('$Time$(min)')
ylabel('$Temperature$(C)')
title('$Shahid$-Plot')

savefig('myfig.png',dpi = 300)

show()

print ('Hello World! I just wrote my first python program. Yayyyyyyyy')
print ('Taha Shahid')


# LED Pinout test
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
pins = [17,18,27,22]
for i, pin in enumerate(pins):
GPIO.setup(pin, GPIO.OUT)
for j in range(i+1):
GPIO.output(pin,1)
time.sleep(0.5)
GPIO.output(pin,0)
time.sleep(0.5)
GPIO.cleanup()

