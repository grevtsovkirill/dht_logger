import subprocess
import json
import threading
import io
import time
import datetime
import argparse
import requests

from w1thermsensor import W1ThermSensor
from dht_logger import fill_sql
from dht_logger import user_info
from dht_logger import outside_T
from dht_logger import bmp280
#from dht_logger import btsr

parser = argparse.ArgumentParser(description='Upload data from sensor')
parser.add_argument('--debug', required=False, default=False, type=bool, help='For local checks ')
parser.add_argument('--token', required=True, type=str, help='Your InfluxDB REST token. This argument is required.')
#parser.add_argument('--org', required=False, type=str, default="your@mail.com", help='Your InfluxDB organization name. This argument is required.')
parser.add_argument('--url', required=False, type=str, default="https://us-west-2-1.aws.cloud2.influxdata.com/", help="defaults to Cloud 2")
parser.add_argument('--bucket', required=False, type=str, default="home_service", help="the bucket to write to") 
parser.add_argument('--delay', required=False, type=float, default=60, help="Delay between readings") 
args = parser.parse_args()


debug = vars(args)["debug"]
influx_url = vars(args)["url"]
influx_token = vars(args)["token"]
#organization = vars(args)["org"]
organization = user_info.infl_org
bucket = vars(args)["bucket"]
delay = vars(args)["delay"]
precision = "ms"

def get_line_protocol(sensor, reading, value):
        line = "{} {}={} {}"
        timestamp = str(int(datetime.datetime.now().timestamp()*1000))
        dt = int(datetime.datetime.now().timestamp())
        dt_object = datetime.datetime.fromtimestamp(dt) 
        #add_readings(sensor, reading, value, dt_object)
        return line.format(sensor, reading, value, timestamp)


def send_line(line):
    try:
        url = "{}api/v2/write?org={}&bucket={}&precision={}".format(influx_url, organization, bucket, precision)
        headers = {"Authorization": "Token {}".format(influx_token)}
        r = requests.post(url, data=line, headers=headers)

        if debug:
                print(line)
    except:
        print("oops")
        
def get_bedroom_reading():
        sensor = W1ThermSensor()
        current_temperature=sensor.get_temperature()
        sens='DS18B20'
        reading='T_bedroom'
        return sens,reading,current_temperature
        
while True:
    sens, reading, value = get_bedroom_reading()
    line=get_line_protocol(sens, reading, value)
    send_line(line)
    for i in outside_T.read_types:
        sens, reading, value = outside_T.get_out_reading(i)
        line=get_line_protocol(sens, reading, value)
        send_line(line)

    for i in bmp280.read_types:
        sens, reading, value = bmp280.get_bmp_reading(i)
        line=get_line_protocol(sens, reading, value)
        send_line(line)

    # for i in btsr.read_types:
    #     sens, reading, value = btsr.get_bt_reading(i)
    #     line=get_line_protocol(sens, reading, value)
    #     send_line(line)

    time.sleep(delay)
