from helper.config import Config
import os
import sqlite3
import pandas as pd

def build_df_from_db():
    script_dir = os.path.dirname(__file__)
    rel_path = Config.PATH_2_DB_TARGET_LOCATION
    abs_file_path = os.path.join(script_dir, rel_path)

    # Getting Database and turning it to a data frame
    connection = sqlite3.connect(abs_file_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM klimadaten where datetime(zeitstempel) >=datetime('now', '-24 Hour', 'localtime')")
    db_data_raw = cursor.fetchall()

    cursor.execute("SELECT * FROM cpu_temp ORDER BY cpu_temp_zero DESC LIMIT 1")
    db_data_cpu_temp = cursor.fetchall()

    df = pd.DataFrame(db_data_raw, columns=["Timestamp", "Temperature", "Humidity"])

    connection.close()

    return df, db_data_cpu_temp[0][1]
