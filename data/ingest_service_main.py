#read data service
import csv
import time

csv_file_path = "../data/iot_telemetry_data.csv"

#open csv folder and read csv file
with open(csv_file_path , mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row) # print every row
        time.sleep(3) #wait 3 second

    