import time
import board
import adafruit_dht


class Sensor:
    def __init__(self):
        self.dhtDevice = adafruit_dht.DHT11(board.D4)

    def read(self):
        try:
            temperature = self.dhtDevice.temperature
            humidity = self.dhtDevice.humidity
            return humidity, temperature
        except RuntimeError as error:
            print(error.args[0])
            return None, None