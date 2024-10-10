import RPi.GPIO as GPIO
import time


Sensor1_PIN = 24  # Vores sensor pin1
Sensor2_PIN = 25  # Vores sensor pin2
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor1_PIN, GPIO.IN)  # Sensor input
GPIO.setup(Sensor2_PIN, GPIO.IN)


while True:
    Venstre = int (GPIO.input(Sensor1_PIN))
    Højre = int (GPIO.input(Sensor2_PIN))
    print(Venstre) 
    print(Højre)
    time.sleep(0.1)
    Venstre = 0
    Højre = 0
#    GPIO.cleanup()


