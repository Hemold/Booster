import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Pin setup
PWM1 = 11 # Blå, Venstre side
PWM2 = 13 # Lilla, Højre side

# Front
DIR1 = 26 # Venstre hjul
DIR2 = 24 # Højre hjul
# Bag
DIR3 = 19 # Hvid, højre hjul
DIR4 = 21  # Sort, venstre hjul

Sensor1_PIN = 31  # Vores sensor pin1
Sensor2_PIN = 29  # Vores sensor pin2
# GPIO setup

GPIO.setup(DIR1, GPIO.OUT)      #motor dir ourput
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)      #PWM output
GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(Sensor1_PIN, GPIO.IN)  # Sensor input
GPIO.setup(Sensor2_PIN, GPIO.IN)

# PWM setup (setting frequency to 100 Hz)
pwm1 = GPIO.PWM(PWM1, 1000)
pwm2 = GPIO.PWM(PWM2, 1000)

pwm1.start(0)  # Initialize with 0% duty cycle (stopped)
pwm2.start(0)

# Function to move forward
def forward():
    GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul
    GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul
    GPIO.output(DIR3, GPIO.LOW)  # højre hjul
    GPIO.output(DIR4, GPIO.LOW)  # venstre hjul
    pwm1.ChangeDutyCycle(45)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(45)   # Set motor 2 speed (0-100)

def backwards():
    GPIO.output(DIR1, GPIO.HIGH)  # Set motor 1 direction forward
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 direction forward.
    GPIO.output(DIR3, GPIO.LOW)  # Set motor 1 direction forward
    GPIO.output(DIR4, GPIO.LOW)
    pwm1.ChangeDutyCycle(100)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(100)   # Set motor 2 speed (0-100)

# Function to turn left
def left():
    GPIO.output(DIR1, GPIO.HIGH)   # Set motor 1 reverse
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 forward
    pwm1.ChangeDutyCycle(35)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(0)   # Set motor 2 speed (0-100)

# Function to turn right
def right():
    GPIO.output(DIR3, GPIO.LOW)  # Set motor 1 forward
    GPIO.output(DIR4, GPIO.LOW)   # Set motor 2 reverse
    pwm1.ChangeDutyCycle(0)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(35)   # Set motor 2 speed (0-100)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example

'''try:
   while True:
    Venstre = int (GPIO.input(Sensor1_PIN))
    print(Venstre)
    Højre = int (GPIO.input(Sensor2_PIN))
    print(Højre)
    if((Sensor1_PIN == 0) and (Sensor2_PIN == 1)):
        left()
    elif((Sensor1_PIN == 1) and (Sensor2_PIN == 0)):
        right()
    elif((Sensor1_PIN == 0) and (Sensor2_PIN == 0)):
        forward()
    elif((Sensor1_PIN == 1) and (Sensor2_PIN == 1)):
        forward()
    else:
        forward()
except KeyboardInterrupt:
  pass
GPIO.cleanup()
'''
try:
    while True:
        Venstre = GPIO.input(Sensor1_PIN)  # Read sensor 1 state
        Højre = GPIO.input(Sensor2_PIN)    # Read sensor 2 state
        
        if Venstre == 0 and Højre == 1:
            right()
        elif Venstre == 1 and Højre == 0:
            left()
        elif Venstre == 0 and Højre == 0:
            forward()
        elif Venstre == 1 and Højre == 1:
            forward()
        else:
            forward()
        time.sleep(0.1)  # Delay to prevent excessive CPU usage
except KeyboardInterrupt:
    stop()