'''
Nombre: dht.py
Autor: David Velásquez
Fecha: 15-05-2024
Descripción: Monitorea la temperatura y humedad del ambiente (DHT22) conectado al pin
GPIO17 cada segundo.
'''

# Librerías
import board
import adafruit_dht
import time

# Etiquetado de pines
DHT = adafruit_dht.DHT22(board.D17)

# Constantes
TLECTURA = 1

# Variables
temperatura = 0
humedad = 0

# Ejecución
while True:
    try:
        temperatura = DHT.temperature
        humedad = DHT.humidity
        print(f"Temperatura: {temperatura} °C, Humedad: {humedad} %")
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(TLECTURA)
