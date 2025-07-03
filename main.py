# Este script es para mover el puntero al punto indicado y hacer clic

import pyautogui
import time

# Espera 2 segundos para darte tiempo a cambiar de ventana si es necesario
time.sleep(2)

# Mueve el puntero a la posición especificada con la velocidad indicada
x=(2548)
y=(72)
pyautogui.moveTo(x, y, duration=0.5)

# Realiza un clic izquierdo en la posición actual del puntero
pyautogui.click()