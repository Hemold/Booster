import RPi.GPIO as GPIO
import time

# Pin setup
PWM1 = 0
PWM2 = 2
DIR1 = 12
DIR2 = 13
DIR3 = 10
DIR4 = 11
QRE1113_PIN = 17  # Example pin for the QRE1113 sensor

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(QRE1113_PIN, GPIO.IN)  # Setup QRE1113_PIN as an input

# PWM setup (setting frequency to 100 Hz)
pwm1 = GPIO.PWM(PWM1, 100)
pwm2 = GPIO.PWM(PWM2, 100)

pwm1.start(0)  # Initialize with 0% duty cycle (stopped)
pwm2.start(0)

# Function to move forward
def forward(speed):
    GPIO.output(DIR1, GPIO.HIGH)  # Set motor 1 direction forward
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 direction forward
    GPIO.output(DIR3, GPIO.HIGH)  # Set motor 1 direction forward
    GPIO.output(DIR4, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left
def left(speed):
    GPIO.output(DIR1, GPIO.LOW)   # Set motor 1 reverse
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 forward
#    GPIO.output(DIR2, GPIO.LOW)   # Set motor 1 reverse
#    GPIO.output(DIR3, GPIO.HIGH)
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
    forward(100)  # Move forward at 50% speed
    time.sleep(2)

    left(100)  # Turn left at 50% speed
    time.sleep(2)

    right(100)  # Turn right at 50% speed
    time.sleep(2)

    # Sensor loop
#    while True:
#        sensor_value = GPIO.input(QRE1113_PIN)  # Read the sensor value
        
#        if sensor_value == GPIO.HIGH:
#            print("Reflective surface detected")  # Checks if a reflective surface is detected
#        else:
#            print("No reflective surface detected")
            
#        time.sleep(0.1)  # Short delay

finally:
    stop()  # Ensure GPIO cleanup when done
