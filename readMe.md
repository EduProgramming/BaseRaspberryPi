# Raspberry Pi 3B+

라즈베리파이 3B+을 이용하여 IoT CCTV RC Car을 만들어 봅시다.


## Index

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

### R05

Hello, Flask

### R06

Flask와 HTML 연동

Hello, Flask templates
