from picamera import PiCamera
from time import sleep

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

# type 'omxplayer video.h264'  from terminal to play video
