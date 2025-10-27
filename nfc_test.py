import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id,text = reader.read()
    print(id)
    print(str(text) + "ey")
finally:
    GPIO.cleanup()