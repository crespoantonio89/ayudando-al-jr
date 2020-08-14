import json
from datetime import datetime

json_string = """

   [
            {
            "idcliente": 1,
            "fecha": "09/08/20 13:55:26",
            "idproducto": 3,
            "cantidad":1
            },
            {
            "idcliente": 1,
            "fecha": "09/08/20 13:55:26",
            "idproducto": 2,
            "cantidad":1
            },
            {
            "idcliente": 1,
            "fecha": "08/08/20 13:55:26",
            "idproducto": 3,
            "cantidad":1
            }
    ]
"""
#Toma la string de JSON y la convierte en una lista de diccionarios de Python (hash map).
buys_list = json.loads(json_string)
product_dates = {}

#Creo un diccionario donde la key es la id del producto y su value son las diferentes fechas de compra del producto.
def deserializer(buys_list):
    for buy in buys_list:
        product_id = buy['idproducto']
        if product_id not in product_dates:
            product_dates[product_id] = [datetime.strptime(buy['fecha'], '%d/%m/%y %H:%M:%S')]
        else:
            product_dates[product_id].append(datetime.strptime(buy['fecha'], '%d/%m/%y %H:%M:%S'))
    return product_dates

#Elimino los productos que no tengan mas de 1 compra.
def filterBuys(product_dates):
    keys_to_delete = [key for key in product_dates if len(product_dates[key]) < 2]
    for key in keys_to_delete: del product_dates[key]
    return product_dates

#Ordeno las fechas de compras de los productos en orden descendente.
def sortDates(product_dates):
    for date in product_dates:
        product_dates[date].sort(reverse=True)
    return product_dates

#Calculo la proxima fecha de compra sacando un average entre las compras del producto y sumandoselo a la fecha de la ultima compra.
#El metodo devuelve una lista de tuplas, donde las tuplas contienen la id del producto y su prediccion de proxima compra.
def getNextBuyDate(product_dates):
    next_buy_by_product = []
    for date in product_dates:
        list_size = len(product_dates[date]) - 1
        last_buy = product_dates[date][0]
        avg_time = product_dates[date][0] - product_dates[date][1]
        for i in range(1,list_size):
            avg_time += product_dates[date][i] - product_dates[date][i+1]
        avg_time = avg_time / list_size 
        next_buy =  last_buy + avg_time
        next_buy_by_product.append((date,str(next_buy)))
    return next_buy_by_product

deserializer(buys_list)
filterBuys(product_dates)
sortDates(product_dates)
print(getNextBuyDate(product_dates))

