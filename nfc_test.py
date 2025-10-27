import RPi.GPIO as GPIO
import mfrc522

RST_PIN = 22  # Reset (Shared for all modules)
reader1 = mfrc522.SimpleMFRC522()

try:
    print("Place tag...")
    id = reader1.read()
    print(id[0])
finally:
    GPIO.cleanup()