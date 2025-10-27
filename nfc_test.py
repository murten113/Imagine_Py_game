import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id = reader.read()
    x = id.split(",")
    x1 = x[0].split("(")
    x2 = x1[1]
    print(x2)
finally:
    GPIO.cleanup()