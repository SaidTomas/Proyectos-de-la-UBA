## EJERCICIO 1
import sys

def juegaBien(j:str) -> bool:
 opciones = ["Piedra", "Papel", "Tijera"]
 return j in opciones
  
def gana(j1:str, j2:str): 
  if j1 == j2:
    return "empate"
  
  def piedraGanaATijera(j1:str, j2:str) -> bool:
     if (j1 == "Piedra" and j2 == "Tijera"):
       return True
     else:
       return False

  def tijeraGanaAPapel(j1:str, j2:str) -> bool:
     if (j1 == "Tijera" and j2 == "Papel"):
       return True
     else:
       return False

  def papelGanaAPiedra(j1:str, j2:str) -> bool:
     if (j1 == "Papel" and j2 == "Piedra"):
       return True
     else:
       return False
  
  return piedraGanaATijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2) 

def quienGana(j1:str, j2:str) -> str:
  if juegaBien(j1) and juegaBien(j2) == True:
   if gana(j1, j2) == True:
    return "Jugador1"
   if gana(j1, j2) == False:
    return "Jugador2"
   if (j1) == (j2):
    return "Empate"
   
if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))

## EJERCICIO 2

import sys  

def esSecuenciaFibonacci(l: int) -> bool:
 if len(l) > 0 and l[0] != 0:
  return False
 if len(l) > 0 and l[1] != 1:
  return False
 for i in range(2, len(l)):
   if l[i] != l[i - 1] + l[i - 2]:
       return False
 return True
  
def fibonacciNoRecursivo(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  fibonacciSeq:list([int]) = [0, 1]
  for i in range(2, n + 1):
        fibonacciSeq.append(fibonacciSeq[-1] + fibonacciSeq[-2])
  if len(fibonacciSeq) == n + 1:
    return fibonacciSeq[-1]

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(1))

## EJERCICIO 3


def todosIguales(l: List[int], i:int, j:int) -> bool:
    for k in range(i, j+1):
        if l[k] != l[i]:
            return False
    return True

def hayMesetaDeLong(l: List[int], n:int) -> bool:
  for i in range(len(l)):
    if i + n - 1 < len(l) and todosIguales(l, i, i + n - 1):
      return True
  return False

def mesetaMasLarga(l: List[int]) -> int:
  mesetaLarga = 0
  for i in range(len(l)):
    for j in range(i, len(l)):
      if todosIguales(l, i, j) and (j - i + 1 > mesetaLarga):
        mesetaLarga = j - i + 1
  return mesetaLarga

## EJERCICIO 4

from typing import List



def filaAnteriorMasN(m: List[List[int]], i:int, n:int) -> bool :
   if i > 0 and i < len(m):
        for j in range(len(m[0])):
            if m[i][j] != m[i - 1][j] + n:
                return False
        return True
   else:
        return False
   

def filasParecidasAanterior(l: List[List[int]], n:int) -> bool :  
    for i in range(1, len(l)):
        if not filaAnteriorMasN(l, i, n):
            return False

    return True

def esMatriz (l: List[List[int]]) -> bool :  
  if len(l) > 0 and len(l[0]) > 0: 
    for i in range (0, len(l)):
      if len(l[i]) != len(l[0]):
        return False    
    return True
  else: 
    return False
  
def filasParecidas (l: List[List[int]]) -> bool :
  if esMatriz(l) == True:
    for n in range (0, len(l)):
      if filasParecidasAanterior(l,n) == True:
        return True      
    return False
  else: 
    return False  



if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))


## EJERCICIO 5

from typing import List
from typing import Tuple

def laRuta (vuelos: List[Tuple[str,str]], origen:str, destino: str)->List[Tuple[str,str]]:
  ruta = []
  noRuta = []
  if(len(vuelos)<=1):
    return []
  for i in range(len(vuelos)):
    if(vuelos[i][0]==origen and vuelos[i][1]==destino):
        return [vuelos[i]]
    if(vuelos[i][0]==origen and vuelos[i][1]!=destino):
      ruta.append(vuelos[i])
      if(len(ruta)>0 and ruta[0][1]!=destino):
          for j in range(len(vuelos)):
              for h in range(len(vuelos)):
                if(ruta[-1][1] == vuelos[h][0] and ruta[-1][1]!=destino):
                  ruta.append(vuelos[h])
          if(ruta[-1][1]!=destino):
            return noRuta
          else:
            return ruta

def sinRepetidos(l:List[Tuple[str,str]])->List[Tuple[str,str]]:
  sinRep : List[Tuple[str,str]]=[]
  if(len(l)==0):
    return []
  for i in range(len(l)):
    if (l[i] not in sinRep):
      sinRep.append(l[i])
  return sinRep

def vuelosValidos (ruta: List[Tuple[str,str]] ,vuelos: List[Tuple[str,str]])->bool:
  if(len(ruta)<1):
    return False
  if(len(sinRepetidos(ruta))==len(ruta)):
    for i in range(len(ruta)):
      if(ruta[i] not in vuelos):
        return False
    return True
  else:
    return False

def caminoDeVuelos  (vuelos: List[Tuple[str,str]])->bool:
  for i in range (1,len(vuelos)):
    if (vuelos[i][0]!=vuelos[i-1][1]):
      return False
  return True

def hayRuta (vuelos: List[Tuple[str,str]], origen:str, destino:str)->bool:
  ruta :List[Tuple[str,str]]= laRuta(vuelos,origen,destino)
  if(vuelosValidos(ruta,vuelos)==True and len(ruta)>= 1):
    if(ruta[0][0]== origen and ruta[len(ruta)-1][1]==destino):
      if(caminoDeVuelos(ruta)==True):
        return True
  else:
    return False

def sePuedeLlegar (origen: str,destino: str, vuelos:List[Tuple[str,str]])->int :
  if(hayRuta(vuelos,origen,destino)==True):
    return len(laRuta(vuelos,origen,destino))
  else:
    return -1

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))