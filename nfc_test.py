import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id = reader.read()
    print(id)
finally:
    GPIO.cleanup()