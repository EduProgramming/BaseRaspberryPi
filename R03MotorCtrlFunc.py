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

def motor_ctrl(is_left_front, is_right_front, is_left_stop, is_right_stop):
    if is_left_stop:
        GPIO.output(PIN_LEFT_MOTOR_FW, False)
        GPIO.output(PIN_LEFT_MOTOR_BW, False)
    else:
        GPIO.output(PIN_LEFT_MOTOR_FW, is_left_front)
        GPIO.output(PIN_LEFT_MOTOR_BW, not is_left_front)

    if is_right_stop:
        GPIO.output(PIN_RIGHT_MOTOR_FW, False)
        GPIO.output(PIN_RIGHT_MOTOR_BW, False)
    else:
        GPIO.output(PIN_RIGHT_MOTOR_FW, is_right_front)
        GPIO.output(PIN_RIGHT_MOTOR_BW, not is_right_front)

motor_ctrl(True, False, False, True)
time.sleep(3)
motor_ctrl(False, False, False, True)
time.sleep(3)
motor_ctrl(False, False, True, True)
time.sleep(1)
motor_ctrl(False, True, True, False)
time.sleep(3)
motor_ctrl(False, False, True, False)
time.sleep(3)
motor_ctrl(False, False, True, True)
time.sleep(1)

GPIO.cleanup()