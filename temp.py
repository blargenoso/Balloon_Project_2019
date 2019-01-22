# Import code dependencies
from sense_hat import SenseHat
import datetime
import time
from time import sleep
import smbus
# declare variables from dependencies
bus = smbus.SMBus(1)

sense = SenseHat()

led = 1
ticks = time.time()
doc = 0
# Some led stuff
sense.clear((100, 0, 100))
sleep(5)
sense.show_message("Starting")
sense.clear((100, 25, 100))
sleep(60)
count = 0
# Open doc
while doc < 4:
    csv = open('/media/pi/9083-4562/tempdata(' + str(doc) + ').csv', 'w')
    # doc header
    csv.write('time' + ',' + 'temp' + ',' + 'pressure' + ',' + 'humidity' + ',' + 'altitude')
    csv.write('\n')
    count = 0
    doc += 1
    # take data and insert it into the doc
    while count < 60:
        ticks = time.time()
        print (ticks)
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
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
  
        tempf = (temp * 1.8) + 32
        print(str(tempf))
        
        csv.write('\n')
        csv.write(str(ticks)+ ',' + str(tempf) + ',' + str(pressure) + ',' + str(humidity) + ',' + str(altitudef) )
        # turns led messages on or off
        if led == 1:
            sense.show_message("working")
            sense.show_letter("W", (100, 50, 0))
        sleep(28)
        sense.clear((0, 0, 0))
        sleep(1)
        count += 1
sense.show_message("done")
sense.clear((0, 100, 0))
csv.close()
print('Done!')



