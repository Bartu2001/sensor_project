import csv
import time
import psycopg2
import json
import os
from datetime import datetime


# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mysecretpassword"
)
cur = conn.cursor()

# File Paths
# ============================================
csv_file_path = "../data/iot_telemetry_data.csv"
checkpoint_path = "checkpoint.json"

#Checkpoint Functions

def load_checkpoint():
    if not os.path.exists(checkpoint_path):
        return 0
    with open(checkpoint_path, "r") as f:
        return json.load(f).get("line", 0)

def save_checkpoint(line_number):
    with open(checkpoint_path, "w") as f:
        json.dump({"line": line_number}, f)

# Reading CSV into Memory

with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    data_rows = list(reader)

#Starting a Data Stream
index = load_checkpoint()
batch_size = 100  

while True:
    for i in range(batch_size):
        if index >= len(data_rows):
            print("✅ Tüm veriler işlendi. Sistem durduruluyor.")
            break  # tekrar yazmayı durdur

        row = data_rows[index]

        try:
            insert_query = """
                INSERT INTO public.sensor_data (ts, device, co, humidity, light, lpg, motion, smoke, temp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            def safe_float(val):
                try:
                    return float(val)
                except:
                    return None

            def safe_timestamp(val):
                try:
                    return datetime.fromtimestamp(float(val))
                except:
                    return None

            data = (
                safe_timestamp(row.get('ts')),
                row.get('device', None),
                safe_float(row.get('co')),
                safe_float(row.get('humidity')),
                row.get('light'),
                safe_float(row.get('lpg')),
                row.get('motion'),
                safe_float(row.get('smoke')),
                safe_float(row.get('temp'))
            )

            cur.execute(insert_query, data)
            conn.commit()
            print(f"[{index}] Inserted row: {data}")

        except Exception as e:
            print(f"[{index}] Skipped row due to error: {e}")
            conn.rollback()

        index += 1
        save_checkpoint(index)

    time.sleep(1)
