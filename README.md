Steps to get the cameraPi working

1. Use GPIO pin number 10 (You can use any GPIO, change the code)

2. Given is the code named 'camera.py' in the directory (you can check inside)

3. Keep this directory('cameraPi') in /home/pi

To run this code on startup, you can do :

  1. Open terminal and type sudo nano /etc/rc.local
  2. Go to the down before 'exit 0' and paste python3 /home/pi/cameraPi/camera.py
  3. Ctrl + O to save the file
  4. Reboot and now it a shot. Press the button and you will get a image on the Desktop
