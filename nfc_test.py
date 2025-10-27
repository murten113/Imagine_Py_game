import re
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id, text = reader.read()

    # Clean up the text — remove nulls, newlines, and extra spaces
    text = text.strip().replace('\x00', '')

    # Find all sequences of digits
    numbers = re.findall(r'\d+', text)

    if numbers:
        last_number = numbers[-1]
        print("Last number:", last_number)
    else:
        print("No numbers found in text:", repr(text))

finally:
    GPIO.cleanup()
