# 1.Filtrar elementos: Utiliza listas y comprensiones para filtrar elementos basados en ciertos criterios.
# Por ejemplo, puedes filtrar una lista de números para obtener solo los números pares o impares,
# o filtrar una lista de cadenas para obtener solo las que contengan ciertas letras.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]

print("Números pares:", pares)

# 2. Operaciones matemáticas: Utiliza listas o tuplas para realizar operaciones matemáticas
# en conjuntos de datos. Por ejemplo, puedes sumar los elementos de una lista,
# obtener el producto de una tupla o calcular la media de una lista de números.

nums = [1, 2, 3, 4, 5]

media = sum(nums) / len(nums)

print("Media de los elementos:", media)

# 3.Acceder y modificar elementos: Utiliza índices para acceder a elementos
# específicos en listas, tuplas o diccionarios.
# También puedes modificar los valores de los elementos si es necesario.

Numeros = [10, 20, 30, 40, 50]
print(Numeros)

primer_elemento = Numeros[0]
print("Primer elemento:", primer_elemento)


ultimo_elemento = Numeros[-1]
print("Último elemento:", ultimo_elemento)


Numeros[2] = 35
print("Lista después de modificar el tercer elemento:", Numeros)
