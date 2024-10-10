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
GPIO.setup(DIR1, GPIO.OUT)  # Motor direction output
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
def forward(speed=90):
    GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul
    GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul
    GPIO.output(DIR3, GPIO.LOW)   # Højre hjul
    GPIO.output(DIR4, GPIO.LOW)   # Venstre hjul
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left with variable speed
def turn_left(venstre_intensity):
    GPIO.output(DIR1, GPIO.HIGH)  # Motor 1 forward
    GPIO.output(DIR2, GPIO.HIGH)  # Motor 2 forward
    # Slow down left side, keep right side at normal speed
    pwm1.ChangeDutyCycle(50 * venstre_intensity)  # Left motor slower
    pwm2.ChangeDutyCycle(70)                      # Right motor faster

# Function to turn right with variable speed
def turn_right(højre_intensity):
    GPIO.output(DIR1, GPIO.HIGH)  # Motor 1 forward
    GPIO.output(DIR2, GPIO.HIGH)  # Motor 2 forward
    # Slow down right side, keep left side at normal speed
    pwm1.ChangeDutyCycle(70)                      # Left motor faster
    pwm2.ChangeDutyCycle(50 * højre_intensity)    # Right motor slower

# Adjust speed and direction based on sensor readings
def adjust_movement(venstre, højre):
    # No line detected, drive forward
    if venstre == 0 and højre == 0:
        forward(60)  # Move forward at a moderate speed
    
    # Line detected on the left, turn right
    elif venstre == 1 and højre == 0:
        turn_right(0.8)  # Adjust intensity if needed (0-1)
    
    # Line detected on the right, turn left
    elif venstre == 0 and højre == 1:
        turn_left(0.8)   # Adjust intensity if needed (0-1)
    
    # Line detected on both sides, slow down and go forward
    elif venstre == 1 and højre == 1:
        forward(30)      # Move slower forward when on the line

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

        # Adjust movement based on sensor readings
        adjust_movement(Venstre, Højre)

        time.sleep(0.05)  # Lowering delay for quicker response
except KeyboardInterrupt:
    stop()
