#!/bin/bash

import time
import board 
import digitalio
import adafruit_dht

pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

dht_device = adafruit_dht.DHT11(board.D4)


while 1:
      temperature = dht_device.temperature
      print("T = ",temperature)
      time.sleep(100)
	 
