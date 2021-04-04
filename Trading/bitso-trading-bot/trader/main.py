#import sys
#import os
#sys.path.append(os.path.realpath('..'))


import requests
import bitso
import json
import requests
from tkinter import *
from PIL import Image
from PIL import ImageTk

from urllib.parse import urlparse
from urllib.parse import urlencode

WINDOWS_GEOMETRY = "800x600"

API_KEY 	= ""
API_SECRET 	= ""

IMG_BITSO_LOGO = "C:/Users/Aldo/Documents/Python/bitso-trading-bot/res/images/bitso_logo.png"
#IMG_BITSO_LOGO = "bitso-trading-bot/res/images/bitso_logo.png"

api = bitso.Api(API_KEY, API_SECRET)

# Interfaz de usuario

ui = Tk()
ui.geometry(WINDOWS_GEOMETRY)
ui.title = "Bitso trading bot"

ui_titulo = Label(ui,text="Welcome again")
ui_titulo.pack()    

image = Image.open(IMG_BITSO_LOGO)
#image = image.resize(200,200)
photo = ImageTk.PhotoImage(image)


label = Label(ui, image=photo, bd=0)
label.pack(anchor = NW, side="left")

ui.mainloop()


# [OK]Implementar una clase con funciones propias para no utilizar la api afuera
# [OK]Revisar el precio actual de coin que va a basarse la aplicacion con una funcion
# [BD]Revisar el precio de coin en una fecha y hora 
# [PR]Hacer una compra de coin
# [PR]Hacer una venta de coin
# Cancelar una compra
# Cancelar una venta
# Sacar grafica de precios
# 
# Cargar datos de precios como entrenamiento IA
# Simulacion de Comprar y vender automaticamente en lapsos
# Investigar si el tiempo de funcionamiento puede ser variable
# Utilizar predicciones de coin
# Despliegue

