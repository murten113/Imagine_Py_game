import RPi.GPIO as GPIO
import mfrc522

RST_PIN = 22  # Reset (Shared for all modules)
reader1 = mfrc522.SimpleMFRC522()

try:
    print("Place tag...")
    id = reader1.read()
    x = id.split(",")
    x1 = x[0].split("(")
    x2 = x1[1]
    print(x2)
finally:
    GPIO.cleanup()