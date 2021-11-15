import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_LEFT_MOTOR_FW = 20
PIN_LEFT_MOTOR_BW = 21
PIN_RIGHT_MOTOR_FW = 16
PIN_RIGHT_MOTOR_BW = 26

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