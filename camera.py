from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
sense = SenseHat()
count = 0
anncount = 0
 
camera = PiCamera()

camera.start_recording('')
while anncount < 1800:
    temp = sense.get_temperature()
    bus.write_byte_data(0x60, 0x26, 0xB9)
    bus.write_byte_data(0x60, 0x13, 0x07)
    bus.write_byte_data(0x60, 0x26, 0xB9)
    time.sleep(1)
    data = bus.read_i2c_block_data(0x60, 0x00, 6)
    theight = ((data[1] * 65536) + (data[2] *256) + (data[3] & 0xF0)) / 16
    altitude = theight / 16.0
    altitudef = altitude * 3.280839895
    bus.write_byte_data(0x60, 0x26, 0x39)
    time.sleep(1)
    data = bus.read_i2c_block_data(0x60, 0x00, 4)
    pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    camera.annotate_text = str(temp) + "  " + 
    sleep (1)
    anncount += 1
camera.stop_recording()


