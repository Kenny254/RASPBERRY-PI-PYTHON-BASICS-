import socket
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()
        
        
#This script is needed on the client side - we can simply use VLC with a network URL:
#$ vlc tcp/h264://my_pi_address:8000/
#There 2~3 seconds delay in my test on Raspberry Pi 2.
