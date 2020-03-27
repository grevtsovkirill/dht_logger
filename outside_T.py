#!/usr/bin/python3

from urllib.request import urlopen
import json

apikey = "yourAPIkey" # get Free account at openweathermap.org/
city_id = 1234567 # search for your city ID
lat = 99.99999 # specify latitude 
lon = 0.00000  # specify longitude

input_type = "latlon"
if input_type is "id":
    url="http://api.openweathermap.org/data/2.5/weather?id="+str(city_id)+"&APPID="+apikey
elif input_type is "latlon":
    url="http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&APPID="+apikey
print(url)
meteo=urlopen(url).read()
meteo = meteo.decode('utf-8')
weather = json.loads(meteo)

for key in weather['main']:
    print (key," = ",weather['main'][key] )
