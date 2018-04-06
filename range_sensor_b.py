import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 12 
ECHO = 18

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
         pulse_start = time.time()

    while GPIO.input(ECHO)==1:
         pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"
	
    r = requests.post("http://172.20.10.3:3000/obstacle", data={'distance': distance})
  
    print(r.status_code, r.reason)
    # GPIO.cleanup()

