# Este script captura la pantalla y encuentra un objeto en ella, luego mueve el puntero al centro del objeto y hace clic.

import mss
import pyautogui
from PIL import Image

with mss.mss() as sct:
    # Captura la pantalla completa
    monitor = sct.monitors[1]
    sct_img = sct.grab(monitor)

    # Convierte la imagen a formato compatible con PIL
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    # Encuentra un objeto en la pantalla (ejemplo: una imagen)
    #location = pyautogui.locateOnScreen('image.png')
    location = pyautogui.locateOnScreen('image.png', confidence=0.8)


    if location:
        # Obtiene las coordenadas del centro del objeto
        center_x, center_y = pyautogui.center(location)
        print(f"Coordenadas del centro del objeto: x={center_x}, y={center_y}")

        # Mueve el ratón al centro del objeto
        pyautogui.moveTo(center_x, center_y)

        # Haz clic en el centro del objeto
        pyautogui.click(center_x, center_y)
    else:
        print("Objeto no encontrado en la pantalla.")