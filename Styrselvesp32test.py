from flask import Flask, request
import RPi.GPIO as GPIO
import time

# GPIO setup (same as before)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PWM1, PWM2 = 11, 13
DIR1, DIR2, DIR3, DIR4 = 26, 24, 19, 21
Sensor1_PIN, Sensor2_PIN = 31, 29

GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)

pwm1 = GPIO.PWM(PWM1, 1000)
pwm2 = GPIO.PWM(PWM2, 1000)
pwm1.start(0)
pwm2.start(0)

# Movement functions (same as before)
def forward(speed):
    GPIO.output(DIR1, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.HIGH)
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)

def left(speed):
    GPIO.output(DIR1, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)

def right(speed):
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.LOW)
    pwm2.ChangeDutyCycle(speed)

def backward(speed):
    GPIO.output(DIR1, GPIO.LOW)
    GPIO.output(DIR2, GPIO.LOW)
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)

def stop():
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)

# Flask server setup
app = Flask(__name__)

@app.route('/move', methods=['GET'])
def move():
    command = request.args.get('command')

    if command == 'forward':
        forward()
        return "Moving Forward"
    elif command == 'backward':
        backward()
        return "Moving Backward"
    elif command == 'left':
        left()
        return "Turning Left"
    elif command == 'right':
        right()
        return "Turning Right"
    elif command == 'stop':
        stop()
        return "Stopping"
    else:
        return "Unknown command"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
