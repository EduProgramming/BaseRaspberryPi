import pigpio
import sys

PIN_SERVO = 18
cmd = int(sys.argv[1])
servo = pigpio.pi()
servo.set_servo_pulsewidth(PIN_SERVO, cmd)