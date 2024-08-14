from proyecto_final import (agregar_libro, agregar_usuario, eliminar_libro, eliminar_usuario, registrar_prestamo, registrar_devolucion,
                            reservar_libro,  imprimir_libros, imprimir_prestamos, imprimir_reservas, imprimir_usuarios)

libros = {}
usuarios = {}
prestamos = []
reservas = []


libro1 = {'id': '001', 'titulo': 'Cien años de soledad',
          'autor': 'Gabriel García Márquez', 'cantidad': 5}
libro2 = {'id': '002', 'titulo': 'Don Quijote de la Mancha',
          'autor': 'Miguel de Cervantes', 'cantidad': 3}
libro3 = {'id': '003', 'titulo': 'La odisea',
          'autor': 'Homero', 'cantidad': 4}
libro4 = {'id': '004', 'titulo': 'Orgullo y prejuicio',
          'autor': 'Jane Austen', 'cantidad': 5}
libro5 = {'id': '005', 'titulo': 'Matar a un ruiseñor',
          'autor': 'Harper Lee', 'cantidad': 7}

agregar_libro(libros, libro1['id'], libro1['titulo'],
              libro1['autor'], libro1['cantidad'])
agregar_libro(libros, libro2['id'], libro2['titulo'],
              libro2['autor'], libro2['cantidad'])
agregar_libro(libros, libro3['id'], libro3['titulo'],
              libro3['autor'], libro3['cantidad'])
agregar_libro(libros, libro4['id'], libro4['titulo'],
              libro4['autor'], libro4['cantidad'])
agregar_libro(libros, libro5['id'], libro5['titulo'],
              libro5['autor'], libro5['cantidad'])


usuario1 = {'id': 'u001', 'nombre': 'Juan Pérez', 'email': 'juan@perez.com'}
usuario2 = {'id': 'u002', 'nombre': 'Ana Gómez', 'email': 'ana@gomez.com'}
usuario3 = {'id': 'u003', 'nombre': 'Pablo Rodriguez',
            'email': 'pablo@rodriguez.com'}
usuario4 = {'id': 'u004', 'nombre': 'Rosa Martinez',
            'email': 'rosa@martinez.com'}


agregar_usuario(usuarios, usuario1['id'],
                usuario1['nombre'], usuario1['email'])
agregar_usuario(usuarios, usuario2['id'],
                usuario2['nombre'], usuario2['email'])
agregar_usuario(usuarios, usuario3['id'],
                usuario3['nombre'], usuario3['email'])
agregar_usuario(usuarios, usuario4['id'],
                usuario4['nombre'], usuario4['email'])


registrar_prestamo(usuario1['id'], libro1['id'], '2024-08-01')

reservar_libro(reservas, usuario2['id'], libro2['id'], '2024-08-07')


print("Estado Inicial:")
imprimir_libros(libros)
imprimir_usuarios(usuarios)
imprimir_prestamos(prestamos)
imprimir_reservas(reservas)

print('-'*60)
print("despues de eliminar")


eliminar_libro(libros, '001')
eliminar_usuario(usuarios, 'u001')
eliminar_libro(libros, '005')
eliminar_usuario(usuarios, 'u002')

imprimir_libros(libros)
imprimir_usuarios(usuarios)
