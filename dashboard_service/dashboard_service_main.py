import streamlit as st
import psycopg2
import pandas as pd

# STREAMLIT PAGE SETTINGS

st.set_page_config(page_title="Sensor Dashboard", layout="wide")
st.title("📊 Sensor Dashboard")
st.write("""
This dashboard monitors real-time sensor data from the environment.  
Each chart includes a brief explanation below to help interpret the trends.
""")

# DATABASE CONNECTION - DATA FETCH FUNCTION

def get_sensor_data():
    """
    Retrieves the last 100 sensor data entries from PostgreSQL.
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="mysecretpassword"
        )
        query = """
            SELECT ts, temp, humidity, light, co, lpg, smoke, motion
            FROM public.sensor_data
            ORDER BY ts DESC
            LIMIT 100
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df.sort_values(by='ts')  # Oldest to newest
    except Exception as e:
        st.error(f"Error retrieving data: {e}")
        return pd.DataFrame()

# 📥 FETCH DATA

df = get_sensor_data()

if df.empty:
    st.warning("No data found or unable to retrieve data.")
    st.stop()
    
#  TEMPERATURE & HUMIDITY LINE CHART

st.subheader("🌡️ Temperature and Humidity Over Time")
st.line_chart(df.set_index('ts')[['temp', 'humidity']])
st.write("""
**Chart Description:**  
- **X-axis**: Time (when each sensor reading was recorded)  
- **Y-axis**: Sensor readings  
  - 🔵 `temp` (°C): Ambient temperature  
  - 🟢 `humidity` (%): Relative humidity  
This chart helps monitor how temperature and humidity fluctuate together in real time.
""")

# LIGHT LEVEL LINE CHART

st.subheader("💡 Light Level Over Time")
st.line_chart(df.set_index('ts')[['light']])
st.write("""
**Chart Description:**  
- **X-axis**: Time  
- **Y-axis**: Light level (intensity)  
This chart shows how the lighting conditions of the environment vary over time.
""")

# GAS LEVELS MULTI-LINE CHART

st.subheader("🔥 Gas Levels (CO, Smoke, LPG)")
st.line_chart(df.set_index('ts')[['co', 'smoke', 'lpg']])
st.write("""
**Chart Description:**  
- **X-axis**: Time  
- **Y-axis**: Gas concentration levels  
  - 🔴 `co`: Carbon Monoxide  
  - 🟣 `smoke`: Smoke particles  
  - 🟠 `lpg`: LPG concentration  
Used for air quality and safety monitoring in the environment.
""")



# SMART CHART: TEMP vs HUMIDITY SCATTER

st.subheader("📉 Temperature vs Humidity Correlation")
st.scatter_chart(df[['temp', 'humidity']])
st.write("""
**Chart Description:**  
This scatter plot compares temperature and humidity.  
- As temperature rises, humidity typically drops (or vice versa).  
- Useful to observe physical environment behavior and sensor consistency.
""")
