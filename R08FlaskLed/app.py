import RPi.GPIO as GPIO
import time
from flask import Flask, render_template

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

PIN_LED = 12

GPIO.setup(PIN_LED, GPIO.OUT)

@app.route('/')
def index():
    return "INDEX"

@app.route('/<int:value>')
def get_int(value):
    return f"숫자로 인식{value}"

@app.route('/<string:state>')
def get_string(state):
    if state.lower() == 'on':
        GPIO.output(PIN_LED, True)
    elif state.lower() == 'off':
        GPIO.output(PIN_LED, False)
    return state

if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        GPIO.cleanup()