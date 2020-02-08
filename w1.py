import subprocess
import json
import threading
import io
import time

from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
while True:
    current_temperature=sensor.get_temperature()
    print(current_temperature)
    time.sleep(1)
