# Raspberry Pi DHT-22 Dashboard
<img src="https://github.com/marwonn/Raspberry-DHT-22-Dashboard/blob/master/app/static/img/line_chart.gif">

The idea for this project was to log the dht sensor output data over time. I have succsessfully integrated the dht-22 sensor via Homebridge into Homekit, but there wasn't any abillity to log the sensor data over the course of time. 

## Which tools respectively equipement did I use
- Raspberry Pi Zero WH plus DHT-22 sensor: This combination logs the temperature and humidity data every 5 minutes. In addition the cpu temperature of both Raspberrys is also stored in the database. The record intervall can be adjusted in *klima_logger.py*. The data is going to be stored in a sqlite file.

- Raspberry Pi 4B: This Raspi runs the local flask-server and pulls the database from the Raspi Zero. I tried to run the flask-server on the Raspi Zero but that was way too slow (due to the lack of RAM).

- The connection between the Raspi Zero and Raspi 4B is handled via SSH through the package *paramiko*.

- The interactive charts are created with *pygal*.

## How to start

1. Transfer and start the script *klima_logger.py* to the Raspi Zero
2. Transfer the app data to another Raspi with enough RAM
3. Adjust the script *config.py* with your local settings
4. Run ```pip install -r requirements.txt```
5. Run ```main.py```
6. Open ```127.0.0.1:8000/dashboard```

<img src="https://github.com/marwonn/Raspberry-DHT-22-Dashboard/blob/master/app/static/img/cpu.JPG">
<img src="https://github.com/marwonn/Raspberry-DHT-22-Dashboard/blob/master/app/static/img/Raspi-Dashboard_1.png">
<img src="https://github.com/marwonn/Raspberry-DHT-22-Dashboard/blob/master/app/static/img/bar_chart.JPG" width="400"> 

