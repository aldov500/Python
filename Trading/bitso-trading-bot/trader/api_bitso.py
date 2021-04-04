
import bitso

class bitso_api:
    api = 0
    api_key = ""
    api_secret = ""
    api_book = "empty"
    api_ticker = "ticker"
    
    # inicializa con un libro especificado
    def __init__(self,book):
        self.api = bitso.Api(self.api_key, self.api_secret)
        self.api_book = book
    
    # Obtiene una postura
    def get_ticker(self):
        self.api_ticker = self.api.ticker(self.api_book)
        print(self.api_ticker)
    
    ## En trasncurso de tanto tiempo, con tantas transacciones dividir las transacciones en espacios de tiempo y estar monitoreando
    ## En cada vuelta cambia un parametro de comprar o vender
    ## Llega el momento y ejecuta la accion

    # Obtiene el valor de la moneda en MXN
    def get_mxn_coinvalue(self,coin):
        ticker = self.api.ticker(str(coin) +"_mxn")
        return ticker.ask + ((ticker.high - ticker.ask)/2)

    # Los trades de esta funcion, por buy sell
    def get_trade(self):
        trades = self.api.trades(self.api_book)
        return trades
  
    # Muestra trades abiertos de ese libro
    def order_book_asks(self, book):
        orders = self.api.order_book(book)
        return orders
        
    def order_book_bids(self, book):
        orders = self.api.order_book(book)
        for bid in orders.bids:
            print(bid)

# Coin
coin = "btc"
# Book
book_selected = str(coin) + "_mxn"
# Init
test = bitso_api(book_selected)
# Coin Value
coin_value = test.get_mxn_coinvalue(coin)
# Coin Value
#coins = ["btc","mana","xrp","bch"]
#for coin in coins:
#    print(coin + " value: " + str(test.get_mxn_coinvalue(coin)) + " mxn")

# Books
#print("Venden")
#test.order_book_asks(book_selected)
#print("Compran")
#test.order_book_bids(book_selected)

# Trades
print("value of 1 " + str(coin) + " is " + str(coin_value) + str(" MXN"))
#trades = test.get_trade()
#for order in trades:
#    print("Precio " + str(order.price) + " Cant " + str(order.amount))
#    print("Total " + str(order.price * order.amount))
#    print("ID: " + str(order.tid))