import sys
import time
import os
import json

from w1 import TempSens
#from lucky_n import LUCKY

class read_data():
    def __init__(self):
        self.sensor = TempSens()  
        #self.sensor = LUCKY()
    def sample(self):
        return self.sensor.get_readings(self.sensor)

    
while True:
    rd = read_data()
    measurements = rd.sample()
    print(measurements[0]['fields'])
