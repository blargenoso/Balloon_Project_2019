from sense_hat import SenseHat
import datetime
import time
from time import sleep
sense = SenseHat()

ticks = time.time()
doc = 0

sense.clear((100, 0, 100))
sleep(5)
sense.show_message("Starting")
sense.clear((100, 25, 100))
sleep(60)
count = 0
while doc < 4:
    csv = open('/media/pi/9083-4562/tempdata(' + str(doc) + ').csv', 'w')
    csv.write('time' + ',' + 'temp' + ',' + 'pressure' + ',' + 'humidity')
    csv.write('\n')
    count = 0
    doc += 1
    while count < 60:
        ticks = time.time()
        print (ticks)
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        tempf = (temp * 1.8) + 32
        print(str(tempf))
        
        csv.write('\n')
        csv.write(str(ticks)+ ',' + str(tempf) + ',' + str(pressure) + ',' + str(humidity))

        sense.show_message("working")
        sense.show_letter("W", (100, 50, 0))
        sleep(30)
        sense.clear((0, 0, 0))
        sleep(1)
        count += 1
sense.show_message("done")
sense.clear((0, 100, 0))
csv.close()
print('info.txt is closed')#



