# python 2
from __future__ import print_function
from urllib2 import urlopen

# python 3
# from urllib.request import urlopen
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)

def jump(ip='10.42.0.1'):
	content = urlopen('http://' + ip + ':3000/jump').read()
	print(content)

# Begin your code from here
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
# GPIO.add_event_detect(12, GPIO.RISING, callback=jump)
import time
while True:
    if(GPIO.input(12)):
    	jump()
    time.sleep(0.1)