import csv

from datetime import datetime
from collections import deque

LENGHT = 3 * 24 * 12 # 3 days of data at 5-minute intervals

class DataHandler:
    def __init__(self, length:int = 100 ):
        self.lenght = length
        self.readData()

    def readData(self):
        self.data = deque(maxlen=self.lenght)

    def writeData(self):
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["TimeStamp", "Humidity", "Temperature"])
            for row in self.data:
                print(row)
                writer.writerow(row)

    def appendData(self, humidity, temperature):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.append([timestamp, humidity, temperature])

db = DataHandler(LENGHT)

db.appendData(50.2, 23.4)
db.writeData()