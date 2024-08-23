'''
Nombre: dhtMQTT.py
Autor: David Velásquez
Fecha: 15-05-2024
Descripción: Monitorea la temperatura y humedad del ambiente (DHT22) conectado al pin
GPIO17 cada segundo y la envia a un servidor MQTT.
'''

# Librerías
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import json
import time

# Etiquetado de pines
DHT = adafruit_dht.DHT22(board.D17)

# Constantes
TENVIO = 1
BROKER = "192.168.10.70"
PUERTO = 1883
USUARIO = "admin"
PASSWORD = "semillero"
TOPICO = "/rpi5-dvelas25/dht"

# Variables
temperatura = 0
humedad = 0

# Subrutinas y/o funciones
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f"Conectado al MQTT Broker: {BROKER}")
    else:
        print(f"Fallo en la conexión MQTT, código rc: {rc}")

# Configuración
## Comunicaciones
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.username_pw_set(USUARIO, PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.connect(BROKER, PUERTO)
mqtt_client.loop_start()

# Ejecución
while True:
    try:
        temperatura = DHT.temperature
        humedad = DHT.humidity
        print(f"Temperatura: {temperatura} °C, Humedad: {humedad} %")
        payload = {
            "temperatura": temperatura,
            "humedad": humedad
        }
        mqtt_client.publish(TOPICO, json.dumps(payload))
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(TENVIO)
mqtt_client.loop_stop()
