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

Sensor1_PIN = 31  # Vores sensor pin1 (Left)
Sensor2_PIN = 29  # Vores sensor pin2 (Right)

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
    GPIO.output(DIR3, GPIO.LOW)   # højre hjul
    GPIO.output(DIR4, GPIO.LOW)   # venstre hjul
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left
def left(speed):
    GPIO.output(DIR1, GPIO.HIGH)   # Set motor 1 forward
    GPIO.output(DIR2, GPIO.HIGH)   # Set motor 2 forward
    pwm1.ChangeDutyCycle(speed)    # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(0)        # Set motor 2 speed to 0 (stop right motor)

# Function to turn right
def right(speed):
    GPIO.output(DIR3, GPIO.LOW)    # Set motor 1 forward
    GPIO.output(DIR4, GPIO.LOW)    # Set motor 2 forward
    pwm1.ChangeDutyCycle(0)        # Set motor 1 speed to 0 (stop left motor)
    pwm2.ChangeDutyCycle(speed)    # Set motor 2 speed (0-100)

# Proportional turn based on sensor input
def smooth_turn(venstre, højre):
    if venstre > højre:
        pwm1.ChangeDutyCycle(100 - venstre * 100)  # Adjust left motor slower
        pwm2.ChangeDutyCycle(70)                   # Right motor runs normally
    elif højre > venstre:
        pwm1.ChangeDutyCycle(70)                   # Left motor runs normally
        pwm2.ChangeDutyCycle(100 - højre * 100)    # Adjust right motor slower

# Adjust speed based on sensor readings
def adjust_speed(venstre, højre):
    if venstre == 0 and højre == 0:
        forward(90)  # Move forward at a moderate speed
    elif venstre == 1 and højre == 1:
        forward(90)  # Move forward if both sensors detect line (e.g., centering)
    elif venstre == 0 and højre == 1:
        right(70)    # Turn right if right sensor detects line
        time.sleep(0.1)
    elif venstre == 1 and højre == 0:
        left(70)     # Turn left if left sensor detects line
        time.sleep(0.1)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example
try:
    while True:
        Venstre = GPIO.input(Sensor1_PIN)  # Read left sensor state
        Højre = GPIO.input(Sensor2_PIN)    # Read right sensor state

        # Adjust speed based on sensor readings
        adjust_speed(Venstre, Højre)

        time.sleep(0.05)  # Lowering delay for better responsiveness
except KeyboardInterrupt:
    stop()
