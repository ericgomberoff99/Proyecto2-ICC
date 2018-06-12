from random import randint

#Función para crear una tupla para el juego "campo minado"
def tupla_minada():
    lista = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
    print(lista)
    contador = 0
    minas = 0
    while minas < 3:
        mina = randint(0,5)
        if mina == 1:
            lista[contador] = "*!"
            minas = minas + 1
        contador = contador + 1
        if contador == 20:
            contador = 0
    tupla_llena = tuple(lista)
    return tupla_llena

#Invocar a la función "tupla_minada" y devolver el valor a una variable "tupla"
tupla = tupla_minada()
print(tupla)

n=0
linea=""
for i in tupla:
    linea = linea + " " + iter
    n=n+1
    if n%4==0:
        print(linea)
        print(" ")

