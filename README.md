# IoT project with RaspberryPi and Arduino


## Analysis of temperature level remotely
Aim to monitor and analyse the temperature, humidity and pressure measurements in the appartment and outside.
Provide visualization of the data directly from the cloud based DB.


### Setup
RaspberryPi used as main station to collect information from various sources.
For indoors measurements it reads signal directly from the connected sensor.
For outdoor data API of openweathermap.org is used.

### Features
#### Interactive dashboard:
Dashboar is hosted at InfluxData Cloud. It provides change of measurements in last 24 hours, for indoor temperature it shows minimal/maximal temperature over period and gauge with current value. For outdoor measurements temperature, humidity and pressure are presented:

![alt text](https://github.com/grevtsovkirill/dht_logger/blob/master/helpers/RDMPlots/dashboard.png)

#### Local copy of SQL database:
It's convenient to have online dashboard for monitoring and service for alerting, but it is essential to keep data.
Storage realised using reliable and fast relational database management system PostgreSQL.

#### Monitoring & Alerting:
Different notification levels from Ok to Critical are set with corresponding measurement thresholds.
Notifiactions are transmitted to slack, using webhooks:

![alt text](https://github.com/grevtsovkirill/dht_logger/blob/master/helpers/RDMPlots/slack_integration.png)


### Techinical details of setup
Setup includes RaspberryPi running with Raspbian 10 (buster), reading temerature measurement sensor DS18B20.
Uses libraries ```w1thermsensor``` and writhe data to ```InfluxDBCloud```.

Make a local backup to the PostrgeSQL database (```fill_sql.py```).

Run the code as daemon:
 - copy ```logger.service``` from ```helpers``` to the ```/etc/systemd/system/```
 - update the ```systemd``` units with ```sudo systemctl daemon-reload``` and reload ```systemctl enable logger.service```
 - start the deamon: ```sudo systemctl start logger.service ```
 - check the status: ```sudo systemctl status logger.service ```

Code to read sensor data with Arduino and transmit it to BT can be found at:
```
helpers/arduino_data/arduino_data.ino
```

Description of setting up BT on RPi can be found in twiki:
https://github.com/grevtsovkirill/dht_logger.wiki.git