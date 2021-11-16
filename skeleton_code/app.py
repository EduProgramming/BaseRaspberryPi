from importlib import import_module
from flask import Flask, render_template, Response, request, jsonify
import RPi.GPIO as GPIO
import time, json
import os

if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_cctv import Camera

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Setting Pin Variable
LEFT_MOTOR_FW = 20
LEFT_MOTOR_BW = 21
RIGHT_MOTOR_FW = 16
RIGHT_MOTOR_BW = 26

speed = 0

# Setting PinMode
GPIO.setup(LEFT_MOTOR_FW, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_BW, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FW, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_BW, GPIO.OUT)

# Setting Global Variable
angle = START_ANGLE = 1500

left_fw_speed = GPIO.PWM(LEFT_MOTOR_FW, 50) #PinNumber, 50Hz
left_bw_speed = GPIO.PWM(LEFT_MOTOR_BW, 50)
right_fw_speed = GPIO.PWM(RIGHT_MOTOR_FW, 50)
right_bw_speed = GPIO.PWM(RIGHT_MOTOR_BW, 50)

left_fw_speed.start(0)
left_bw_speed.start(0)
right_fw_speed.start(0)
right_bw_speed.start(0)

@app.route('/')
def index():
    global angle
    angle = START_ANGLE
    os.system(f'sudo python3 servo_ctrl.py {START_ANGLE}')
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/motor_forward')
def motor_forward():
    # Forward: ChangeDutyCycle
    return jsonify({"result": True})

@app.route('/motor_turn_left')
def motor_turn_left():
    # Turn Left
    return jsonify({"result": True})

@app.route('/motor_turn_right')
def motor_turn_right():
    # Turn Right
    return jsonify({"result": True})

@app.route('/motor_backward')
def motor_backward():
    # Backward
    return jsonify({"result": True})

@app.route('/motor_stop')
def motor_stop():
    # Stop
    return jsonify({"result": True})

@app.route('/setting_motor_speed', methods=['POST'])
def setting_motor_speed():
    data = json.loads(request.get_data(), encoding='utf-8')
    speed = data.get('speed', 0)
    speed = max(speed, 0)
    speed = min(speed, 100)
    return jsonify({"result": True})

@app.route('/cctv_move_left', methods=['POST'])
def cctv_move_left():
    global angle
    data = json.loads(request.get_data(), encoding='utf-8')
    if data.get('state') == True:
        angle = 2500
    else:
        angle += 250
        angle = 2500 if angle > 2500 else angle
    os.system(f'sudo python3 servo_ctrl.py {angle}')
    time.sleep(0.5)
    return jsonify({"result": True})

@app.route('/cctv_move_right', methods=['POST'])
def cctv_move_right():
    global angle
    data = json.loads(request.get_data(), encoding='utf-8')
    if data.get('state') == True:
        angle = 500
    else:
        angle -= 250
        angle = 500 if angle < 500 else angle
    os.system(f'sudo python3 servo_ctrl.py {angle}')
    time.sleep(0.5)
    return jsonify({"result": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)