import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    try:
        pass
    except KeyboardInterrupt:
        GPIO.cleanup()