#imports necessary files and functions
import os
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep


camera = PiCamera()#camera started


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering for board
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value off


while True: # run the code forever (Enjoy the camera, until you exit the code)
    camera.start_preview()# starts a preview of camera on your screen
    if GPIO.input(10) == GPIO.HIGH : #if you clicked the button, the value get from 0 to 1 (You can change the pin number)
        print("Clicking photo")
        os.system("raspistill -o /home/pi/Desktop/image.jpg") #takes a photo and saves to Desktop (you can change the destination)
        sleep(2)
	camera.stop_preview()


GPIO.cleanup() # Clean up the GPIO
