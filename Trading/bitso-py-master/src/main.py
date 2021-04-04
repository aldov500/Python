
import requests
import bitso
import json
import requests
from tkinter import *

from urllib.parse import urlparse
from urllib.parse import urlencode


API_KEY 	= "wUmhOErRz"
API_SECRET 	= ""

api = bitso.Api(API_KEY, API_SECRET)

# Interfaz de usuario
ui = Tk()

ui_TituloApp = Label(ui, text="Bitso master bot")
ui_TituloApp.pack()

ui_LabelYourBitcoins = Label(ui,text="Your bitcoin quantity ")
ui_LabelYourBitcoins.pack()




ui_titulo.pack()

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

