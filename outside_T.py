#!/usr/bin/python3

from urllib.request import urlopen
import json
from user_info import *

sens = 'OpenWeather'
measurement_dict = {'temp':'T_out','pressure':'P_out','humidity':'H_out'}
read_types = ['temp','pressure','humidity']

def request_data():
    input_type = "latlon"
    if input_type is "id":
        url="http://api.openweathermap.org/data/2.5/weather?id="+str(city_id)+"&APPID="+apikey
    elif input_type is "latlon":
        url="http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&APPID="+apikey+"&units=metric"
        #print(url)
        meteo=urlopen(url).read()
        meteo = meteo.decode('utf-8')
        weather = json.loads(meteo)
        return weather
        
def get_out_reading(read_type):
    data = request_data()['main']    
    return sens,measurement_dict[read_type],data[read_type]
        
def main():
    weather = request_data()
    #for key in weather['main']:
    #    print (key," = ",weather['main'][key] )    
    for i in read_types:
        print(get_out_reading(i))

if __name__== "__main__":
  main()    
