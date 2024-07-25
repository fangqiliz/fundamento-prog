def saludos():
    return 'Hola'


msj = saludos()
print(msj)


def suma(n1, n2):
    return n1 + n2


resultado = suma(3, 4)


print(resultado)


def area_rectangulo(base, altura):
    return base * altura


base = int(input('ingresa la base del rectangulo: '))
altura = int(input('ingresa la altura del rectangulo: '))

area = area_rectangulo(base, altura)
print(f'El area del rectangulo es: {area}')


def par_o_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'


num = int(input('ingresa un numero entero: '))
result = par_o_impar(num)

print(result)


def max_tres(num1, num2, num3):
    return max(num1, num2, num3)


num1 = int(input('ingresa un numero entero: '))
num2 = int(input('ingresa un numero entero: '))
num3 = int(input('ingresa un numero entero: '))


resultado2 = max_tres(num1, num2, num3)
print(f'El numero mayor es : {resultado2}')


def es_primo(numero):
    if numero < 1:
        return 'No es primo'
    if numero == 2:
        return 'Es primo'
    if numero % 2 == 0:
        return 'No es primo'
    for i in range(3, int(numero**0.5)+1, 2):
        if numero % i == 0:
            return 'No es primo'

    return 'Es primo'


numero = int(input('ingresa un numero entero: '))
resultado3 = es_primo(numero)

print(f'{numero} es : {resultado3}')


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)


n = int(input('ingresa un numero entero: '))
resultado4 = fact(n)

print(f'El factorial de {n} : {resultado4}')


def contar_vocales(texto):

    vocales = ['a', 'e', 'i', 'o', 'u']
    cont = 0
    for item in texto:
        if item in vocales:
            cont += 1
    return cont


texto = input('ingresa un texto: ').lower()
result2 = contar_vocales(texto)


print(f'El texto tiene {result2} vocales')


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit


grado_celsius = float(input('Ingrese el grado en celsius: '))

grado_fahrenheit = celsius_fahrenheit(grado_celsius)
print(f'{grado_celsius}  grados celsius son en fahrenheit {
      grado_fahrenheit} grados')


def es_palindromo(frase):
    frase = frase.replace(' ', ' ').lower()
    return frase == frase[::-1]


texto = input('Ingresa un texto: ')
resultado = es_palindromo(texto)
if resultado:
    print(f'{texto} es palindromo ')
else:
    print(f'{texto} no es palindromo')
