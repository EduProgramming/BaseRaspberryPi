import RPi.GPIO as GPIO
import time

PIN_SERVO = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_SERVO, GPIO.OUT)
servo = GPIO.PWM(PIN_SERVO, 50)

servo.start(0)


servo.ChangeDutyCycle(2.5) # 0 angle
time.sleep(1)

servo.ChangeDutyCycle(12.5) # 180 angle
time.sleep(1)

servo.ChangeDutyCycle(7.5) # 90 angle
time.sleep(1)

servo.stop()
GPIO.cleanup()

"""
try:
    # run code
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
"""
