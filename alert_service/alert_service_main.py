import psycopg2
import time


#DATABASE CONNECTION

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mysecretpassword"
)
cur = conn.cursor()


🧠 ALERT THRESHOLDS
TEMP_THRESHOLD = 29.0     # Temperature threshold
CO_THRESHOLD = 8.0        # CO gas threshold
SMOKE_THRESHOLD = 0.02    # Smoke threshold

#LOOP: Data control
last_checked_id = 0  # Last checked row ID

while True:
    query = f"""
        SELECT id, ts, temp, co, smoke
        FROM public.sensor_data
        WHERE id > {last_checked_id}
        ORDER BY id ASC
        LIMIT 50;
    """
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        row_id, ts, temp, co, smoke = row
        last_checked_id = row_id  # We processed the row, update the ID

        if temp and temp > TEMP_THRESHOLD:
            print(f"[ALERT] 🚨 High Temperature at {ts}: {temp}°C")

        if co and co > CO_THRESHOLD:
            print(f"[ALERT] 💨 High CO Level at {ts}: {co}")

        if smoke and smoke > SMOKE_THRESHOLD:
            print(f"[ALERT] 🔥 High Smoke Level at {ts}: {smoke}")

    time.sleep(3)  # Check every 3 seconds
