import RPi.GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id,text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()