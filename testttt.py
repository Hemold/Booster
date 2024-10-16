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

# Function to move forward with proportional speed adjustments
def forward_with_proportional_turn(venstre, højre, base_speed=50):
    # Move straight forward when both sensors are on the line
    if venstre == 0 and højre == 0:
        # Move straight forward when both sensors are on the line
        GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul
        GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul
        GPIO.output(DIR3, GPIO.LOW)   # højre hjul
        GPIO.output(DIR4, GPIO.LOW)   # venstre hjul
        pwm1.ChangeDutyCycle(base_speed)  # Set motor 1 speed (left wheel)
        pwm2.ChangeDutyCycle(base_speed)  # Set motor 2 speed (right wheel)
    elif venstre == 1 and højre == 0:
        # Proportionally reduce left motor speed, increase right motor speed
        GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul (move forward)
        GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul (move forward)
        GPIO.output(DIR3, GPIO.LOW)   # højre hjul (move forward)
        GPIO.output(DIR4, GPIO.LOW)   # venstre hjul (move forward)
        pwm1.ChangeDutyCycle(base_speed * 0.6)  # Slow down left motor
        pwm2.ChangeDutyCycle(base_speed)        # Keep right motor at base speed
    elif venstre == 0 and højre == 1:
        # Proportionally reduce right motor speed, increase left motor speed
        GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul (move forward)
        GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul (move forward)
        GPIO.output(DIR3, GPIO.LOW)   # højre hjul (move forward)
        GPIO.output(DIR4, GPIO.LOW)   # venstre hjul (move forward)
        pwm1.ChangeDutyCycle(base_speed)        # Keep left motor at base speed
        pwm2.ChangeDutyCycle(base_speed * 0.6)  # Slow down right motor
    elif venstre == 1 and højre == 1:
        # If both sensors are off the line, keep moving forward at base speed
        GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul (move forward)
        GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul (move forward)
        GPIO.output(DIR3, GPIO.LOW)   # højre hjul (move forward)
        GPIO.output(DIR4, GPIO.LOW)   # venstre hjul (move forward)
        pwm1.ChangeDutyCycle(base_speed)
        pwm2.ChangeDutyCycle(base_speed)
    else:
        GPIO.output(DIR1, GPIO.HIGH)  # Venstre hjul (move forward)
        GPIO.output(DIR2, GPIO.HIGH)  # Højre hjul (move forward)
        GPIO.output(DIR3, GPIO.LOW)   # højre hjul (move forward)
        GPIO.output(DIR4, GPIO.LOW)   # venstre hjul (move forward)
        pwm1.ChangeDutyCycle(base_speed)
        pwm2.ChangeDutyCycle(base_speed)

        pwm1.ChangeDutyCycle(base_speed)
        pwm2.ChangeDutyCycle(base_speed)

# Cleanup GPIO
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

# Main loop example
try:
    while True:
        venstre = GPIO.input(Sensor1_PIN)  # Read left sensor
        højre = GPIO.input(Sensor2_PIN)    # Read right sensor

        # Adjust speed proportionally based on sensor readings
        forward_with_proportional_turn(venstre, højre)

        time.sleep(0.05)  # Short delay for responsiveness
except KeyboardInterrupt:
    stop()
