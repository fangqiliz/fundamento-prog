# Leer dos números enteros y si la diferencia entre los dos números es par
# mostrar en pantalla la suma de los dígitos de los números,
# si dicha diferencia es un número primo menor que 10 entonces
# mostrar en pantalla el producto de los dos números
# y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

n1 = int(input('ingrese el primer numero: '))
n2 = int(input('ingrese el segundo numero: '))


diferencia = abs(n1 - n2)

if diferencia % 2 == 0:
    print(f"La suma de los dígitos de los números es: {
          sum(int(digito) for digito in str(n1)) + sum(int(digito) for digito in str(n2))}")
elif diferencia in [2, 3, 5, 7]:
    print(n1*n2)
elif diferencia % 10 == 4:
    print('digitos del primer numero:')
    for digito in str(n1):
        print(digito)
    print('digitos del segundo numero:')
    for digito in str(n2):
        print(digito)
else:
    print('ninguna condicion se cumplio')
