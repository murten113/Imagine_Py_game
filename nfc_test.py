import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

RST_PIN = 22

reader1 = SimpleMFRC522(bus=0, device=0, pin_rst=RST_PIN)
reader2 = SimpleMFRC522(bus=1, device=0, pin_rst=RST_PIN)

try:
    print("Place tag...")
    id = reader1.read()
    print(id[0])
finally:
    GPIO.cleanup()