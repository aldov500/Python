
import requests
import bitso
import json
import requests
import tkinter

from urllib.parse import urlparse
from urllib.parse import urlencode


API_KEY = "wUmhROErRz"
API_SECRET = "6b18e1e02d977e4ce04a865b5a7a2818"

api = bitso.Api(API_KEY, API_SECRET)

#print("Balances de la cuenta:")
#balance = api.balances()
#print(balance)


#print("Estado de cuenta:")
#status = api.account_status()
#print("Limite diario: " + str(status.daily_limit))
#print("Limite restante: " + str(status.daily_remaining))

#print("Libros disponibles: ")
#books = api.available_books()
#print(books)

#print("Trades de mana_btc: ")
#book_selected = "btc_mxn"

#F = open("data.txt","r+") 
#repite = F.read()

#print(repite)

#F.write(repite)
#F.close()

#book_selected = "mana_btc"
#tipo_cambio = 1

#books = api.available_books()
#print("Minimo trade MXN ")


api_balance = api.balances()
print(api_balance)

urljson = "https://bitso.com/api/v3/available_books"
url_response = requests.get(urljson)
#print(url_response.json())


trades = api.trades(book_selected)

oferta_venta = 20000000
oferta_compra = 0

#tid = 1

#for trade in trades:
#	print(trade)
#	if trade.maker_side == "sell":
#		if trade.price < oferta_venta:
#			tid = trade.tid
#			oferta_venta = trade.price
#	else:
#		if trade.price > oferta_compra:
#			oferta_compra = trade.price

#print("Mejor oferta venta es: " + str(oferta_venta))
#print("Realizar la compra en " + str(tid))
#print("Estan comprando a " + str(oferta_compra))

#orders = api.open_orders(book_selected)

#for order in orders: 	
#	print("Orden encontrada:")
#	print(order)

#print("Finalizado")

