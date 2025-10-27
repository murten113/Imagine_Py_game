import RPi.GPIO as GPIO
from mfrc522 import NewSimpleMFRC522

RST_PIN = 22  # Reset (Shared for all modules)
reader1 = NewSimpleMFRC522()

try:
    print("Place tag...")
    status1, TagType1 = reader1.MFRC522_Request(reader1.PICC_REQIDL)
    if status1 == reader1.MI_OK:
        print("1 yes")
    print("klaar")
finally:
    GPIO.cleanup()