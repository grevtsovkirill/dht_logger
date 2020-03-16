import subprocess
import json
import threading
import io
import time
import datetime
import argparse
import requests

from w1thermsensor import W1ThermSensor

parser = argparse.ArgumentParser(description='Upload data from sensor')
parser.add_argument('--wait', required=False, default=0, type=int, help='Second to wait after opening the connection')
parser.add_argument('--token', required=True, type=str, help='Your InfluxDB REST token. This argument is required.')
parser.add_argument('--org', required=False, type=str, default="grevtsovkirill@gmail.com", help='Your InfluxDB organization name. This argument is required.')
parser.add_argument('--url', required=False, type=str, default="https://us-west-2-1.aws.cloud2.influxdata.com/", help="defaults to Cloud 2")
parser.add_argument('--bucket', required=False, type=str, default="home_service", help="the bucket to write to") 
args = parser.parse_args()


influx_url = vars(args)["url"]
influx_token = vars(args)["token"]
organization = vars(args)["org"]
bucket = vars(args)["bucket"]
precision = "ms"

def get_line_protocol(sensor, reading, value):
	line = "{} {}={} {}"
	timestamp = str(int(datetime.datetime.now().timestamp() * 1000))
	return line.format(sensor, reading, value, timestamp)


def send_line(line):
    try:
        url = "{}api/v2/write?org={}&bucket={}&precision={}".format(influx_url, organization, bucket, precision)
        headers = {"Authorization": "Token {}".format(influx_token)}
        r = requests.post(url, data=line, headers=headers)
        print(line)
    except:
        # this is terrible
	# any time there is a problem with the server, data will be lost
	# this is a job for Telegraf
        print("oops")
        
              
sensor = W1ThermSensor()
while True:
    current_temperature=sensor.get_temperature()
    #print(datetime.datetime.now(), "\t",current_temperature)
    sens='DS18B20'
    reading='T'
    value=current_temperature
    line=get_line_protocol(sens, reading, value)
    send_line(line)
    time.sleep(5)

