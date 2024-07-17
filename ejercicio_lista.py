# 1.       Leer 10 enteros, almacenarlos en una lista y
# determinar en qué posición del arreglo está el mayor número leído.

import math


def leer_enteros():
    numeros = []
    for i in range(10):
        num = int(input(f'Ingrese el numero: '))
        numeros.append(num)

    num_mayor = max(numeros)
    posicion_mayor = numeros.index(num_mayor)

    print(f'El numero mayor es {
          num_mayor} y se encuentar en la posicion {posicion_mayor}')


leer_enteros()


# 2.       Leer 10 enteros, almacenarlos en una lista y
# determinar en qué posición de del arreglo está el mayor número par leído.

def posicion_mayor_par(lista):
    max_par = float('-inf')
    pos_max_par = -1

    for i in range(len(lista)):
        if lista[i] > max_par:
            max_par = lista[i]
            pos_max_par = i

    return pos_max_par


def main():
    numeros2 = []
    for i in range(10):
        num = int(input(f'Ingrese el numero: '))
        numeros2.append(num)

        posicion = posicion_mayor_par(numeros2)

        if posicion == -1:
            print('No se encontro ningun numero par en la lista')
        else:
            print(f'El numero par {
                  numeros2[posicion]} esta en la posicion {posicion}')


main()


# 3.       Leer 10 enteros, almacenarlos en una lista y
# determinar en qué posición del arreglo está el mayor número primo leído.


def es_primo(numero):
    if numero < 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5)+1, 2):
        if numero % i == 0:
            return False

    return True


def posicion_mayor_primo(numeros3):
    max_primo = float('-inf')
    pos_max_primo = -1

    for i in range(len(numeros3)):
        if es_primo(numeros3[i]):
            if numeros3[i] > max_primo:
                max_primo = numeros3[i]
                pos_max_primo = i

    return pos_max_primo


def main2():
    numeros3 = []
    for i in range(10):
        num = int(input(f'Ingrese el numero: '))
        numeros3.append(num)

        posicion = posicion_mayor_primo(numeros3)

        if posicion == -1:
            print('No se encontro ningun numero par en la lista')
        else:
            print(f'El mayor numero primo {
                  numeros3[posicion]} esta en la posicion {posicion}')


main2()

# 4.       Leer 10 números enteros, almacenarlos en una lista y
# determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo


def es_primos(digito):
    return digito in {2, 3, 5, 7}


def contar_numeros_con_digitos_primo(numeros4):
    contador = 0
    for numero in numeros4:
        primer_dig = int(str(abs(numero))[0])
        if es_primos(primer_dig):
            contador += 1
    return contador


numeros4 = []
for _ in range(10):
    num = int(input('Ingrese un numero entero: '))
    numeros4.append(num)

resultado = contar_numeros_con_digitos_primo(numeros4)

print(f'cantidad de numeros que comienzan con un digitos primo: {resultado}')


# 5.       Leer 10 números enteros, almacenarlos en una lista y
# determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.

def es_primo2(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % 2 == 0:
            return False
    return True


def contar_dig_pares(numero):
    contador = 0
    for digito in str(abs(numero)):
        if int(digito) % 2 == 0:
            contador += 1
        return contador


numeros5 = []
for _ in range(10):
    num = int(input('Ingrese un numero entero: '))
    numeros5.append(num)

max_pares = -1
posicion_max_pares = -1

for i, num in enumerate(numeros5):
    if es_primo2(num):
        pares = contar_dig_pares(num)
        if pares > max_pares:
            max_pares = pares
            posicion_max_pares = i

if posicion_max_pares != -1:
    print(f'El numero primo con la mayor cantidad de digitos pares esta en la posicion {
          posicion_max_pares}')
else:
    print('No hay numeros primos en la lista')

# 6.       Leer 10 números enteros, almacenarlos en una lista y
# determinar en qué posiciones se encuentran los números con más de 3 dígitos

numeros6 = []
for i in range(10):
    num = int(input('Ingrese un numero entero: '))
    numeros6.append(num)

posiciones_mas_3_digitos = [i for i, num in enumerate(
    numeros6) if len(str(abs(num))) > 3]

print(f'las posiciones de los numeros con mas de 3 digitos son: {
      posiciones_mas_3_digitos}')


# 7.       Leer 10 números enteros, almacenarlos en una lista y
# determinar a cuánto es igual el promedio entero de los datos de la lista

numeros7 = []
for i in range(10):
    num = int(input('Ingrese un numero entero: '))
    numeros7.append(num)

promedio = sum(numeros7) // len(numeros7)

print(f'El promedio de los datos de la lista es: {promedio}')


# 8.       Leer 10 números enteros, almacenarlos en una lista y
# determinar cuántos números negativos hay.

numeros8 = []
for i in range(10):
    num = int(input('ingrese un numero entero: '))
    numeros8.append(num)

contador_negativo = 0
for num in numeros8:
    if num < 0:
        contador_negativo += 1

print(f'La cantidad de numeros negativos en la lista es: {contador_negativo}')

# 9.       Leer 10 números enteros, almacenarlos en una lista y
# calcular la factorial a cada uno de los números leídos almacenándolos en otra lista


numeros10 = []
for i in range(10):
    num = int(input('Ingrese un numero entero: '))
    numeros10.append(num)

factoriales = []
for num in numeros10:
    factorial = math.factorial(num)
    factoriales.append(factorial)

print('Los factoriales de los numeros ingresados son: ')
for i, factorial in enumerate(factoriales):
    print(f'Factorial de {numeros10[i]}:{factorial}')


# 10.   Leer 10 números enteros, almacenarlos en una lista.Luego leer un entero y
# determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.


numeros11 = []
for _ in range(10):
    num = int(input('Ingrese un numero entero:'))
    numeros11.append(num)

num_extra = int(input('Ingrese un numero adicional:'))

divisores_exacto = 0
for num in numeros11:
    if num_extra % num == 0:
        divisores_exacto += 1

print(f'El numero {num_extra} tiene {
      divisores_exacto} divisores exactos entre los almacenados en al lista')
