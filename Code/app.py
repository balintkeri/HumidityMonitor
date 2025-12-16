

from collections import deque

LENGHT = 3 * 24 * 12 # 3 days of data at 5-minute intervals

class DataHandler:
    def __init__(self, length:int = 100 ):
        self.lenght = length
        self.readData()

    def readData(self):
        pass