#!/usr/bin/python3

from urllib.request import urlopen
import json
from user_info import *

input_type = "latlon"
if input_type is "id":
    url="http://api.openweathermap.org/data/2.5/weather?id="+str(city_id)+"&APPID="+apikey
elif input_type is "latlon":
    url="http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&APPID="+apikey+"&units=metric"
print(url)
meteo=urlopen(url).read()
meteo = meteo.decode('utf-8')
weather = json.loads(meteo)

for key in weather['main']:
    print (key," = ",weather['main'][key] )
