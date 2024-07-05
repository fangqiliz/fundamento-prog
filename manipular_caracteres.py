text = input('Ingrese un texto: ')

text_mayuscula = text.upper()
print(f'Texto en mayuscula: {text_mayuscula}')

text_minuscula = text.lower()
print(f'Texto en minuscula: {text_minuscula}')

dos_primeros_caracteres = text[:2]
print(f'Los dos primeros caracteres son: {dos_primeros_caracteres}')

dos_ultimos_caracteres = text[-2:]
print(f'Los dos ultimos caracteres son: {dos_ultimos_caracteres}')

ultimo_caracter = text[-1]
cantidad_repeticion_ultimo_caracter = text.count(ultimo_caracter)
print(f'Cantidad de veces que se repite el ultimo caracter: {
      cantidad_repeticion_ultimo_caracter}')

text_invertido = text[::-1]
print(f'Texto invertido: {text_invertido}')
