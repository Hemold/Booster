import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin setup
PWM1 = 11  # Blå, Venstre side
PWM2 = 13  # Lilla, Højre side

# Front
DIR1 = 26  # Venstre hjul
DIR2 = 24  # Højre hjul
# Bag
DIR3 = 19  # Hvid, højre hjul
DIR4 = 21  # Sort, venstre hjul

Sensor1_PIN = 31  # Vores sensor pin1
Sensor2_PIN = 29  # Vores sensor pin2

# GPIO setup
GPIO.setup(DIR1, GPIO.OUT)  # Motor dir output
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)  # PWM output
GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(Sensor1_PIN, GPIO.IN)  # Sensor input
GPIO.setup(Sensor2_PIN, GPIO.IN)

# PWM setup (setting frequency to 1000 Hz)
pwm1 = GPIO.PWM(PWM1, 1000)
pwm2 = GPIO.PWM(PWM2, 1000)

pwm1.start(0)  # Initialize with 0% duty cycle (stopped)
pwm2.start(0)

# Function to move forward
def forward(speed):
    GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul
    GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul
    GPIO.output(DIR3, GPIO.LOW)  # højre hjul
    GPIO.output(DIR4, GPIO.LOW)  # venstre hjul
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left
def left(speed):
    GPIO.output(DIR1, GPIO.HIGH)   # Set motor 1 reverse
    GPIO.output(DIR2, GPIO.HIGH)   # Set motor 2 forward
    pwm1.ChangeDutyCycle(speed)    # Set motor 1 speed (0-100)

# Function to turn right
def right(speed):
    GPIO.output(DIR3, GPIO.LOW)    # Set motor 1 forward
    GPIO.output(DIR4, GPIO.LOW)    # Set motor 2 reverse
    pwm2.ChangeDutyCycle(speed)    # Set motor 2 speed (0-100)


# Adjust speed based on sensor readings
def adjust_speed(venstre, højre):
    if venstre == 0 and højre == 0:
        forward(100)  # Move forward at a moderate speed
    elif venstre == 1 and højre == 1:
        forward(100)  # Slow down when both sensors are triggered
    elif venstre == 0 and højre == 1:
        right(100)    # Turn right
        left(35)
        time.sleep(0.1)
    elif venstre == 1 and højre == 0:
        right(35)
        left(100)     # Turn left
        time.sleep(0.1)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example
try:
    while True:
        Venstre = GPIO.input(Sensor1_PIN)  # Read sensor 1 state
        Højre = GPIO.input(Sensor2_PIN)    # Read sensor 2 state

        # Adjust speed based on sensor readings
        adjust_speed(Venstre, Højre)
except KeyboardInterrupt:
    stop()