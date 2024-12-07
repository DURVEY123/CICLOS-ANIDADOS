#cilos anidados
# es un ciclo que suele contener otros ciclos es decir hay uno exrterno y hay uno interno
#  (esto no implica que solo se pueden anidar 2) se usan para procesar datos de diferentes niveles o dimensiones


##
# for i in range(3):
#     for j in range(3):
#      print (f"i={i}, j={j}")


#se aplica para procesar matrices generar patrones visuales, resolver problemas jerarquicos como tableros o graficos
#concepto clave
#por cada iteracion del ciclo externo, el ciclo interno se ejecuta completamente
#procesamiento de matrices con ciclos anidados
#matriz en it: 
#es una lista [], donde cada elemento es una lista o una sublista, estas van a representar una fila



###ejemplo 1: imprimir una matriz de forma que quede representada como su representacion matematica
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()
# ########
# ########
# ########
# suma = 0
# for fila in matriz:
#     for elemento in fila:
#         suma += elemento       
# print (F"suma total es: {suma}")


# contador_pares = 0 
# for fila in matriz:
#     for elemento in fila:
#         if elemento %2 == 0:
#             contador_pares += 1
# print (f"hay {contador_pares} numeros pares en la matriz")  


#generacion de patrones visuales con ciclos 

##triangulo de numeros
# n = int(input("indicame el numero de pisos que tendra el triangulo: "))
# for i in range (1, n + 1): 
#     for j in range (1, i + 1):
#         print(j, end= " ")
#     print ()

##triangulo invertido
# m = 10
# for i in range(m, 0, -1):
#     for j in range(1, i +1):
#        print (j, end=" ")
#     print ()

##tablero de ajedrez 
# n = 8

# for i in range (n):
#     for j in range (n):
#         if (i + j) %2 == 0:
#             print ("⬛", end= "")
#         else:
#             print ("⬜", end="")
#     print()

##hacer transposicion de matrices, teniendo en cuenta la matriz previamente definida

tranpuesta = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        tranpuesta[j][i] = matriz[i][j]

for fila in tranpuesta: 
    print(fila)