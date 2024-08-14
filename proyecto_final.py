# proyecto de un sistema de biblioteca

libros = {}
usuarios = {}
prestamos = []
reservas = []


def agregar_libro(libros, libro_id, titulo, autor, cantidad):
    libros[libro_id] = {'Titulo': titulo,
                        'Autor': autor, 'Cantidad': cantidad}


def eliminar_libro(libros, libro_id):
    if libro_id in libros:
        del libros[libro_id]


def agregar_usuario(usuarios, usuario_id, nombre, email):
    usuarios[usuario_id] = {'Nombre': nombre, 'Email': email}


def eliminar_usuario(usuarios, usuario_id):
    if usuario_id in usuarios:
        del usuarios[usuario_id]


def registrar_prestamo(usuario_id, libro_id, fecha_prestamo):
    prestamos.append({'usuario_id': usuario_id, 'libro_id': libro_id,
                     'fecha de prestamo': fecha_prestamo, 'fecha_devolucion': None})


def registrar_devolucion(prestamos, usuario_id, libro_id, fecha_devolucion):
    for prestamo in prestamos:
        if prestamo['usuario_id'] == usuario_id and prestamo['libro_id'] == libro_id and not prestamo['fecha_devolucion']:
            prestamo['fecha_devolucion'] = fecha_devolucion
            break


def reservar_libro(reservas, usuario_id, libro_id, fecha_reserva):
    reservas.append({'Usuario_id': usuario_id, 'libro_id': libro_id,
                     'fecha_reserva': fecha_reserva, 'lista_espera': []})


def imprimir_libros(libros):
    print('Libros:')
    print()
    for libro_id, detalles in libros.items():
        print(f"ID: {libro_id}")
        for key, value in detalles.items():
            print(f"{key}: {value}")
        print()


def imprimir_usuarios(usuarios):
    print('Usuarios:')
    print()
    for usuario_id, detalles in usuarios.items():
        print(f'ID: {usuario_id}')
        for key, value in detalles.items():
            print(f'{key}: {value}')
        print()


def imprimir_prestamos(prestamos):
    print('Prestamos')
    print()
    for prestamo in prestamos:
        for key, value in prestamo.items():
            print(f'{key}: {value}')
        print()


def imprimir_reservas(reservas):
    print('Reservas')
    print()
    for reserva in reservas:
        for key, value in reserva.items():
            print(f'{key}: {value}')
        print()
