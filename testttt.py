import RPi.GPIO as GPIO
import time
 
# Define valid GPIO pins for line followers
linefollower1 = 27  # GPIO27 (Physical Pin 13)
linefollower2 = 22  # GPIO22 (Physical Pin 15)
 
# Suppress warnings
GPIO.setwarnings(False)
 
# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
 
# Setup GPIO pins as input with pull-down resistors
GPIO.setup(linefollower1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(linefollower2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
try:
    while True:
        # Read sensor values
        Venstre = GPIO.input(linefollower1)
        Hoejre = GPIO.input(linefollower2)
        # Print sensor states
        print(f"Venstre (GPIO {linefollower1}): {'HIGH' if Venstre else 'LOW'}, "
              f"Højre (GPIO {linefollower2}): {'HIGH' if Hoejre else 'LOW'}")
        # Short delay
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()