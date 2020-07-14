#!/usr/bin/python3

import smbus2
import bme280

sens = 'BMP'
measurement_dict = {'temperature':'T_liv','pressure':'P_liv','humidity':'H_liv'}
read_types = ['temperature','pressure','humidity']

def request_data():
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    return data

def get_bmp_reading(read_type):
    data = request_data()
    mes = 0
    if read_type=='temperature': mes = data.temperature
    elif read_type=='pressure': mes = data.pressure
    elif read_type=='humidity': mes = data.humidity
    
    return sens,measurement_dict[read_type],mes


def main():
    data = request_data()
    for i in read_types:
        print(get_bmp_reading(i))

if __name__== "__main__":
    main()    
