import RPi.GPIO as GPIO
import time

# Pin setup
PWM1 = 5
DIR1 = 4
PWM2 = 6
DIR2 = 7

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)

# PWM setup (setting frequency to 100 Hz)
pwm1 = GPIO.PWM(PWM1, 100)
pwm2 = GPIO.PWM(PWM2, 100)

pwm1.start(0)  # Initialize with 0% duty cycle (stopped)
pwm2.start(0)

# Function to move forward
def forward(speed):
    GPIO.output(DIR1, GPIO.HIGH)  # Set motor 1 direction forward
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 direction forward
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left
def left(speed):
    GPIO.output(DIR1, GPIO.LOW)   # Set motor 1 reverse
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 forward
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn right
def right(speed):
    GPIO.output(DIR1, GPIO.HIGH)  # Set motor 1 forward
    GPIO.output(DIR2, GPIO.LOW)   # Set motor 2 reverse
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example
try:
    forward(50)  # Move forward at 50% speed
    time.sleep(2)

    left(50)  # Turn left at 50% speed
    time.sleep(2)

    right(50)  # Turn right at 50% speed
    time.sleep(2)

finally:
    stop()