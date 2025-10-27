import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

RST_PIN = 22

reader1 = SimpleMFRC522(0,0,1000000)

try:
    print("Place tag...")
    id = reader1.read()
    print(id[0])
finally:
    GPIO.cleanup()