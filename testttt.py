import RPi.GPIO as GPIO
import time


Sensor1_PIN = 37  # Vores sensor pin1
Sensor2_PIN = 35  # Vores sensor pin2

GPIO.setup(Sensor1_PIN, GPIO.IN)  # Sensor input
GPIO.setup(Sensor2_PIN, GPIO.IN)


try:
   while True:
        Venstre = int (GPIO.input(Sensor1_PIN))
        print(Venstre)
        Højre = int (GPIO.input(Sensor2_PIN))
        print(Højre)
        time.sleep(0.1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()