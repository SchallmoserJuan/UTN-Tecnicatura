# Importacion de servicios
from dominio.Pelicula import pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

# Creacion del menu
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar peliculas')
        print('2. Listar peliculas')
        print('3. Eliminar peliculas')
        print('4. Salir')
        opcion = int(input('Ingrese una opción (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la pelicula: ')
            pelicula = pelicula()
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ha ocurrido un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')
    