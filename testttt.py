import RPi.GPIO as GPIO
import time

linefollower1 = 24
linefollower2 = 25


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(linefollower1,GPIO.IN)
GPIO.setup(linefollower2,GPIO.IN)
try:
   while True:
        Venstre = GPIO.input(linefollower1)
        print(Venstre)
        Hoejre = GPIO.input(linefollower2)
        print(Hoejre)
        time.sleep(0.1)
except KeyboardInterrupt:
  pass
finally:
    GPIO.cleanup()

