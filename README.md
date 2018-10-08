# RASPBERRY-PI-PYTHON-BASICS-
This repo contains quick to configure raspberry pi python configurations to at least start up. Works on all versions.


1.First of all, with the Pi switched off, you’ll need to connect the Camera Module to the Raspberry Pi’s camera port, then start up the Pi and ensure the software is enabled.

2.Start up the Pi and open the Raspberry Pi Configuration Tool from the main menu.Ensure the camera software is enabled.

3.Now your camera is connected and the software is enabled, you can get started by trying out the camera preview.
Open Python 3 from the main menu.Open a new file and save it as camera.py. It’s important that you do not save it as picamera.py.




Part 2.

 for sure, you have to enable camera module in your Raspberry Pi/Raspbian setup.

- install vlc:
$ sudo apt-get install vlc

- Run the command in Terminal, or you can make a sh file (remember to make it runnable):
$ raspivid -o - -t 99999 -w 640 -h 360 -fps 25|cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264

Where 99999 is the length of the video, 99.999 seconds. You can change that to whatever you like. If you change it to 0 (zero) it will carry on indefinitely. (And CTRL+C to kill it at any time).

8090 is the port you assign.

Now you can play the stream video at http:<Raspberry Pi IP>:8090

(reference: http://raspi.tv/2013/how-to-stream-video-from-your-raspicam-to-your-nexus-7-tablet-using-vlc)

In my case, report error of "Invalid PCR value in ES_OUT_SET_(GROUP_)PCR !" Just ignore it, the stream video is playing, and show on RPi main monitor.
