import re
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place tag...")
    id, text = reader.read()

    # Find all numeric sequences in the text
    numbers = re.findall(r'\d+', text)

    if numbers:  # If at least one number is found
        last_number = numbers[-1]
        print("Last number:", last_number)
    else:
        print("No numbers found in text:", repr(text))

finally:
    GPIO.cleanup()
