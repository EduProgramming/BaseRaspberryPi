import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_LEFT_MOTOR_FW = 5
PIN_LEFT_MOTOR_BW = 6
PIN_RIGHT_MOTOR_FW = 22
PIN_RIGHT_MOTOR_BW = 23

GPIO.setup(PIN_LEFT_MOTOR_FW, GPIO.OUT)
GPIO.setup(PIN_LEFT_MOTOR_BW, GPIO.OUT)
GPIO.setup(PIN_RIGHT_MOTOR_FW, GPIO.OUT)
GPIO.setup(PIN_RIGHT_MOTOR_BW, GPIO.OUT)

GPIO.output(PIN_LEFT_MOTOR_FW, True)
GPIO.output(PIN_LEFT_MOTOR_BW, False)
time.sleep(3)
GPIO.output(PIN_LEFT_MOTOR_FW, False)
GPIO.output(PIN_LEFT_MOTOR_BW, True)
time.sleep(3)
GPIO.output(PIN_LEFT_MOTOR_FW, False)
GPIO.output(PIN_LEFT_MOTOR_BW, False)
time.sleep(1)
GPIO.output(PIN_RIGHT_MOTOR_FW, True)
GPIO.output(PIN_RIGHT_MOTOR_BW, False)
time.sleep(3)
GPIO.output(PIN_RIGHT_MOTOR_FW, False)
GPIO.output(PIN_RIGHT_MOTOR_BW, True)
time.sleep(3)
GPIO.output(PIN_RIGHT_MOTOR_FW, False)
GPIO.output(PIN_RIGHT_MOTOR_BW, False)
time.sleep(1)

GPIO.cleanup()