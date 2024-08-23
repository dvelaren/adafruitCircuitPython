# Librerías
import board
import digitalio
import time

# Etiquetado de pines
SW1 = digitalio.DigitalInOut(board.D20)
LED = digitalio.DigitalInOut(board.D21)

# Constantes
TBLINK = 1

# Configuración
## Configuración de pines
SW1.direction = digitalio.Direction.INPUT
LED.direction = digitalio.Direction.OUTPUT
## Limpieza de salidas
LED.value = False

# Ejecución
while True:
    if SW1.value == True:
        LED.value = True
        print("LED: ON")
        time.sleep(TBLINK)
        LED.value = False
        print("LED: OFF")
        time.sleep(TBLINK)
    else:
        LED.value = False
        print("LED: OFF")
