import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

leds = [2,3,4,17,27,22,10,9]

for i in range(8): GPIO.setup(leds[i], GPIO.OUT)

for j in range(3):
    for i in range(8):
        GPIO.output(leds[i],1)
        time.sleep(0.2)
        GPIO.output(leds[i],0)

for i in range(8): GPIO.output(leds[i],0)

GPIO.cleanup()