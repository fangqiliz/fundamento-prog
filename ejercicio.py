# Iteracion sobre la lista de nombres que imprima solamente los nombres que tengan igual o mas de tres vocales.

def contar_vocal(nombre):

    vocales = ['a', 'e', 'i', 'o', 'u']
    cont = 0
    for item in nombre:
        if item in vocales:
            cont += 1
    return cont


nombre = input('Ingrese el nombre: ')

if contar_vocal(nombre) >= 3:
    print(nombre)
else:
    print('Tiene menos de 3 vocales')
