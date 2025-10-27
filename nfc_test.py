import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id, text = reader.read()
    # Split the text by spaces
    parts = text.split()
    # Get the last part
    last_part = parts[-1]
    print("Last part:", last_part)
finally:
    GPIO.cleanup()