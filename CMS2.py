##EJERCICIO 2

from typing import List, Dict

def unir_diccionarios(a_unir: List[Dict[str, str]]) -> Dict[str, List[str]]:
    resultado = {}

    for diccionario in a_unir:
        for clave, valor in diccionario.items():
            if clave in resultado:
                resultado[clave].append(valor)
            else:
                resultado[clave] = [valor]

    return resultado


if __name__ == '__main__':
    import json

    x = json.loads(input())
    print(unir_diccionarios(x))


#EJERCICIO 3

from queue import Queue
from typing import List, Dict, Union
import json

def procesamiento_pedidos(pedidos: Queue,
                    stock_productos: Dict[str, int],
                    precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, Union[int, float]]]]]:
    res = []

    while not pedidos.empty():
        pedido = pedidos.get()
        id_pedido = pedido['id']
        cliente = pedido['cliente']
        productos = pedido['productos']
        total_pedido = 0.0
        completo = True
        productos_actualizados = {}

        for producto, cantidad in productos.items():
            if producto in stock_productos and stock_productos[producto] >= cantidad:
                precio_producto = precios_productos[producto]
                total_producto = precio_producto * cantidad
                total_pedido += total_producto
                stock_productos[producto] -= cantidad
                productos_actualizados[producto] = cantidad
            else:
                completo = False
                if producto in stock_productos:
                    cantidad_disponible = stock_productos[producto]
                    productos_actualizados[producto] = cantidad_disponible
                    total_producto = precios_productos[producto] * cantidad_disponible
                    total_pedido += total_producto
                    stock_productos[producto] = 0
                else:
                    productos_actualizados[producto] = 0

        estado = 'completo' if completo else 'incompleto'

        pedido_actualizado = {
            'id': id_pedido,
            'cliente': cliente,
            'productos': productos_actualizados,
            'precio_total': round(total_pedido, 2),
            'estado': estado
        }

        res.append(pedido_actualizado)

    return res


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}


#EJERCICIO 4

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
from queue import Queue

def avanzarFila(fila: Queue, min: int):
    personas = fila.qsize()
    minuto = 0
    caja3 = 0
    while minuto <= min:
        if minuto % 4 == 0:
            fila.put(personas + 1)
            personas = personas + 1
        if minuto % 10 == 1 and not fila.empty():
            fila.get()
        if minuto % 4 == 3 and not fila.empty():
            fila.get()
        if minuto % 4 == 2 and not fila.empty():
            caja3 = fila.get()
        if minuto % 3 == 2 and minuto > 2 and not fila.empty():
            fila.put(caja3)

        minuto = minuto + 1


  #implementar función

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)