import os
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep


camera = PiCamera()#camera started


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


while True: # run the code forever
    camera.start_preview()#gets a preview on your screen
    if GPIO.input(10) == GPIO.HIGH : #enter your GPIO button pin number
        print("Clicking photo")
        os.system("raspistill -o /home/pi/Desktop/image.jpg") #takes a photo and saves to Desktop
        sleep(2)

GPIO.cleanup() # Clean up the GPIO




