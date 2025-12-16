import time
import board
import adafruit_dht

# Use GPIO4 (BCM)
dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")

    except RuntimeError as error:
        # DHT sensors are slow & error-prone
        print(error.args[0])

    time.sleep(2)