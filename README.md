# IoT project with RaspberryPi and Arduino


## Analysis of temperature level remotely
Aim to monitor and analyse the reasings from the sensor using cloud solutions.


### Setup
Setup includes RaspberryPi running with Raspbian 10 (buster), reading temerature measurement sensor DS18B20.
Uses libraries ```w1thermsensor``` and writhe data to ```InfluxDBCloud```.

### Features
#### Interactive dashboard:
In the cloud, dashboars if created to monitor historical data in last 24 hours, shows minimal and maximal temperature and provide gauge with current measurements:
![alt text](https://github.com/grevtsovkirill/dht_logger/blob/master/helpers/RDMPlots/t_dash.png)

#### Monitoring & Alerting:
Different notification levels from Ok to Critical are set with corresponding measurement thresholds.
Notifiactions are transmitted to slack, using webhooks:
![alt text](https://github.com/grevtsovkirill/dht_logger/blob/master/helpers/RDMPlots/slack_integration.png)