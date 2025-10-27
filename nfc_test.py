import RPi.GPIO as GPIO
from mfrc522 import MFRC522

reader = MFRC522()

try:
    print("Place tag...")
    id = reader.read()
    print(id[0])
finally:
    GPIO.cleanup()