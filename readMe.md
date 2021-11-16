# Raspberry Pi 3B+

라즈베리파이 3B+을 이용하여 IoT CCTV RC Car을 만들어 봅시다.


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