import RPi.GPIO as GPIO
import time

# Pin setup
PWM1 = 17 # Blå, Venstre side
PWM2 = 15 # Lilla, Højre side

# Front
DIR1 = 26 # Venstre hjul
DIR2 = 24 # Højre hjul
# Bag
DIR3 = 19 # Hvid, højre hjul
DIR4 = 21  # Sort, venstre hjul

Sensor1_PIN = 37  # Vores sensor pin1
Sensor2_PIN = 35  # Vores sensor pin2
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)      #motor dir ourput
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)      #PWM output
GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(Sensor1_PIN, GPIO.IN)  # Sensor input
GPIO.setup(Sensor2_PIN, GPIO.IN)

# PWM setup (setting frequency to 100 Hz)
pwm1 = GPIO.PWM(PWM1, 100)
pwm2 = GPIO.PWM(PWM2, 100)

pwm1.start(0)  # Initialize with 0% duty cycle (stopped)
pwm2.start(0)

# Function to move forward
def forward(speed):
    GPIO.output(DIR1, GPIO.LOW)  # Venstre hjul
    GPIO.output(DIR2, GPIO.LOW)  # Højre hjul
    GPIO.output(DIR3, GPIO.HIGH)  # højre hjul
    GPIO.output(DIR4, GPIO.HIGH)  # venstre hjul
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

def backwards(speed):
    GPIO.output(DIR1, GPIO.HIGH)  # Set motor 1 direction forward
    GPIO.output(DIR2, GPIO.HIGH)  # Set motor 2 direction forward
    GPIO.output(DIR3, GPIO.LOW)  # Set motor 1 direction forward
    GPIO.output(DIR4, GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn left
def left(speed):
    GPIO.output(DIR1, GPIO.LOW)   # Set motor 1 reverse
    GPIO.output(DIR2, GPIO.LOW)  # Set motor 2 forward
#    GPIO.output(DIR2, GPIO.LOW)   # Set motor 1 reverse
#    GPIO.output(DIR3, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Function to turn right
def right(speed):
    GPIO.output(DIR3, GPIO.HIGH)  # Set motor 1 forward
    GPIO.output(DIR4, GPIO.HIGH)   # Set motor 2 reverse
    pwm1.ChangeDutyCycle(speed)   # Set motor 1 speed (0-100)
    pwm2.ChangeDutyCycle(speed)   # Set motor 2 speed (0-100)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example

linefollower1 = 31      #pin for ventre sensor
linefollower2 = 29      #pin for højre sensor


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(linefollower1,GPIO.IN)
GPIO.setup(linefollower2,GPIO.IN)

try:
   while True:
    forward(75)
    Venstre = int (GPIO.input(linefollower1))
    print(Venstre)
    Højre = int (GPIO.input(linefollower2))
    print(Højre)
except KeyboardInterrupt:
  pass
finally:
    GPIO.cleanup()
    stop()  # Ensure GPIO cleanup when done