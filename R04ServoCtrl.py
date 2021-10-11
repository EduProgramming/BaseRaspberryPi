import pigpio
import time

PIN_SERVO = 18

servo = pigpio.pi()
servo.set_servo_pulsewidth(PIN_SERVO, 1500)
time.sleep(1)
servo.set_servo_pulsewidth(PIN_SERVO, 2400)
time.sleep(1)
servo.set_servo_pulsewidth(PIN_SERVO, 600)
time.sleep(1)
servo.set_servo_pulsewidth(PIN_SERVO, 1500)
time.sleep(1)