import RPi.GPIO as GPIO
import time

pin_led = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

pwm_led = GPIO.PWM(pin_led, 50)
pwm_led.start(100)

for power in range(101):
    pwm_led.ChangeDutyCycle(power)
    time.sleep(0.1)

for power in range(100, -1, -1):
    pwm_led.ChangeDutyCycle(power)
    time.sleep(0.1)

GPIO.cleanup()