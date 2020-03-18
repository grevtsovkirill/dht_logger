import subprocess
import json
import threading
import io
import time
import datetime
import os

#from w1thermsensor import W1ThermSensor
#sensor = W1ThermSensor()

class TempSens:
    def __init__(self, sid=None):        
        from w1thermsensor import W1ThermSensor
        self.sensor = W1ThermSensor(sensor_id=sid)
            
    def get_readings(self, sensor):
        current_temperature = self.sensor.get_temperature()
        return [
            {
                'measurement': 'home-data',
                'fields': {
                    'temperature': float(current_temperature)
                }
            }
        ]    

#while True:
#    current_temperature=sensor.get_temperature()
#    print(datetime.datetime.now(), " T=",current_temperature," C")
#    time.sleep(5)
