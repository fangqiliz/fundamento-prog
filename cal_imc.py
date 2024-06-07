print('kg')
print('lb')
peso = input('ingrese el peso en lb o kg: ')

if peso == 'kg':
    peso_kg = float(input('Ingrese su peso (kg): '))
    altura = float(input('Ingrese su altura (m): '))
    imc = peso_kg / altura**2
    print(f'su indice de masa corporal es: {imc} ')

elif peso == 'lb':
    peso_lb = float(input('Ingrese su peso (lb): '))
    altura = float(input('Ingrese su altura (m): '))
    imc = peso_lb / altura**2
    print(f'su indice de masa corporal es: {imc} ')
