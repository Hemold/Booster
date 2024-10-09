import RPi.GPIO as GPIO
import time

# Pin setup
PWM1 = 0
PWM2 = 2
DIR1 = 12
DIR2 = 13
DIR3 = 10
NY_DIR3 = 19
DIR4 = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)

pi_PWM1 = GPIO.PWM(PWM1, 1000)
pi_PWM1.start(0)
pi_PWM2 = GPIO.PWM(PWM2, 1000)
pi_PWM2.start(0)

def koer():
    GPIO.output(DIR1, True)
    GPIO.output(DIR2, True)			

    GPIO.output(DIR3, True)
    GPIO.output(DIR4, True)
    
    pi_PWM1.ChangeDutyCycle(100)
    pi_PWM2.ChangeDutyCycle(100)

def dven():
		

    GPIO.output(DIR1, True)
    GPIO.output(DIR2, True)			

    GPIO.output(DIR3, True)
    GPIO.output(DIR4, True)

    pi_PWM1.ChangeDutyCycle(100)
    pi_PWM2.ChangeDutyCycle(0)

def dhoej():

    GPIO.output(DIR1, True)
    GPIO.output(DIR2, True)			

    GPIO.output(DIR3, True)
    GPIO.output(DIR4, True)

    pi_PWM1.ChangeDutyCycle(0)
    pi_PWM2.ChangeDutyCycle(100)

koer()
dven()
dhoej()
