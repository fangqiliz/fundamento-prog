libros = {}
usuarios = {}
prestamos = []


def agregar_libro(libros, libro_id, titulo, autor, cantidad):
    libros[libro_id] = {'Titulo': titulo,
                        'Autor': autor, 'Cantidad': cantidad}


def eliminar_libro(libro_id):
    if libro_id in libros:
        del libros[libro_id]


def agregar_usuario(usuario_id, nombre, email):
    usuarios[usuario_id] = {'Nombre': nombre, 'Email': email}


def eliminar_usuario(usuario_id):
    if usuario_id in usuarios:
        del usuarios[usuario_id]


def registrar_prestamo(usuario_id, libro_id, fecha_prestamo):
    prestamos.append({'usuario_id': usuario_id, 'libro_id': libro_id,
                     'fecha de prestamo': fecha_prestamo, 'fecha_devolucion': None})


def resgistrar_devolucion(prestamos, usuario_id, libro_id, fecha_devolucion):
    for prestamo in prestamos:
        if prestamo['usuario_id'] == usuario_id and prestamo['libro_id'] == libro_id and not prestamo['fecha_devolucion']:
            prestamo['fecha_devolucion'] = fecha_devolucion
            break
