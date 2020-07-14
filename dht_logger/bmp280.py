#!/usr/bin/python3

import smbus2
import bme280


def request_data():
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    return data
def main():
    data = request_data()
    print(data.id)
    print(data.timestamp)
    print(data.temperature)
    print(data.pressure)
    print(data.humidity)
    print(data)

if __name__== "__main__":
  main()    
