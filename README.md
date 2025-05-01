# 📡 Real-Time Sensor Data Pipeline
This project simulates a real-time sensor data pipeline using Python, PostgreSQL, and Streamlit.
It processes IoT sensor data from a CSV file, stores it in a database, visualizes it in real-time, and triggers alerts for critical values.

# 🗂️ Project Structure

sensor_project/


├── ingest_service/        # Reads CSV and writes to PostgreSQL (real-time)

├── dashboard_service/     # Streamlit dashboard for live visualizations

├── alert_service/         # Alerts (e.g., if temperature > 29)

├── data/                  # Raw CSV dataset (iot_telemetry_data.csv)

├── checkpoint.json        # Keeps track of current row index

├── requirements.txt       # Python dependencies

└── .gitignore             # Files ignored by Git

# ⚙️ Technologies Used
Python 3.11

PostgreSQL

Streamlit

psycopg2

Git & GitHub

🚀 How It Works


ingest_service reads 100 rows per second from the CSV file and writes to PostgreSQL

dashboard_service uses Streamlit to create live graphs and dashboards

alert_service continuously monitors the data and alerts when temperature > 29°C

checkpoint.json keeps track of the last processed row so the system can resume where it left off

# 🖥️ How to Run

# Ingest Service - sends data to PostgreSQL
cd ingest_service

python ingest_service_main.py

# Dashboard Service - shows real-time graphs
cd dashboard_service

streamlit run dashboard_service_main.py

# Alert Service - checks for temperature threshold
cd alert_service

python alert_service_main.py




# 📈 Sample Dashboards
Below are examples of real-time charts generated as part of the project:

🌡️ Temperature and Humidity Over Time
Shows how temperature and humidity change over time.

🔥 Gas Levels (CO, Smoke, LPG)
Displays concentrations of various gases in the environment.

💡 Light Level Over Time
Indicates whether the light sensor detected ON (true) or OFF (false).

📉 Temperature vs Humidity Correlation
A scatter plot analyzing the relationship between temperature and humidity.

These dashboards are dynamically generated using Streamlit, with real-time data pulled from PostgreSQL.


<img width="1350" alt="Ekran Resmi 2025-05-01 21 12 17" src="https://github.com/user-attachments/assets/f51d579d-a9df-41bd-b3e6-8474cb9a7fd6" />


---------------------------------

<img width="1389" alt="Ekran Resmi 2025-05-01 21 12 51" src="https://github.com/user-attachments/assets/80c25cde-e8dc-4814-a332-97e1edc7d1dc" />

---------------------------------

<img width="1349" alt="Ekran Resmi 2025-05-01 21 13 21" src="https://github.com/user-attachments/assets/14642717-5fcd-4f5c-8446-5c60a133a804" />


---------------------------------

<img width="1350" alt="Ekran Resmi 2025-05-01 21 13 49" src="https://github.com/user-attachments/assets/fd7fc6c2-599e-4d0a-905d-697f65bf5130" />














