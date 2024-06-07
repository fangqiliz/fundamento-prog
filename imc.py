peso_kg = float(input('Ingrese su peso (kg): '))
altura = float(input('Ingrese su altura (m): '))
peso_lb = peso_kg * 2.2
imc = peso_lb / altura**2
print(f'su indice de masa corporal es: {imc} ')
