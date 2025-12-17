import csv
import time
from sensor import Sensor
from datetime import datetime
from collections import deque

LENGHT = 3 * 24 * 12 # 3 days of data at 5-minute intervals

class DataHandler:
    def __init__(self, length:int = 100 ):
        self.lenght = length
        self.readData()

    def readData(self):
        self.data = deque(maxlen=self.lenght)

        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                self.data.append(row)

    def writeData(self):
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["TimeStamp", "Humidity", "Temperature"])
            for row in self.data:
                writer.writerow(row)

    def appendData(self, humidity, temperature):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.append([timestamp, humidity, temperature])

class Watcher:
    def __init__(self):
        self.sensor = Sensor()
        self.dataBase = DataHandler(LENGHT)


    def run(self):
        while True:
            for i in range(3):
                humidity, temperature = self.sensor.read()
                if humidity is not None and temperature is not None:
                    self.dataBase.appendData(humidity, temperature)
                    self.dataBase.writeData()
                    break
                else:
                    time.sleep(1)
            time.sleep(300)  # Wait for 5 minutes

Watcher().run()