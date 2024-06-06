import random

numero_secreto = random.randint(1, 30)

print('Bienvenido al juego')
print('intenta adivinar el numero secreto del 1-30')

while True:
    intento = int(input('introduce un numero: '))

    if intento == numero_secreto:
        print('Felicidades has adivinado el numero')
        break
    elif abs(numero_secreto - intento) <= 10:
        print('caliente')
    else:
        print('frio')
