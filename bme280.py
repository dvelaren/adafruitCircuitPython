import board
from adafruit_bme280 import basic as adafruit_bme280
import time
i2c = board.I2C()
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)
sensor.sea_level_pressure = 1015

while True:
	print(f'Temperature: {sensor.temperature} °C') 
	print(f'Humidity: {sensor.relative_humidity}')
	print(f'Pressure: {sensor.pressure} hPa')
	print(f'Altitude: {sensor.altitude} meters\n')
	time.sleep(1)

