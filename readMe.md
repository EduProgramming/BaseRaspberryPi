# Raspberry Pi 3B+

라즈베리파이 3B+을 이용하여 IoT CCTV RC Car을 만들어 봅시다.



## :warning:사용방법과 공지사항

교육 시간이 한정되어 설명하지 못했던 부분을 잠시 이 공간을 통해 공지합니다.

해당 공지사항은 12월이 되었을 때 내릴 예정입니다.

교육장에서 다운받은 파일을 통해서는 RC카 기능을 할 수 없습니다.

안되는 이유는 교육장에서 설명드렸기에 넘어가도록 하겠습니다.



먼저, 최종파일을 다운받아서 실행하는 방법을 기재하겠습니다.

파일이 다운받아있지 않다고 가정했을 때 해당 부분을 라즈베리파이 터미널에 작성해주시면 됩니다.

```bash
git clone https://github.com/EduProgramming/BaseRaspberryPi.git
```

해당 부분을 실행하셨다면 폴더명이 `BaseRaspberryPi`라고 생성되게 됩니다. 안에는 github 사이트 주소에서 봤던 파일들이 있는 것을 확인하실 수 있습니다.



파일이 있는 분들은 여기서부터 진행해주시면 됩니다.

```bash
cd ~/BaseRaspberryPi/final
```

이렇게 작성하시면 최종소스를 실행할 수 있는 경로로 터미널이 움직이게 됩니다.



실행을 시켜보도록 하겠습니다.

```bash
sudo pigpiod
sudo python3 app.py
```



:rotating_light:**RC카 이동방향이 전진을 눌렀는데 다른 방향으로 갈 때 해결방안**

정말 쉬운 방안으로 설명드리겠습니다.

`app.py` 내용을 보게 되면 아래와 같은 내용이 있습니다.

```python
@app.route('/motor_forward')
def motor_forward():
    global speed
    left_bw_speed.ChangeDutyCycle(0)
    right_bw_speed.ChangeDutyCycle(0)
    left_fw_speed.ChangeDutyCycle(speed)
    right_fw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_turn_left')
def motor_turn_left():
    global speed
    left_fw_speed.ChangeDutyCycle(0)
    right_bw_speed.ChangeDutyCycle(0)
    left_bw_speed.ChangeDutyCycle(speed)
    right_fw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_turn_right')
def motor_turn_right():
    global speed
    left_bw_speed.ChangeDutyCycle(0)
    right_fw_speed.ChangeDutyCycle(0)
    left_fw_speed.ChangeDutyCycle(speed)
    right_bw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_backward')
def motor_backward():
    global speed
    left_fw_speed.ChangeDutyCycle(0)
    right_fw_speed.ChangeDutyCycle(0)
    left_bw_speed.ChangeDutyCycle(speed)
    right_bw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})
```

route의 내용만 바꿔서 처리하면 됩니다.

예를 들어서 왼쪽버튼을 눌렀는데 오른쪽으로 가고, 오른쪽 버튼을 누르면 왼쪽으로 간다고 하겠습니다.

그러면 위의 소스를 아래와 같이 변경하시면 쉽게 됩니다.



```python
@app.route('/motor_forward')
def motor_forward():
    global speed
    left_bw_speed.ChangeDutyCycle(0)
    right_bw_speed.ChangeDutyCycle(0)
    left_fw_speed.ChangeDutyCycle(speed)
    right_fw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_turn_right')
def motor_turn_left():
    global speed
    left_fw_speed.ChangeDutyCycle(0)
    right_bw_speed.ChangeDutyCycle(0)
    left_bw_speed.ChangeDutyCycle(speed)
    right_fw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_turn_left')
def motor_turn_right():
    global speed
    left_bw_speed.ChangeDutyCycle(0)
    right_fw_speed.ChangeDutyCycle(0)
    left_fw_speed.ChangeDutyCycle(speed)
    right_bw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})

@app.route('/motor_backward')
def motor_backward():
    global speed
    left_fw_speed.ChangeDutyCycle(0)
    right_fw_speed.ChangeDutyCycle(0)
    left_bw_speed.ChangeDutyCycle(speed)
    right_bw_speed.ChangeDutyCycle(speed)
    return jsonify({"result": True})
```

`@app.route('/motor_turn_right')`와 `@app.route('/motor_turn_left')`을 바꿨습니다.

함수이름과 같이 않아서 조금 와닿진 않지만 작동에는 이상없이 수정이 됩니다.




## Raspberry GPIO

### R01

라즈베리파이를 이용한 LED 제어

### R02

라즈베리파이를 이용한 DC 모터 제어(with Motor Driver)

### R03

라즈베리파이를 이용한 DC 모터 제어(With Motor Driver, Python Function)

### R04

라즈베리파이에서 `pigpiod` 서버를 이용하여 서버모터 제어

해당 방안을 이용하는 이유는 지터링을 방지하기 위해서 입니다.

GPIO에서 바로 제어하면 지터링 현상이 간혹 발생합니다.

```bash
# install library
sudo apt-get install pigpio python-pigpio python3-pigpio

# Run Code
sudo pigpiod
sudo python3 R04ServoCtrl.py
```

#### R04ServoBase

GPIO PWM을 통한 서보모터 제어
단점, 연산작업에 특화되어 있지 않아 -> 지터링이 발생함

#### R04ServoCtrl

지터링을 방지하기 위해서 `pigpiod` 서버를 구동하여 위의 문제를 해결한 방식

### R07LedPwm

라즈베리파이 GPIO 제어를 통한 PWM 제어
주파수는 기본적으로 50Hz를 사용하는데 사용하는 특성 센서모듈마다 상이할 수 있음

## Hello, Flask :snake:

### R05HelloFlask

Hello, Flask
가장 기본적인 Flask 소스 실행

### R06HelloFlask

flask의 `render_template` 함수를 이용한 html과 연결
해당 방안을 사용하여 html, css, js를 이용하여 서버를 꾸미고 동작을 넣어 원하는 웹 사이트를 구성하면 됨

- html: 골격
- css: 살 붙이기(디지인)
- js: 액션/동작


### R08FlaskLed

flask를 이용하여 웹 서버와 GPIO 연결
URL 주소에 어떠한 값이 오느냐에 따라 보여지는 값과 LED제어가 가능하게 설정

- /on: 12번 LED ON
- /off: 12번 LED OFF

`<>` 기법을 이용하여 동적 Route가 되게 설정함


<hr/>

## Fianl

### Skeleton Code

모터 PWM 제어를 통한 방향 제어 부분을 빼놓음

해당 부분을 채워서 진행하면 Final Code와 같음

### Final

최종 소스