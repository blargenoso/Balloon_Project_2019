from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
sense = SenseHat()
count = 0
anncount = 0
 
camera = PiCamera()

camera.start_recording('')
while anncount < 20:
    temp = sense.get_temperature()
    camera.annotate_text = str(temp) + "  " + 
    sleep (1)
    anncount += 1
camera.stop_recording()


