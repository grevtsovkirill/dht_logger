import sys
import time
import os
import json

from w1 import TempSens
from http.server import HTTPServer, BaseHTTPRequestHandler

#from lucky_n import LUCKY

class read_data():
    def __init__(self):
        self.sensor = TempSens()  
        #self.sensor = LUCKY()
    def sample(self):
        return self.sensor.get_readings(self.sensor)

    
class homeDataHTTP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        measurements = rd.sample()
        self.wfile.write(json.dumps(measurements[0]['fields']).encode('UTF-8'))

    def do_HEAD(self):
        self._set_headers()

rd = read_data()
        
while True:
    #measurements = rd.sample()
    #print(measurements[0]['fields'])
    server_address = ('http://192.168.0.10', 80)
    httpd = HTTPServer(server_address, homeDataHTTP)
    print('Sensor HTTP server running')
    httpd.serve_forever()

