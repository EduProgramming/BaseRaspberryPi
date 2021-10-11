import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_LED = 26

GPIO.setup(PIN_LED, GPIO.OUT)

GPIO.output(PIN_LED, True)
time.sleep(5)
GPIO.output(PIN_LED, False)

GPIO.cleanup()