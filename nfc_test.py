import RPi.GPIO as GPIO
from mfrc522 import MFRC522

RST_PIN = 22  # Reset (Shared for all modules)
reader1 = MFRC522(bus=0, device=0, pin_mode=24, pin_rst=RST_PIN)

try:
    print("Place tag...")
    status1, TagType1 = reader1.MFRC522_Request(reader1.PICC_REQIDL)
    if status1 == reader1.MI_OK:
        print("1 yes")
    print("klaar")
finally:
    GPIO.cleanup()