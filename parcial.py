def solicitar_notas():
    Notas = []
    for i in range(1, 5):
        while True:
            nota = float(input(f'Ingrese la nota:{i} '))
            if nota < 0:
                print('La nota no puede ser negativo. Intentalo de nuevo.')
            else:
                Notas.append(nota)
                break
    return Notas


def calcular_promedio(Notas):
    return sum(Notas) / len(Notas)


def main():
    estudiantes = []

    while True:
        nombre = input('Ingrese el nombre del estudiante:')
        matricula = int(input("Ingrese la matricula del estudiante:"))

        Notas = solicitar_notas()
        promedio = calcular_promedio(Notas)

        estudiantes.append((nombre, matricula, promedio))

        opcion = input('¿ Deseas incluir otro estudiante? (si/no): ').lower()
        if opcion != 'si':
            break

    print('\npromedio de los estudiantes:')
    for nombre, matricula, promedio in estudiantes:
        print(f"Nombre: {nombre}, matricula: {
              matricula}, promedio:{promedio:.2f}")


if __name__ == "__main__":
    main()
