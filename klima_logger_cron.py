import os
from datetime import datetime
import sqlite3
import Adafruit_DHT
from gpiozero import CPUTemperature

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "klimalog.db")

zeitstempel = datetime.now().isoformat()
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

cpu = CPUTemperature()
cpu_temp_zero = cpu.temperature

# Creation of Database
connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS klimadaten(
    zeitstempel TIMESTAMP,
    Temperatur REAL,
    Luftfeuchte REAL
    );"""
cursor.execute(sql)

cursor.execute("""
                INSERT INTO klimadaten 
                    VALUES (?,?,?)
            """, 
            (zeitstempel, temperature, humidity)
            )
cursor.execute(sql)

sql2 = """
CREATE TABLE IF NOT EXISTS cpu_temp(
    zeitstempel TIMESTAMP,
    cpu_temp_zero REAL
    );"""
    
cursor.execute(sql2)

cursor.execute("""
            INSERT INTO cpu_temp 
                VALUES (?,?)
        """, 
        (zeitstempel, cpu_temp_zero)
        )

cursor.execute(sql2)
connection.commit()

connection.close()

