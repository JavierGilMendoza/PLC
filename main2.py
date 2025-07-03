# Este script muestra las coordenadas de donde está posicionado el puntero

import pyautogui
import time

print("Mueve el mouse y presiona Ctrl+C para salir")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posición actual del mouse: {x}, {y}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nHecho.")