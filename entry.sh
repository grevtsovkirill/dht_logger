#!/bin/bash

import time
import adafruit_dht
import board 

dht_device = adafruit_dht.DHT11(board.D4)


while 1:
      temperature = dht_device.temperature
      print("T = ",temperature)
      time.sleep(100)
	 
