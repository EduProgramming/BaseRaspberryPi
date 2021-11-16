from flask import Flask, render_template, Response, request, jsonify
import time, json
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/motor_forward')
def motor_forward():
    print('FORWARD')
    return jsonify({"result": True})

@app.route('/motor_turn_left')
def motor_turn_left():
    print('TURN_LEFT')
    return jsonify({"result": True})

@app.route('/motor_turn_right')
def motor_turn_right():
    print('TURN_RIGHT')
    return jsonify({"result": True})

@app.route('/motor_backward')
def motor_backward():
    print('BACKWARD')
    return jsonify({"result": True})

@app.route('/cctv_move_left', methods=['POST'])
def cctv_move_left():
    print(json.loads(request.get_data(), encoding='utf-8'))
    time.sleep(3)
    return jsonify({"result": True})

@app.route('/cctv_move_right', methods=['POST'])
def cctv_move_right():
    print(json.loads(request.get_data(), encoding='utf-8'))
    time.sleep(3)
    return jsonify({"result": True})

@app.route('/motor_stop')
def motor_stop():
    print('MOTOR_STOP')
    return jsonify({"result": True})

@app.route('/setting_motor_speed', methods=['POST'])
def setting_motor_speed():
    print(json.loads(request.get_data(), encoding='utf-8'))
    return jsonify({"result": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)