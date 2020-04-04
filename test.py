import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

# Open file
#filename = ":/test.csv"


try: while True:
	result = instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
	    print("Temperature: %-3.1f " % result.temperature)
		print("Humidity: %-3.1f %%" % result.humidity)

        now = datetime.datetime.now()
        recordtime = '{0:%Y%m%d}'.format(now)
        temp = ("Temperature: %-3.1f " % result.temperature)
        humi = ("Humidity: %-3.1f %%" % result.humidity)
        data = recordtime + "," +  temp + "," +  humi

		with open('log.csv', "w", encoding="utf-8", newline=",") as f:
		writer = csv.writer(f)
		writer.writerow(data)
		f.close()
		print("loggging done. see log.csv")

	    time.sleep(6)

except KeyboardInterrupt: print("Cleanup") GPIO.cleanup()
