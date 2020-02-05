#!/bin/bash

import time
import adafruit_dht
from board import 4

dht_device = adafruit_dht.DHT11(4)


while 1:
      temperature = dht_device.temperature
      print("T = ",temperature)
      time.sleep(100)
	 
