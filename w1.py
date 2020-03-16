import subprocess
import json
import threading
import io
import time
import datetime

from w1thermsensor import W1ThermSensor

def get_line_protocol(sensor, reading, value):
	line = "{} {}={} {}"
	timestamp = str(int(datetime.datetime.now().timestamp() * 1000))
	return line.format(sensor, reading, value, timestamp)
    
sensor = W1ThermSensor()
while True:
    current_temperature=sensor.get_temperature()
    #print(datetime.datetime.now(), "\t",current_temperature)
    sens='DS18B20'
    reading='T'
    value=current_temperature
    print(get_line_protocol(sens, reading, value))
    time.sleep(5)

